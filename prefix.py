#!/usr/bin/env python3

import json
import requests


def apnic():

    r = requests.get("http://data1.labs.apnic.net:8080/export.json")
    return r.json()
    
def main():
    
    print("Querying APNIC LABS for ROA's")
    data = apnic()
    ipv6 = dict()
    ipv4 = dict()
    totalipv6 = 0
    totalipv4 = 0
    for roas in data['roas']:
        if ":" in roas['prefix']:
            prefixes,mask = roas['prefix'].split("/")
            if mask in ipv6 :
                ipv6[mask] = ipv6[mask] + 1
            else:
                ipv6[mask] = 1
        elif ":" not in roas['prefix']:
            ipv4prefixes,ipv4mask = roas['prefix'].split("/")
            if ipv4mask in ipv4 :
                ipv4[ipv4mask] = ipv4[ipv4mask] + 1
            else:
                ipv4[ipv4mask] = 1
    
    print("IPv4 CIDR Count's")
    print()

    numeric = dict(sorted(ipv4.items(), key=lambda x: int(x[0])))
    for k,v in numeric.items():
        print('/'+k,v)
        totalipv4 = totalipv4 + v
    print()
    print("Total IPv4 ROA's", totalipv4)

    print()
    print("IPv6 CIDR Count's")
    print()

    numeric = dict(sorted(ipv6.items(), key=lambda x: int(x[0])))

    for k,v in numeric.items():
        print('/'+k,v)
        totalipv6 = totalipv6 + v
    print()
    print("Total IPv6 ROA's", totalipv6)


if __name__  == "__main__":
    main()

