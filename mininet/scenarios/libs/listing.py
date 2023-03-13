#!/usr/bin/env python

import requests

from time import sleep

from requests.auth import HTTPBasicAuth
from prettytable import PrettyTable

url = "http://sdn_opendaylight_max_"+str(1)+".sdn_sdn:8181/restconf/operational/network-topology:network-topology"
log_pass = HTTPBasicAuth( 'admin', 'admin')

xml = requests.get(url, auth=log_pass)

data = xml.json()

err = False

while err == False:
    if str(data).find('node') != -1:
        c=0
        while err == False:
            xml = requests.get(url, auth=log_pass)
            data = xml.json()
            th = ['host-id', "MAC", "IP"]
            data = data['network-topology']['topology' ][0][ 'node' ]
            table = PrettyTable(th)
            td_data = []
            e_tab =3
            s_tab = 0
            ct=1
            for node in data:
                s = str(node['node-id'])
                if s.startswith('host') == True:
                    td_data.append(node[ 'node-id'])
                    td_data.append(node[ 'host-tracker-service:addresses' ][0]['mac'])
                    td_data.append(node[ 'host-tracker-service:addresses' ][0]['ip'])
                    table.add_row(td_data[s_tab:e_tab])
                    s_tab += 3
                    e_tab += 3
            if td_data != []:
                print('[', c, ']', "TABLE OF AVAILABLE HOSTS")
                print(table)
                print("*** through 10s table will be updated")
                print('')
            else:
                err = True
                print("ERROR: no hosts in your topology")
        if err == False:
            sleep(10)
    else:
        err = True
        print('ERROR: mininet is not running now')