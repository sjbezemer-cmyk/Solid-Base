# -*- coding: utf-8 -*-
"""Vul Master_calculatie met offertes/opdrachten uit OneDrive SJB/Kioti 2."""
import openpyxl, re, datetime
from copy import copy

SRC = "/root/.claude/uploads/91ac974e-acf4-5bda-9388-9bdb44ace267/e254490d-Master_calculatie.xlsm"
OUT = "/tmp/claude-0/-home-user-Solid-Base/91ac974e-acf4-5bda-9388-9bdb44ace267/scratchpad/Kioti 2 - Calculatie inkoop leveranciers.xlsx"

wb = openpyxl.load_workbook(SRC, data_only=False)
ws = wb["4 | Calculation"]

# ---- 1. reset: alle itemrijen (herkenbaar aan M-formule =K{r}*L{r}) op K=0 ----
item_rows = []
for r in range(13, 619):
    m = ws.cell(row=r, column=13).value
    if isinstance(m, str) and m == f"=K{r}*L{r}":
        item_rows.append(r)
        if ws.cell(row=r, column=11).value not in (None, 0):
            ws.cell(row=r, column=11).value = 0
print(f"{len(item_rows)} itemrijen gereset (K=0)")

# ---- 2. sectiebereiken (uit SUM-formules) ----
sections = {}
for r in range(13, 644):
    g = ws.cell(row=r, column=7).value
    if isinstance(g, str):
        mt = re.match(r"=SUM\(G(\d+):G(\d+)\)", g)
        if mt and r != 623:
            sections[r] = (int(mt.group(1)), int(mt.group(2)))

SEC = {  # code -> sumrow
    "131": 64, "210": 205, "220": 213, "230": 237, "240": 257, "250": 280,
    "260": 304, "314": 339, "322": 368, "323": 372, "410": 480, "420": 494,
    "430": 511, "450": 543,
}
used = set()

def add_line(code, desc, party, price, note, qty=1):
    a, b = sections[SEC[code]]
    rows = list(range(a, b + 1))
    # eerst rijen zonder omschrijving, daarna (gereset) placeholder-rijen
    cand = [r for r in rows if r not in used and ws.cell(row=r, column=3).value in (None, "")] + \
           [r for r in rows if r not in used]
    if not cand:
        raise RuntimeError(f"sectie {code} vol")
    r = cand[0]
    used.add(r)
    tpl = a  # rij met complete formules als opmaakvoorbeeld
    ws.cell(row=r, column=3).value = desc                       # C omschrijving
    ws.cell(row=r, column=4).value = "post"                     # D eenheid
    ws.cell(row=r, column=5).value = f"=K{r}"                   # E aantal
    ws.cell(row=r, column=6).value = f"=CEILING(L{r}*$M$7,$M$8)"  # F €/unit
    ws.cell(row=r, column=7).value = f"=ROUND(E{r}*F{r},0)"     # G totaal
    ws.cell(row=r, column=9).value = party                      # I partij
    ws.cell(row=r, column=11).value = qty                       # K aantal
    ws.cell(row=r, column=12).value = price                     # L €/eenh
    ws.cell(row=r, column=13).value = f"=K{r}*L{r}"             # M totaal netto
    ws.cell(row=r, column=15).value = note                      # O opmerking
    if ws.cell(row=r, column=2).value in (None, ""):
        prev = ws.cell(row=r - 1, column=2).value
        ws.cell(row=r, column=2).value = (prev + 1) if isinstance(prev, int) else 1
    # opmaak kopiëren van eerste rij van de sectie
    for col in (2,3,4,5,6,7,9,11,12,13,15):
        src_c = ws.cell(row=tpl, column=col); dst = ws.cell(row=r, column=col)
        dst.font = copy(src_c.font); dst.border = copy(src_c.border)
        dst.fill = copy(src_c.fill); dst.number_format = src_c.number_format
        dst.alignment = copy(src_c.alignment)
    return r

