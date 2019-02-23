#!/usr/bin/env python3

import json
import requests
import pprint
import argparse
import concurrent.futures

poolCount = 10


def apnic():

    #r = requests.get("http://data1.labs.apnic.net:8080/export.json")
    #return r.json()
    r = open("export.json","r")
    data = json.load(r)
    return data
    

def apnicvalidator(asn, prefix):
    r = requests.get("http://data1.labs.apnic.net:8080/api/v1/validity/{0}/{1}".format(asn,prefix))
    return r.json()
   
def write_validity(reason_list):
    with open('validity_reason.txt','w') as f:
        for reason in reason_list:
            f.write(reason+"\n")
    
def main():
    print("Querying APNIC LABS")
    data = apnic()
    print("---")
       # for validity in roadata['validated_route']:
        #    print(int(validity['route']))

       # print(format(roadata))
    for roas in data['roas']:
        print(roas['asn'], roas['prefix'], roas['maxLength'])
        roadata =apnicvalidator(roas['asn'],roas['prefix'])
        data = roadata["validated_route"]
        route = data["route"]
        validity= data["validity"]
       # print("test:",validity)

        #print("origin_asn : ", route["origin_asn"], "prefix:",route["prefix"])
        #print("state:",validity["state"],"reason:",validity["description"])
        validity_reason = list()
        if validity["state"] == "Invalid":
            print("reason",validity["reason"])
            validity_reason.append(validity["reason"])
    write_validity(validity_reason)
    print("write_clear")

if __name__  == "__main__":
    main()