"""Manual S61 third-root transcription; checks do not validate its calendar."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SHA='daa3895a61dc5fa0bdb4dc6e3b3ccb07e76e9873f523ed24cdd40a4bd1349740'
pdf=ROOT/'tmp/research/9756.pdf'
if pdf.exists():
    assert hashlib.sha256(pdf.read_bytes()).hexdigest()==SHA
# Visually read PDF4, printed killed-cedar Page2. Rows start at printed years.
TEXT='''1370 320 248 578 605 700 461 891 468 496 438
1380 424 536 575 660 704 599 317 261 298 298
1390 393 194 156 145 105 140 153 174 206 187
1400 240 170 182 390 342 485 540 489 598 688
1410 622 502 513 694 622 658 522 472 436 406
1420 404 287 300 367 263 194 459 569 710 506
1430 836 830 1018 1175 1380 1608 1761 1404 1861 2014
1440 1595 1475 1462 1518 1912 1852 1191 792 811 881
1450 1010 1170 1449 1565 1266 920 860 1021 1010 1256
1460 1717 1403 1309 1309 1005 898 572 507 526 484
1470 602 524 626 444 673 812 699 721 686 766
1480 1098 992 1073 1041 875 541 614 621 684 550
1490 686 813 782 524 760 734 701 1110 951 731
1500 1063 865 722 695 674 924 785 1059 1345 1257
1510 1275 1139 959 1002 1268 1523 1250 1289 936 557
1520 636 1011 1132 953 1412 1380 1494 1129 1652 2502
1530 2525 1727 1977 2545 2766 1675 1837 2682 2576 2776
1540 1641 5126 3604 2776 3249 3049 1956 2509 1546 1295
1550 1903 1663 1938 1997 1447 2393 2800 2545 1954 1799
1560 2955 2727 2712 2029 1664 965 942 1716 1430 2512
1570 4011 1930 1876 2470 2559 2850 2786 2269 1661 1599
1580 1958 1462 1319 1888 2310 1874 1875 2294 2942 2824
1590 2473 2022 1852 1657 1243 1540 1436 1000 2730 2516
1600 3606 3379 3125 1986 1706 1376 1561 1791 1916 1930
1610 1545 1971 2288 1471 682 973 972 1199 959 756
1620 784 1086 1146 833 827 814 910 1026 1486 1505
1630 1522 1727 1521 1369 1121 643 509 612 752 645
1640 555 565 557 515 368 586 604 594 757 434
1650 270 340 475 552 716 909 1003 1221 780 613
1660 555 500 506 489 364 378 434 465 479 491
1670 612 402 527 507 598 508 519 541 600 583
1680 399 292 529 439 581 490 797 809 789 565
1690 586 463 351 490 394 610 532 453 455 293
1700 -9999'''
rows=[]; widths=[]
for line in TEXT.splitlines():
    v=list(map(int,line.split())); year,values=v[0],v[1:]
    rows.append(dict(year=year,values=values))
    if year==1700:
        assert values==[-9999]
        continue
    assert len(values)==10 and min(values)>0
    assert year==1370+len(widths)
    widths.extend(values)
assert len(widths)==330
oldpath=ROOT/'data/cascadia-width-extract.json'
old=json.loads(oldpath.read_text())
terminal=next(s for s in old['series'] if s['id']=='GF2RTA')
assert terminal['start_year']==1690 and terminal['widths']==widths[-10:]
out=dict(status='COMPLETE_MANUAL_TRANSCRIPTION_NOT_INDEPENDENT_REVIEW',
    source_id='S61',original_pdf_sha256=SHA,pdf_page=4,printed_page='killed cedar rings widths Page2',
    id='GF2RTA',start_year=1370,end_year=1699,unit='micrometre',
    rows=rows,widths=widths,terminal_marker=-9999,
    previous_terminal_ledger_sha256=hashlib.sha256(oldpath.read_bytes()).hexdigest(),
    checks='33 ten-value rows;330 positive widths;1700 terminator excluded;1690–1699 exactly agrees with earlier terminal transcription.1541 width5126 retained as printed.',
    limits='Manual reading may contain errors; no independent transcription review or physical sample inspection. Published calendar inherited; no detrending, AR modeling or new date.')
(ROOT/'data/cascadia-third-root.json').write_text(json.dumps(out,indent=2)+'\n')
print('GF2RTA:',len(widths),'widths,1370–1699; terminal decade matches prior record')
