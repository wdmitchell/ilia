#!/usr/bin/env python3

import json
import requests
import pprint
import argparse
import concurrent.futures

poolCount = 10


def apnic():

    r = requests.get("http://data1.labs.apnic.net:8080/export.json")
    return r.json()
    #r = open("export.json","r")
    #data = json.load(r)
    #return data
    

def main():

    ipv624=0
    ipv625=0
    ipv626=0
    ipv627=0
    ipv628=0
    ipv629=0
    ipv630=0
    ipv631=0
    ipv632=0
    ipv633=0
    ipv634=0
    ipv635=0
    ipv636=0
    ipv637=0
    ipv638=0
    ipv639=0
    ipv640=0
    ipv641=0
    ipv642=0
    ipv643=0
    ipv644=0
    ipv645=0
    ipv646=0
    ipv647=0
    ipv648=0
    ipv649=0
    ipv650=0
    ipv651=0
    ipv652=0
    ipv653=0
    ipv654=0
    ipv655=0
    ipv656=0
    ipv657=0
    ipv658=0
    ipv659=0
    ipv660=0
    ipv661=0
    ipv662=0
    ipv663=0
    ipv664=0
    ipv665=0
    ipv6104=0
    ipv6128=0
    
    ipv41=0
    ipv42=0
    ipv43=0
    ipv44=0
    ipv45=0
    ipv46=0
    ipv47=0
    ipv48=0
    ipv49=0
    ipv410=0
    ipv411=0
    ipv412=0
    ipv413=0
    ipv414=0
    ipv415=0
    ipv416=0
    ipv417=0
    ipv418=0
    ipv419=0
    ipv420=0
    ipv421=0
    ipv422=0
    ipv423=0
    ipv424=0
    ipv425=0
    ipv426=0
    ipv427=0
    ipv428=0
    ipv429=0
    ipv430=0
    ipv431=0
    ipv432=0
    
    print("Querying APNIC LABS")
    data = apnic()
    for roas in data['roas']:
        #if "::" in roas['prefix']:
            if "::/24" in roas['prefix']:
                ipv624 +=1
            elif "::/25" in roas['prefix']:
                ipv625 +=1
            elif "::/26" in roas['prefix']:
                ipv626 +=1
            elif "::/27" in roas['prefix']:
                ipv627 +=1
            elif "::/28" in roas['prefix']:
                ipv628 +=1
            elif "::/29" in roas['prefix']:
                ipv629 +=1
            elif "::/30" in roas['prefix']:
                ipv630 +=1
            elif "::/30" in roas['prefix']:
                ipv630 +=1
            elif "::/31" in roas['prefix']:
                ipv631 +=1
            elif "::/32" in roas['prefix']:
                ipv632 +=1
            elif "::/33" in roas['prefix']:
                ipv633 +=1
            elif "::/34" in roas['prefix']:
                ipv634 +=1
            elif "::/35" in roas['prefix']:
                ipv635 +=1
            elif "::/36" in roas['prefix']:
                ipv636 +=1
            elif "::/37" in roas['prefix']:
                ipv637 +=1
            elif "::/38" in roas['prefix']:
                ipv638 +=1
            elif "::/39" in roas['prefix']:
                ipv639 +=1
            elif "::/40" in roas['prefix']:
                ipv640 +=1
            elif "::/41" in roas['prefix']:
                ipv641 +=1
            elif "::/42" in roas['prefix']:
                ipv642 +=1
            elif "::/43" in roas['prefix']:
                ipv643 +=1
            elif "::/44" in roas['prefix']:
                ipv644 +=1
            elif "::/45" in roas['prefix']:
                ipv645 +=1
            elif "::/46" in roas['prefix']:
                ipv646 +=1
            elif "::/47" in roas['prefix']:
                ipv647 +=1
            elif "::/48" in roas['prefix']:
                ipv648 +=1
            elif "::/49" in roas['prefix']:
                ipv649 +=1
            elif "::/50" in roas['prefix']:
                ipv650 +=1
            elif "::/51" in roas['prefix']:
                ipv651 +=1
            elif "::/52" in roas['prefix']:
                ipv652 +=1
            elif "::/53" in roas['prefix']:
                ipv653 +=1
            elif "::/54" in roas['prefix']:
                ipv654 +=1
            elif "::/55" in roas['prefix']:
                ipv655 +=1
            elif "::/56" in roas['prefix']:
                ipv656 +=1
            elif "::/57" in roas['prefix']:
                ipv657 +=1
            elif "::/58" in roas['prefix']:
                ipv658 +=1
            elif "::/59" in roas['prefix']:
                ipv659 +=1
            elif "::/60" in roas['prefix']:
                ipv660 +=1
            elif "::/61" in roas['prefix']:
                ipv661 +=1
            elif "::/62" in roas['prefix']:
                ipv662 +=1
            elif "::/63" in roas['prefix']:
                ipv663 +=1
            elif "::/64" in roas['prefix']:
                ipv664 +=1
            elif "::/65" in roas['prefix']:
                ipv665 +=1
            elif "::/104" in roas['prefix']:
                ipv6104 +=1
            elif "::/128" in roas['prefix']:
                ipv6128 +=1
        #elif "::" not in roas['prefix']:
            elif "/20" in roas['prefix']:
                ipv420 +=1
            elif "/21" in roas['prefix']:
                ipv421 +=1
            elif "/22" in roas['prefix']:
                ipv422 +=1
            elif "/23" in roas['prefix']:
                ipv423 +=1
            elif "/24" in roas['prefix']:
                ipv424 +=1
            elif "/25" in roas['prefix']:
                ipv425 +=1
            elif "/26" in roas['prefix']:
                ipv426 +=1
            elif "/27" in roas['prefix']:
                ipv427 +=1
            elif "/28" in roas['prefix']:
                ipv428 +=1
            elif "/29" in roas['prefix']:
                ipv429 +=1
            elif "/10" in roas['prefix']:
                ipv410 +=1
            elif "/11" in roas['prefix']:
                ipv411 +=1
            elif "/12" in roas['prefix']:
                ipv412 +=1
            elif "/13" in roas['prefix']:
                ipv413 +=1
            elif "/14" in roas['prefix']:
                ipv414 +=1
            elif "/15" in roas['prefix']:
                ipv415 +=1
            elif "/16" in roas['prefix']:
                ipv416 +=1
            elif "/17" in roas['prefix']:
                ipv417 +=1
            elif "/18" in roas['prefix']:
                ipv418 +=1
            elif "/19" in roas['prefix']:
                ipv419 +=1
            elif "/30" in roas['prefix']:
                ipv430 +=1
            elif "/31" in roas['prefix']:
                ipv431 +=1
            elif "/32" in roas['prefix']:
                ipv432 +=1
            elif "/1" in roas['prefix']:
                ipv41 +=1  
            elif ("/2" in roas['prefix']):
                print(roas['prefix'])
                ipv42 +=1
            elif "/3" in roas['prefix']:
                ipv43 +=1
            elif "/4" in roas['prefix']:
                ipv44 +=1
            elif "/5" in roas['prefix']:
                ipv45 +=1
            elif "/6" in roas['prefix']:
                ipv46 +=1
            elif "/7" in roas['prefix']:
                ipv47 +=1
            elif "/8" in roas['prefix']:
                ipv48 +=1
            elif "/9" in roas['prefix']:
                ipv49 +=1


    print("---")
    print("IPv4 /1 Routes: ", ipv41)
    print("IPv4 /2 Routes: ", ipv42)
    print("IPv4 /3 Routes: ", ipv43)
    print("IPv4 /4 Routes: ", ipv44)
    print("IPv4 /5 Routes: ", ipv45)
    print("IPv4 /6 Routes: ", ipv46)
    print("IPv4 /7 Routes: ", ipv47)
    print("IPv4 /8 Routes: ", ipv48)
    print("IPv4 /9 Routes: ", ipv49)
    print("IPv4 /10 Routes: ", ipv410)
    print("IPv4 /11 Routes: ", ipv411)
    print("IPv4 /12 Routes: ", ipv412)
    print("IPv4 /13 Routes: ", ipv413)
    print("IPv4 /14 Routes: ", ipv414)
    print("IPv4 /15 Routes: ", ipv415)
    print("IPv4 /16 Routes: ", ipv416)
    print("IPv4 /17 Routes: ", ipv417)
    print("IPv4 /18 Routes: ", ipv418)
    print("IPv4 /19 Routes: ", ipv419)
    print("IPv4 /20 Routes: ", ipv420)
    print("IPv4 /21 Routes: ", ipv421)
    print("IPv4 /22 Routes: ", ipv422)
    print("IPv4 /23 Routes: ", ipv423)
    print("IPv4 /24 Routes: ", ipv424)
    print("IPv4 /25 Routes: ", ipv425)
    print("IPv4 /26 Routes: ", ipv426)
    print("IPv4 /27 Routes: ", ipv427)
    print("IPv4 /28 Routes: ", ipv428)
    print("IPv4 /29 Routes: ", ipv429)
    print("IPv4 /30 Routes: ", ipv430)
    print("IPv4 /31 Routes: ", ipv431)
    print("IPv4 /32 Routes: ", ipv432)

    totalipv4 = ipv41+ipv42+ipv43+ipv44+ipv45+ipv46+ipv47+ipv48+ipv49+ipv410+ipv411+ipv412+ipv413+ipv414+ipv415+ipv416+ipv417+ipv418+ipv419+ipv420+ipv421+ipv422+ipv423+ipv424+ipv425+ipv426+ipv427+ipv428+ipv429+ipv430+ipv431+ipv432

    print("Total IPv4 Routes: ", totalipv4)

    print("---")
    print("IPv6 /24 Routes: ", ipv624)
    print("IPv6 /25 Routes: ", ipv625)
    print("IPv6 /26 Routes: ", ipv626)
    print("IPv6 /27 Routes: ", ipv627)
    print("IPv6 /28 Routes: ", ipv628)
    print("IPv6 /29 Routes: ", ipv629)
    print("IPv6 /30 Routes: ", ipv630)
    print("IPv6 /31 Routes: ", ipv631)
    print("IPv6 /32 Routes: ", ipv632)
    print("IPv6 /33 Routes: ", ipv633)
    print("IPv6 /34 Routes: ", ipv634)
    print("IPv6 /35 Routes: ", ipv635)
    print("IPv6 /36 Routes: ", ipv636)
    print("IPv6 /37 Routes: ", ipv637)
    print("IPv6 /38 Routes: ", ipv638)
    print("IPv6 /39 Routes: ", ipv639)
    print("IPv6 /40 Routes: ", ipv640)
    print("IPv6 /41 Routes: ", ipv641)
    print("IPv6 /42 Routes: ", ipv642)
    print("IPv6 /43 Routes: ", ipv643)
    print("IPv6 /44 Routes: ", ipv644)
    print("IPv6 /45 Routes: ", ipv645)
    print("IPv6 /46 Routes: ", ipv646)
    print("IPv6 /47 Routes: ", ipv647)
    print("IPv6 /48 Routes: ", ipv648)
    print("IPv6 /49 Routes: ", ipv649)
    print("IPv6 /50 Routes: ", ipv650)
    print("IPv6 /51 Routes: ", ipv651)
    print("IPv6 /52 Routes: ", ipv652)
    print("IPv6 /53 Routes: ", ipv653)
    print("IPv6 /54 Routes: ", ipv654)
    print("IPv6 /55 Routes: ", ipv655)
    print("IPv6 /56 Routes: ", ipv656)
    print("IPv6 /57 Routes: ", ipv657)
    print("IPv6 /58 Routes: ", ipv658)
    print("IPv6 /59 Routes: ", ipv659)
    print("IPv6 /60 Routes: ", ipv660)
    print("IPv6 /61 Routes: ", ipv661)
    print("IPv6 /62 Routes: ", ipv662)
    print("IPv6 /63 Routes: ", ipv663)
    print("IPv6 /64 Routes: ", ipv664)
    print("IPv6 /65 Routes: ", ipv665)
    print("IPv6 /104 Routes: ", ipv6104)
    print("IPv6 /128 Routes: ", ipv6128)


    totalipv6 = ipv624+ipv625+ipv626+ipv627+ipv628+ipv629+ipv630+ipv631+ipv632+ipv633+ipv634+ipv635+ipv636+ipv637+ipv638+ipv639+ipv640+ipv641+ipv642+ipv643+ipv644+ipv645+ipv646+ipv647+ipv648+ipv649+ipv650+ipv651+ipv652+ipv653+ipv654+ipv655+ipv656+ipv657+ipv658+ipv659+ipv660+ipv661+ipv662+ipv663+ipv664+ipv665+ipv6104+ipv6128

    print("Total IPv6 Routes: ", totalipv6)


if __name__  == "__main__":
    main()
