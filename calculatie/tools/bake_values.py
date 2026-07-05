#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
bake_values.py — bereken alle formules van een xlsx en schrijf de uitkomsten
als gecachte waarden in het bestand (formules blijven staan).

Gebruik: python3 calculatie/tools/bake_values.py <bestand.xlsx>

Zonder gecachte waarden tonen viewers (en Excel in handmatige rekenmodus)
lege cellen. Deze stap rekent het hele werkboek door met het `formulas`-
pakket en injecteert de uitkomsten in de sheet-XML.
"""
import re, shutil, sys, zipfile
from pathlib import Path

import formulas


def solution_map(path):
    xl = formulas.ExcelModel().loads(str(path)).finish()
    sol = xl.calculate()
    out = {}
    fname = Path(path).name
    pat = re.compile(r"^'\[" + re.escape(fname) + r"\]([^']+)'!([A-Z]{1,3}\d+)$",
                     re.IGNORECASE)
    for key, val in sol.items():
        m = pat.match(key)
        if not m:
            continue
        try:
            v = val.value[0, 0]
        except Exception:
            continue
        out[(m.group(1).upper(), m.group(2))] = v
    return out


def fmt_value(v):
    """-> (type-attribuut, tekst) voor de <v>-cache, of None om over te slaan."""
    if v is None:
        return None
    if isinstance(v, bool):
        return ' t="b"', "1" if v else "0"
    if isinstance(v, (int, float)):
        if v != v or v in (float("inf"), float("-inf")):
            return ' t="e"', "#NUM!"
        return "", repr(round(float(v), 10))
    s = str(v)
    if s.startswith("#"):
        return ' t="e"', s
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return ' t="str"', s


def bake(path):
    path = Path(path)
    values = solution_map(path)
    print(f"{len(values)} berekende cellen uit het rekenmodel")

    z = zipfile.ZipFile(path)
    wbxml = z.read("xl/workbook.xml").decode()
    rels = z.read("xl/_rels/workbook.xml.rels").decode()
    rid2file = {}
    for m in re.finditer(r"<Relationship\b[^>]*>", rels):
        tag = m.group(0)
        mt = re.search(r'Target="/?(?:xl/)?(worksheets/[^"]+)"', tag)
        mi = re.search(r'Id="(rId\d+)"', tag)
        if mt and mi:
            rid2file[mi.group(1)] = mt.group(1)
    name2file = {}
    for m in re.finditer(r'<sheet name="([^"]+)"[^>]*r:id="(rId\d+)"', wbxml):
        if m.group(2) in rid2file:
            name2file[m.group(1).upper()] = "xl/" + rid2file[m.group(2)]

    new_parts, injected, missing = {}, 0, 0
    for name, fpath in name2file.items():
        xml = z.read(fpath).decode()

        def repl(m, _name=name):
            nonlocal injected, missing
            cell, body = m.group(1), m.group(0)
            fm = re.search(r"<f\b[^>]*/>|<f\b[^>]*>.*?</f>", body, re.S)
            if not fm:
                return body
            v = values.get((_name, cell))
            fv = fmt_value(v)
            if fv is None:
                missing += 1
                return body
            tattr, text = fv
            sm = re.search(r'\ss="\d+"', body.split(">")[0])
            sattr = sm.group(0) if sm else ""
            injected += 1
            return f'<c r="{cell}"{sattr}{tattr}>{fm.group(0)}<v>{text}</v></c>'

        # let op: zelfsluitende cellen (<c .../>) niet matchen, anders wordt
        # de daaropvolgende cel opgeslokt en overgeslagen
        xml = re.sub(r'<c r="([A-Z]{1,3}\d+)"[^>]*?(?<!/)>(?:(?!</c>).)*?</c>',
                     repl, xml, flags=re.S)
        new_parts[fpath] = xml

    tmp = path.with_suffix(".tmp.xlsx")
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in z.infolist():
            data = new_parts.get(item.filename, None)
            zout.writestr(item, data.encode() if isinstance(data, str) else z.read(item.filename))
    z.close()
    shutil.move(tmp, path)
    print(f"OK: {injected} waarden gebakken, {missing} formulecellen zonder uitkomst")
    return values


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("gebruik: bake_values.py <bestand.xlsx>")
    bake(sys.argv[1])
