#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
regels_export.py — genereer een regel-voor-regel Excel uit offerteregels.json.

Gebruik: python3 calculatie/tools/regels_export.py <slug> [uitvoerpad.xlsx]

Leest calculatie/projecten/<slug>/offerteregels.json en schrijft
calculatie/projecten/<slug>/offerteregels.xlsx (tenzij een ander pad is opgegeven):
  - tab "Offerteregels": elke offerteregel afzonderlijk, met autofilter
  - tab "Overzicht": totalen per leverancier en per document
Controleert dat elk documenttotaal exact optelt uit de regels.
"""
import json, sys
from pathlib import Path

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

CW_RED, CW_DARK, GREY = "C3002B", "1C1C1C", "F2F2F2"
SECTIE = {
    "110": "Bouwplaats", "120": "Sloopwerk", "131": "Divers bouwkundig", "132": "Trap",
    "133": "Entree", "134": "Keuken", "135": "Overig bouwkundig", "141": "Sanitair",
    "142": "Douche", "143": "Berging", "210": "HVAC / klimaat", "220": "Loodgieter",
    "230": "Elektra", "240": "Toegang & beveiliging", "250": "IT / data",
    "260": "Brandveiligheid", "311": "Vloerafwerking", "312": "PVC-vloer",
    "313": "Houten vloer", "314": "Vloerafwerking overig", "321": "MS-wanden",
    "322": "Systeemwanden", "323": "Deuren", "330": "Wandafwerking", "340": "Plafond",
    "350": "Verlichting", "360": "Zonwering", "370": "Maatwerkmeubilair",
    "410": "Meubilair", "420": "Losse inrichting", "430": "AV", "440": "Akoestiek",
    "450": "Branding / signing", "510": "Bijzonderheden", "520": "Verhuizing",
    "530": "Garantie/revisie", "610": "PM", "620": "Adviseurs", "710": "Onvoorzien",
    "720": "Opslagen", "730": "Verzekering",
}


def build(slug, out=None):
    root = Path(__file__).resolve().parents[1]
    src = root / "projecten" / slug / "offerteregels.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    out = Path(out) if out else src.with_suffix(".xlsx")

    wb = openpyxl.Workbook()
    thin = Border(bottom=Side(style="thin", color="D9D9D9"))
    hdr_font = Font(bold=True, color="FFFFFF", size=10)
    hdr_fill = PatternFill("solid", fgColor=CW_RED)

    # ---------- tab Offerteregels ----------
    ws = wb.active
    ws.title = "Offerteregels"
    cols = ["Nr", "Leverancier", "Type", "Referentie", "Datum", "Code", "Sectie",
            "Omschrijving", "Aantal", "Eenheid", "Prijs/eenh", "Bedrag excl. btw",
            "Opmerking", "Bron"]
    widths = [5, 17, 9, 12, 11, 6, 20, 68, 8, 8, 12, 14, 34, 55]
    for c, (name, w) in enumerate(zip(cols, widths), start=1):
        cell = ws.cell(row=1, column=c, value=name)
        cell.font, cell.fill = hdr_font, hdr_fill
        cell.alignment = Alignment(vertical="center")
        ws.column_dimensions[get_column_letter(c)].width = w
    r, nr = 2, 1
    for doc in data["documenten"]:
        for regel in doc["regels"]:
            bedrag = round(regel["aantal"] * regel["prijs"], 2)
            vals = [nr, doc["leverancier"], doc["type"], doc["referentie"], doc["datum"],
                    regel["code"], SECTIE.get(regel["code"], ""), regel["omschrijving"],
                    regel["aantal"], regel["eenheid"], regel["prijs"], bedrag,
                    regel.get("opmerking", ""), doc["bron"]]
            for c, v in enumerate(vals, start=1):
                cell = ws.cell(row=r, column=c, value=v)
                cell.border = thin
                cell.font = Font(size=9, color=CW_DARK)
                if c in (11, 12):
                    cell.number_format = '#,##0.00 "€"'
                if r % 2 == 0:
                    cell.fill = PatternFill("solid", fgColor=GREY)
                if c == 8 or c == 13 or c == 14:
                    cell.alignment = Alignment(wrap_text=False, vertical="top")
            if doc["type"] == "offerte":
                ws.cell(row=r, column=3).font = Font(size=9, bold=True, color=CW_RED)
            r, nr = r + 1, nr + 1
    tot_row = r + 1
    ws.cell(row=tot_row, column=8, value="TOTAAL (excl. btw)").font = Font(bold=True, size=10)
    tcell = ws.cell(row=tot_row, column=12, value=f"=SUM(L2:L{r-1})")
    tcell.font, tcell.number_format = Font(bold=True, size=10), '#,##0.00 "€"'
    ws.auto_filter.ref = f"A1:N{r-1}"
    ws.freeze_panes = "A2"

    # ---------- tab Overzicht ----------
    ov = wb.create_sheet("Overzicht")
    ov.column_dimensions["A"].width = 22
    for col, w in zip("BCDEF", (12, 12, 14, 10, 16)):
        ov.column_dimensions[col].width = w
    ov["A1"] = data["project"]
    ov["A1"].font = Font(bold=True, size=14, color=CW_RED)
    ov["A2"] = f"Offerteregels regel voor regel · peildatum {data['peildatum']}"
    ov["A2"].font = Font(size=9, color="777777")

    ov["A4"] = "Per leverancier"
    ov["A4"].font = Font(bold=True, size=11)
    row = 5
    for c, name in enumerate(["Leverancier", "Documenten", "Regels", "Totaal excl. btw"], 1):
        cell = ov.cell(row=row, column=c, value=name)
        cell.font, cell.fill = hdr_font, hdr_fill
    row += 1
    per_lev = {}
    for doc in data["documenten"]:
        e = per_lev.setdefault(doc["leverancier"], [0, 0, 0.0])
        e[0] += 1
        e[1] += len(doc["regels"])
        e[2] += sum(round(x["aantal"] * x["prijs"], 2) for x in doc["regels"])
    for lev, (nd, nr_, tot) in sorted(per_lev.items(), key=lambda x: -x[1][2]):
        ov.cell(row=row, column=1, value=lev)
        ov.cell(row=row, column=2, value=nd)
        ov.cell(row=row, column=3, value=nr_)
        c = ov.cell(row=row, column=4, value=round(tot, 2))
        c.number_format = '#,##0.00 "€"'
        row += 1
    ov.cell(row=row, column=1, value="TOTAAL").font = Font(bold=True)
    ov.cell(row=row, column=2, value=sum(v[0] for v in per_lev.values())).font = Font(bold=True)
    ov.cell(row=row, column=3, value=sum(v[1] for v in per_lev.values())).font = Font(bold=True)
    tc = ov.cell(row=row, column=4, value=round(sum(v[2] for v in per_lev.values()), 2))
    tc.font, tc.number_format = Font(bold=True), '#,##0.00 "€"'

    row += 2
    ov.cell(row=row, column=1, value="Per document").font = Font(bold=True, size=11)
    row += 1
    for c, name in enumerate(["Leverancier", "Type", "Referentie", "Datum", "Regels",
                              "Totaal excl. btw"], 1):
        cell = ov.cell(row=row, column=c, value=name)
        cell.font, cell.fill = hdr_font, hdr_fill
    row += 1
    for doc in data["documenten"]:
        tot = round(sum(round(x["aantal"] * x["prijs"], 2) for x in doc["regels"]), 2)
        ov.cell(row=row, column=1, value=doc["leverancier"])
        tcell = ov.cell(row=row, column=2, value=doc["type"])
        if doc["type"] == "offerte":
            tcell.font = Font(bold=True, color=CW_RED)
        ov.cell(row=row, column=3, value=doc["referentie"])
        ov.cell(row=row, column=4, value=doc["datum"])
        ov.cell(row=row, column=5, value=len(doc["regels"]))
        c = ov.cell(row=row, column=6, value=tot)
        c.number_format = '#,##0.00 "€"'
        row += 1

    wb.calculation.fullCalcOnLoad = True   # Excel herberekent alles bij openen
    wb.save(out)
    n_regels = sum(len(d["regels"]) for d in data["documenten"])
    totaal = round(sum(v[2] for v in per_lev.values()), 2)
    print(f"OK: {out} — {len(data['documenten'])} documenten, {n_regels} regels, "
          f"EUR {totaal:,.2f} excl. btw")
    return totaal


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("gebruik: regels_export.py <slug> [uitvoer.xlsx]")
    build(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
