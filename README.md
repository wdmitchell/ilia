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

ROA count by prefix tool

This tool counts the number of IPv4 and IPv6 ROA entries by prefix.

To run the tool, simply run "python3 prefix.py"

The output will look like:

ubuntu@172-31-1-149:~/invalid-roa$ python3 prefix.py
Querying APNIC LABS
---
IPv4 /1 Routes:  0
IPv4 /2 Routes:  0
IPv4 /3 Routes:  0
IPv4 /4 Routes:  0
IPv4 /5 Routes:  0
IPv4 /6 Routes:  0
IPv4 /7 Routes:  0
IPv4 /8 Routes:  1
IPv4 /9 Routes:  1
IPv4 /10 Routes:  13
IPv4 /11 Routes:  25
IPv4 /12 Routes:  101
IPv4 /13 Routes:  127
IPv4 /14 Routes:  300
IPv4 /15 Routes:  422
IPv4 /16 Routes:  1829
IPv4 /17 Routes:  1124
IPv4 /18 Routes:  1423
IPv4 /19 Routes:  2941
IPv4 /20 Routes:  3467
IPv4 /21 Routes:  3903
IPv4 /22 Routes:  8709
IPv4 /23 Routes:  5843
IPv4 /24 Routes:  33796
IPv4 /25 Routes:  62
IPv4 /26 Routes:  61
IPv4 /27 Routes:  32
IPv4 /28 Routes:  33
IPv4 /29 Routes:  94
IPv4 /30 Routes:  22
IPv4 /31 Routes:  2
IPv4 /32 Routes:  234
Total IPv4 Routes:  64565
---
IPv6 /24 Routes:  7
IPv6 /25 Routes:  2
IPv6 /26 Routes:  13
IPv6 /27 Routes:  10
IPv6 /28 Routes:  29
IPv6 /29 Routes:  985
IPv6 /30 Routes:  83
IPv6 /31 Routes:  39
IPv6 /32 Routes:  2829
IPv6 /33 Routes:  65
IPv6 /34 Routes:  41
IPv6 /35 Routes:  56
IPv6 /36 Routes:  379
IPv6 /37 Routes:  77
IPv6 /38 Routes:  249
IPv6 /39 Routes:  274
IPv6 /40 Routes:  924
IPv6 /41 Routes:  25
IPv6 /42 Routes:  55
IPv6 /43 Routes:  61
IPv6 /44 Routes:  386
IPv6 /45 Routes:  75
IPv6 /46 Routes:  463
IPv6 /47 Routes:  138
IPv6 /48 Routes:  3819
IPv6 /49 Routes:  9
IPv6 /50 Routes:  6
IPv6 /51 Routes:  5
IPv6 /52 Routes:  9
IPv6 /53 Routes:  4
IPv6 /54 Routes:  4
IPv6 /55 Routes:  3
IPv6 /56 Routes:  15
IPv6 /57 Routes:  7
IPv6 /58 Routes:  5
IPv6 /59 Routes:  6
IPv6 /60 Routes:  9
IPv6 /61 Routes:  6
IPv6 /62 Routes:  10
IPv6 /63 Routes:  14
IPv6 /64 Routes:  247
IPv6 /65 Routes:  1
IPv6 /104 Routes:  1
IPv6 /128 Routes:  1
Total IPv6 Routes:  11446 

