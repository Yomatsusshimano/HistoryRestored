"""Compare scan-transcribed S61 trunk widths with archived NOAA S229 records."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_SHA256 = 'daa3895a61dc5fa0bdb4dc6e3b3ccb07e76e9873f523ed24cdd40a4bd1349740'
original_pdf = ROOT / 'tmp/research/9756.pdf'
if original_pdf.exists():
    assert hashlib.sha256(original_pdf.read_bytes()).hexdigest() == ORIGINAL_SHA256
# Manually read from S61 PDF pages 4-5 (printed killed-cedar pages 2-3).
# Positive integers are micrometres; -9999 terminators are not widths.
ROWS = {
    'GF2TRB': '''1515 1167 1266 1404 1371 1177
1520 1325 1095 977 909 1309 1513 1229 1409 1295 1236
1530 1473 1220 1057 1239 1187 931 1145 1416 1436 1729
1540 881 1263 1280 1909 2128 1628 1262 1520 1041 1039
1550 1008 931 1362 1114 980 982 1050 1000 994 1006
1560 1395 1600 1305 1517 1395 1119 930 1181 1330 1399
1570 1682 1291 1041 1270 1623 1861 1996 2078 1885 1923
1580 1547 1411 1101 977 885 703 827 1004 1025 1302
1590 1288 1184 1083 1180 768 1126 1081 618 1061 862
1600 889 819 791 767 785 551 615 560 689 575
1610 585 568 514 448 234 266 316 347 263 259
1620 -9999''',
    'GF2TRA': '''1482 1455 1748 1466 1203 1015 1035 1036 538
1490 807 888 1227 1024 1420 1099 1169 1565 1445 1276
1500 1736 1048 1333 1207 1552 1580 1318 1444 1247 1734
1510 1562 1770 1872 1500 1891 1575 1340 1407 1232 579
1520 745 902 949 598 979 1268 1099 1002 1027 978
1530 938 694 709 773 719 757 812 791 1055 1188
1540 558 1163 1081 1333 1655 1298 1046 1386 651 807
1550 1087 1113 1371 1019 949 948 935 915 860 847
1560 1185 1486 1218 1380 1242 951 796 1157 1195 1194
1570 1316 1103 752 1122 1513 1862 1848 1944 1805 1947
1580 1478 1430 1109 1070 916 721 875 1085 1084 1291
1590 1440 1354 1253 1473 1011 1533 1455 880 1302 1182
1600 1074 1109 1151 1033 1018 820 779 824 897 819
1610 843 867 697 664 391 406 462 503 409 401
1620 338 335 255 220 244 303 261 330 380 363
1630 453 535 437 386 229 212 220 225 236 210
1640 207 199 223 244 167 246 167 194 143 -9999''',
    'GF2TRNW': '''1419 2190
1420 2453 2114 1985 2039 1910 1572 1916 1948 1961 1972
1430 1944 1794 1871 2098 2207 2092 2423 1993 2327 2203
1440 1818 2153 2312 2281 2395 2439 2146 1958 1827 1925
1450 1946 1924 2118 2070 1722 1501 1682 1506 1551 1944
1460 1501 1431 1621 1651 1569 1602 1086 1050 1028 1187
1470 1654 1927 1999 2213 2072 1631 1689 1461 1149 1133
1480 1411 1376 1502 1658 1647 1142 1102 1136 1228 878
1490 1092 1096 1557 1250 1501 1412 1423 1746 1605 1406
1500 1927 1456 1435 1315 1697 1447 1647 1869 1702 1771
1510 1960 2031 1865 1440 2086 1475 1416 1235 1086 773
1520 985 1277 1037 955 1346 1557 1257 1407 1628 1362
1530 1576 1244 1479 1554 1484 944 1320 1503 1625 2111
1540 1348 2167 1589 2114 2563 2018 1385 2082 946 1462
1550 1584 1561 1621 1554 1092 1014 1474 1600 1500 1421
1560 2231 2147 1929 1981 1764 1016 873 1404 1271 1275
1570 1580 923 1044 1423 1685 2032 1881 2338 2274 2165
1580 2106 2290 2027 1992 1214 1541 1863 1756 1800 2084
1590 1967 1574 1367 1363 980 1334 1204 1125 1816 1515
1600 1764 2021 1596 1718 1723 1721 2057 2328 2309 2088
1610 2084 1953 1872 1345 1191 1472 1503 1899 1795 1467
1620 1792 1824 1835 1636 1668 1691 1708 2089 2321 2102
1630 1675 2095 2294 1569 1559 1626 1330 1833 1962 1480
1640 1683 1739 1819 1677 1819 2062 2022 1830 1557 645
1650 716 1210 1258 1201 1308 1399 1421 1662 1269 1597
1660 1622 1361 1807 1381 1215 1419 1593 1712 1671 1744
1670 1765 1404 1549 1581 1268 1252 -9999'''
}

ledger = json.loads((ROOT / 'data/cascadia-raw-acquisition.json').read_text())
item = next(i for i in ledger['files'] if i['file'].endswith('wa130.rwl'))
raw = (ROOT / item['file']).read_bytes()
assert hashlib.sha256(raw).hexdigest() == item['sha256']
noaa = {}
for line in raw.decode().splitlines()[3:]:
    row = line.split()
    if not row or not row[0].startswith('CPGF2'):
        continue
    record = noaa.setdefault(row[0], {})
    for offset, value in enumerate(map(int, row[2:])):
        if value in (999, -9999):
            continue
        year = int(row[1]) + offset
        assert value > 0 and year not in record
        record[year] = value

matches = []
for old, new in [('GF2TRA', 'CPGF2A'), ('GF2TRB', 'CPGF2B'), ('GF2TRNW', 'CPGF2NW')]:
    original, terminators = {}, []
    for line in ROWS[old].splitlines():
        parts = list(map(int, line.split()))
        for offset, value in enumerate(parts[1:]):
            year = parts[0] + offset
            if value == -9999:
                terminators.append(year)
            else:
                assert value > 0 and year not in original
                original[year] = value
    years = sorted(original)
    assert years == list(range(years[0], years[-1] + 1))
    assert terminators == [years[-1] + 1]
    differences = [{'year': y, 'S61': original.get(y), 'S229': noaa[new].get(y)}
                   for y in sorted(set(original) | set(noaa[new]))
                   if original.get(y) != noaa[new].get(y)]
    matches.append(dict(S61_id=old, S229_id=new, start_year=years[0],
                        end_year=years[-1], count=len(years),
                        same_year_coverage=set(original) == set(noaa[new]),
                        differences=differences, terminator_year=terminators[0],
                        widths_micrometres=[original[y] for y in years],
                        inspected_pdf_pages=[4, 5] if old == 'GF2TRA' else [4] if old == 'GF2TRB' else [5]))
out = dict(status='DOCUMENTARY_NUMERICAL_CROSSWALK_NOT_PHYSICAL_AUTHENTICATION',
           source_ids=['S61', 'S229', 'S231'],
           original_pdf_sha256=ORIGINAL_SHA256,
           noaa_file=item['file'], noaa_file_sha256=item['sha256'],
           transcription_method='Manual reading of rendered original PDF pages 4-5; full numerical comparison to NOAA. Same analyst, no independent transcription review.',
           transcription_corrections=[dict(series='GF2TRNW', year=y, initial_read=a, enlarged_scan_read=b)
                                      for y, a, b in [(1457,1656,1506),(1591,1547,1574),(1593,1353,1363),
                                                      (1640,1793,1683),(1641,1683,1739),(1645,2026,2062),(1671,1440,1404)]],
           units='micrometres in original; NOAA -9999 end-marker convention denotes .001 mm, numerically identical.',
           limits='Year labels inherited. Exact duplicate measurements establish dataset correspondence, not independent corroboration, physical custody, bark/anatomy or absolute chronology.',
           matches=matches)
(ROOT / 'data/cascadia-trunk-crosswalk.json').write_text(json.dumps(out, indent=2) + '\n')
for match in matches:
    print(match['S61_id'], match['S229_id'], match['count'], 'differences', match['differences'])
assert all(m['same_year_coverage'] and not m['differences'] for m in matches)