L = add_line
# --- SPIE Building Solutions (opdrachten 2500211, 2500429, 2600008) ---
L("230", "Elektrische installatie (post 0018)", "SPIE", 26603.03, "Opdracht 2500211 / offerte 19633 | 25002 Kioti Build")
L("230", "Meerwerk gebundeld: extra WCD's, armaturen e.d.", "SPIE", 6727.19, "Opdracht 2500429 | offertebrief 17-10-2025")
L("240", "Video- en intercominstallatie met deursturing (post 0019)", "SPIE", 4007.41, "Opdracht 2500211")
L("240", "Ring deurbel + UPD, leveren en monteren", "SPIE", 1226.21, "Opdracht 2600008 | offertebrief 43997")
L("260", "Brandmeld- en ontruimingsinstallatie (post 0021)", "SPIE", 14930.90, "Opdracht 2500211")
# --- 4Some Technisch Beheer (opdrachten 2500210, 2600012) ---
L("210", "Aanpassingen ventilatie", "4Some", 32841.00, "Opdracht 2500210 / offerte 10000/429805")
L("210", "Aanpassingen klimaatplafond (raming)", "4Some", 9500.00, "Opdracht 2500210")
L("210", "Aanpassingen GBS (raming)", "4Some", 17000.00, "Opdracht 2500210")
L("210", "CV- en GKW-aanpassingen", "4Some", 2820.00, "Opdracht 2500210")
L("220", "VWA en tapwater pantry", "4Some", 4454.00, "Opdracht 2500210")
L("220", "Leveren en plaatsen Quooker Cube (gekoeld water)", "4Some", 2270.00, "Opdracht 2600012")
# --- Technoproject (opdrachten 2500212, 2500430 + offerte meerwerk 1250355) ---
L("322", "Systeemwanden (post 2.0)", "Technoproject", 36000.00, "Opdracht 2500212 / offerte 1250270")
L("322", "Glazen panelenwand, flexibel 45 dB (post 4.0)", "Technoproject", 26460.00, "Opdracht 2500212")
L("322", "Algemene kosten en eenmalige relatiekorting (post 5.0)", "Technoproject", 7080.00, "Opdracht 2500212")
L("322", "Meerwerk: koven/sonorex plafond, melamine toeslagen, vlakverdeling, afvoer (incl. verrekening vloerschade -3.000)", "Technoproject", 18347.00, "OFFERTE 1250355 versie A d.d. 6-10-2025 — nog geen opdracht gezien")
L("323", "Deuren, glazen (stomp)/kozijnen (post 3.0)", "Technoproject", 9960.00, "Opdracht 2500212")
L("323", "Cilinderslot deur CEO office, incl. 3 sleutels", "Technoproject", 290.00, "Opdracht 2500430 / offerte 1250539")
# --- Techno Telematica (opdrachten 2500214, 2500323, 2500359, 2500428) ---
L("250", "Data netwerk U/FTP Cat6a (post 1.7)", "Techno Telematica", 13995.00, "Opdracht 2500214")
L("250", "Netwerk additionele voorzieningen (post 1.8)", "Techno Telematica", 5900.00, "Opdracht 2500214")
L("430", "Legborden + AV-installatie MER/SER", "Techno Telematica", 13025.00, "Opdracht 2500323 (610 + 10.000 + 2.415)")
L("430", "AV levering + montage (extra scherm en Poly)", "Techno Telematica", 7080.00, "Opdracht 2500359")
L("430", "Additioneel AV + vergaderapparatuur, incl. verplaatsen bestaand", "Techno Telematica", 15405.00, "Opdracht 2500428")
# --- 4all Solutions ---
L("250", "UTP patchkabels t.b.v. bureaus, levering + montage", "4all Solutions", 1600.00, "Opdracht 2500360 / offerte cable data kabels werkplek")
# --- Bureau VanDerVorm (opdrachten 2500227, 2500282, 2500322, 2500361, 2600011 + offerte CEO office) ---
L("410", "Kantoormeubilair (werkplekken, stoelen, tafels)", "BVDV", 46777.85, "Opdracht 2500227 / offerte 202500218")
L("410", "Additioneel meubilair home office (zit-sta bureau)", "BVDV", 713.55, "Opdracht 2500282 / offerte 202500134")
L("410", "Huurmeubilair: plaatsen en ophalen verstelbaar bureau", "BVDV", 325.00, "Opdracht 2500322 / 202500186")
L("410", "Vergadertafel incl. installatie elektra in blad", "BVDV", 1379.99, "Opdracht 2500361")
L("410", "Bisley Essentials ladeblokken (2 st.) incl. levering/montage", "BVDV", 892.36, "Opdracht 2600011 / offerte 202500301B Kast Kioti")
L("410", "CEO office: zit-sta werkplek + kabelmanagement", "BVDV", 2225.01, "OFFERTE 202500273 d.d. 8-8-2025 — nog geen opdracht gezien")
L("420", "Phonebooths Framery One Compact (2 st.) incl. levering en montage", "BVDV", 18768.76, "Opdracht 2500277 / offerte 202500254")
# --- Hoogwerf Aannemersbedrijf ---
L("131", "Nalopen en herstellen diverse beschadigingen", "Hoogwerf", 614.81, "Opdracht 2500467")
# --- McArt ---
L("450", "Maatwerk bestickering op glaswerk", "McArt", 3299.49, "Opdracht 2600083 / offerte 45268")
# --- Kampschreur (factuur meerwerk) ---
L("314", "Podium stofferen (linoleum Decibel) + herstel vloer na beschadigingen derden", "Kampschreur", 7136.39, "Factuur 20251096 / PO 2500221 (meerwerk, 72,4 m2)")

