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

in this code, the 50 files read and processing at the same time. If you want to change num of file, 
change the code in retrieveroa.py's pool Count

