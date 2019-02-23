#!/usr/bin/env python3

import json
import requests
import pprint
import argparse
import concurrent.futures
import os

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

def write_validity(route,validity):
    try:
        with open('validity_reason.csv','a') as f:
            format = route["origin_asn"]+","+route["prefix"]+","+validity["reason"]
            print(format)
            f.write(format)
    except FileNotFoundError:
        with open('validity_reason.csv','w') as f:
            format = route["origin_asn"]+","+route["prefix"]+","+validity["reason"]
            print(format)
            f.write(format)


'''def validating(data):
    #print(data)
    for roas in data['roas']:
        print(roas['asn'], roas['prefix'], roas['maxLength'])
        loadata =apnicvalidator(roas['asn'],roas['prefix'])
        data = loadata["validated_route"]
        route = data["route"]
        validity= data["validity"]
           # print("test:",validity)

            #print("origin_asn : ", route["origin_asn"], "prefix:",route["prefix"])
            #print("state:",validity["state"],"reason:",validity["description"])
        validity_reason = list()
        if validity["state"] == "Invalid":
            print("reason",validity["reason"])
            validity_reason.append(validity["reason"])

    print("write_clear")

'''

def list_all_file():
    split_files = list()
    for root,dirs,files in os.walk('data/'):
        split_files = files
    #print(split_files)
    return split_files


def is_validate(split_file):
    print(split_file)
    json_data = open("data/"+split_file,'r')

    need_check_data = json.load(json_data)
    validity_list = list()
    for roas in need_check_data['roas']:
        print(roas)
        loadata =apnicvalidator(roas['asn'],roas['prefix'])
        checked_data = loadata["validated_route"]
        route = checked_data["route"]
        validity = checked_data["validity"]
        validity_list.append({"route":route,"validity":validity})

    for split_data in validity_list:
        print("check:",split_data["route"])
        if split_data["validity"]["state"] == "Invalid":
                #if is not invalid
            print("Reason:", validity["reason"])
            return split_data, False

        return split_data, True #if is VALID



def main():
    print("Querying APNIC LABS")

    print("---")
    chunked_files = list_all_file()
#    for split_file in files:

    with concurrent.futures.ThreadPoolExecutor(max_workers=poolCount) as executor:
        for data,is_valid in executor.map(is_validate,chunked_files):
        #    for data,is_valid in executor.map(is_validate,need_check_data['roas']):
            if is_valid == False:
                print("reason",data["validity"]["reason"], "valid", is_valid)
                write_validity(data["route"],data["validity"])



       # print(format(roadata))


if __name__  == "__main__":
    main()