# ---- 3. projectgegevens ----
bp = wb["2 | Basic principles"]
bp["C7"] = "Kioti Rotterdam WTC"
bp["C8"] = "Inkoopoverzicht leveranciers (offertes & opdrachten) | projectcode 25002 / 250098"
bp["C9"] = "Versie 001"
bp["F9"] = datetime.date(2026, 7, 5)
bp["C23"] = "12e verdieping, WTC Beursplein 37 Rotterdam"
bp["E23"] = 445
bp["C32"] = "Bron: OneDrive SJB/Kioti 2/2.3 Aanbesteding & opdrachten/Opdrachten"
bp["C33"] = "Geautoriseerd budget: Kioti Budget 30-05-2025 v3 (EUR 575.644 excl. btw)"

# ---- 4. Check quote amounts: leveranciersnamen ----
cq = wb["Check quote amounts"]
suppliers = ["SPIE", "4Some", "Technoproject", "Techno Telematica", "BVDV",
             "4all Solutions", "Hoogwerf", "McArt", "Kampschreur"]
for i, name in enumerate(suppliers):
    cq.cell(row=15 + i, column=2).value = name
for r in range(15 + len(suppliers), 40):
    cq.cell(row=r, column=2).value = "-"

wb.save(OUT)

# ---- 5. controle: netto som per leverancier ----
wb2 = openpyxl.load_workbook(OUT)
ws2 = wb2["4 | Calculation"]
tot = {}
for r in item_rows:
    k = ws2.cell(row=r, column=11).value or 0
    l = ws2.cell(row=r, column=12).value
    l = l if isinstance(l, (int, float)) else 0
    if k and l:
        p = ws2.cell(row=r, column=9).value
        tot[p] = tot.get(p, 0) + k * l
for p, v in sorted(tot.items()):
    print(f"{p:20s} {v:>12,.2f}")
print(f"{'TOTAAL netto':20s} {sum(tot.values()):>12,.2f}")
print("Opgeslagen:", OUT)
