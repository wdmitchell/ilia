#!/usr/bin/env python3

import json
import requests
import pprint
import argparse
import concurrent.futures
import os

poolCount = 50


def apnic():

    #r = requests.get("http://data1.labs.apnic.net:8080/export.json")
    #return r.json()
    r = open("export.json","r")
    data = json.load(r)
    return data



def apnicvalidator(asn, prefix):
    r = requests.get("http://data1.labs.apnic.net:8080/api/v1/validity/{0}/{1}".format(asn,prefix))
    return r.json()

def write_validity(validity_list):
    for validity in validity_list:
        try:
            print(validity_list)
            with open('validity_reason1.csv','a') as f:
                format ="{AS Number:"+ validity["route"]["origin_asn"]+", Prefix:"+validity["route"]["prefix"]+", Invalid Reason:"+validity["validity"]["reason"]+"}\r\n"
                print(format)
                f.write(format)
        except FileNotFoundError:
            with open('validity_reason1.csv','w') as f:
                format ="{AS Number:"+ validity["route"]["origin_asn"]+", Prefix:"+validity["route"]["prefix"]+", Invalid Reason:"+validity["validity"]["reason"]+"}\r\n"
                print(format)
                f.write(format)


def list_all_file():
    split_files = list()
    for root,dirs,files in os.walk('data1/'):
        split_files = files
    #print(split_files)
    return split_files

def read_data(file):
    ip_list = list()
    print(file)
    with open("data1/"+file,"r") as f:
        while True:
            line = f.readline()
            if not line: break
            line = line.replace('\n','')
            split_data = line.split(' ')

            ip_list.append({"ip":split_data[0],"as_num":split_data[1]})
    return ip_list

def is_validate(split_file):

    ip_list = read_data(split_file)
    invalidity_list = list()
    count = 0
    load_data = ''
    try:
        for ip in ip_list:

            loadata =apnicvalidator("AS"+ip['as_num'],ip['ip'])
            checked_data = loadata["validated_route"]
            route = checked_data["route"]
            validity = checked_data["validity"]
            if validity["state"] == "Valid":
                print("valid")
            elif validity["state"] == "Invalid":
                    #if is not invalid
                invalidity_list.append(checked_data)
                print("Reason:", validity["reason"])
            else:
                print("not Found")
        print(count)
    except:
        print(load_data)

    return invalidity_list #if is VALID



def main():
    print("Querying APNIC LABS")

    print("---")
    chunked_files = list_all_file()
    print(chunked_files)
    count =0
    with concurrent.futures.ThreadPoolExecutor(max_workers=poolCount) as executor:
        for validity_list in executor.map(is_validate,chunked_files):
            count+=50
            print("count"+str(count))
        #    for data,is_valid in executor.map(is_validate,need_check_data['roas']):
            write_validity(validity_list)



       # print(format(roadata))


if __name__  == "__main__":
    main()
