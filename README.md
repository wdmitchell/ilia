# invalid-roa

This project, utilises a full routing bviews dump from RIPE to query the APNIC RPKI validator to find invalid routes.

To run the tool.

1) Download a full bviews data file from the RIPE Data BGP Archivies, we used http://data.ris.ripe.net/rrc00/2019.02/bview.20190209.0000.gz for our test.
2) unzip the file 
3) Utilising the MRT python BGP dump tool execute: 

python3 mrt2bgpdump.py ../bview.20190223.0800 | awk 'BEGIN{FS="|"} { print $6 " " $7}' | awk '{ print $1 " " $NF }' | sort -u > sorted-route-asn.txt

4) mkdir data1
5) cd data1
6) split -l 60 ../sorted-route-asn.txt #Note this will generate approximately 14500 files.
7) Run python3 retreiveroa.py

This will produce an output of validity_reason1.csv once it finds invalid routes.

In this code, the 50 files read and processing at the same time. If you want to change num of file, 
change the code in retrieveroa.py's pool Count

Also once the script has run, you can query the data with some simple awk commands to get a total number of invalid roa's per ASN

 cat validity_reason1.csv | awk '{ print $2 }' | awk 'BEGIN{FS=":"} { print $2 }' | awk 'BEGIN{FS=","} { print $1 }' | sort | uniq -c
 
      2 AS10753
      1 AS1221
      8 AS12302
    240 AS12552
      1 AS12735
      1 AS12969
      1 AS131155
      1 AS133585
      4 AS134419
      1 AS134766
      4 AS137693
     62 AS14080
     54 AS17552
      9 AS18001
      4 AS18259
      2 AS18678
      1 AS19120
      4 AS199419
      4 AS199455
      3 AS2
      2 AS20207
      2 AS202623
      6 AS202940
      1 AS204813
      1 AS209737
      1 AS22411
      2 AS262589
      1 AS263223
      1 AS263756
      1 AS263771
      1 AS264686
      1 AS265515
      2 AS265719
      4 AS265751
      1 AS265758
      1 AS265816
      1 AS27471
      1 AS27650
      4 AS27725
      8 AS27826
      4 AS27843
      2 AS27901
      2 AS27953
      2 AS28086
      1 AS32034
      1 AS3215
      1 AS3320
     46 AS3549
      9 AS37900
      4 AS38193
      2 AS38713
      1 AS394183
      1 AS394308
      6 AS394497
      1 AS4134
      2 AS42010
      4 AS42962
      2 AS44491
      8 AS45774
      2 AS46261
      2 AS46562
      2 AS47215
      1 AS49425
      1 AS49666
      3 AS50434
      1 AS51957
      1 AS52145
      1 AS52255
      3 AS52444
      3 AS53371
      3 AS55862
      3 AS56099
      1 AS57219
      1 AS58779
      1 AS60300
      1 AS60721
      1 AS62021
      1 AS62031
      2 AS62240
      1 AS62597
      1 AS64252
      1 AS65552
      1 AS7604
      5 AS8386
      1 AS9329
      1 AS9484
      1 AS9498
      1 AS9541

ROA count by prefix tool

This tool counts the number of IPv4 and IPv6 ROA entries by prefix.

To run the tool, simply run "python3 prefix.py"

 

