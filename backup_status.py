
"""This script is for checking backup status for UpCloud servers"""

from requests.auth import HTTPBasicAuth
from collections import defaultdict
from socket import gethostname
import json
import requests

#Get list of servers
srvlist=requests.get('https://api.upcloud.com/1.2/server', auth=HTTPBasicAuth('user', 'pass'))
srvlist_json = srvlist.json()
data = srvlist.json()
print(data)

#Store server hostname and uuid in dictionary
hosts = {}
for d in data['servers']['server']:
    srvhostname = d['title']
    srvuuid = d['uuid']
    hosts[srvhostname] = srvuuid
    print(hosts)


#Get server hostname and find uuid dedicated to specific hostname
hostname = gethostname()
print(hostname)
for srvhostname in hosts:
  if srvhostname != hostname:
    continue
  if srvhostname == hostname:
    print(srvhostname + " : " + hosts[srvhostname])
    break
else:
  print("There is no matching hostname or uuid.")

#Parse server uuid and find storage uuid
srvdet = requests.get('https://api.upcloud.com/1.2/server/' + hosts[srvhostname], auth=HTTPBasicAuth('user', 'pass'))
srvdet_json = srvdet.json()
datas = srvdet.json()
print(datas)
for device in datas['server']['storage_devices']['storage_device']:
    stguuid = device['storage']
    print(stguuid)


#Check backup uuid details
bkplist=requests.get('https://api.upcloud.com/1.2/storage/backup', auth=HTTPBasicAuth('user', 'pass'))
bkplist_json = bkplist.json()
backup_list = bkplist.json()
bkpsts = backup_list['storages']['storage']
print(bkpsts)


#Get server uuid and match with storage
backup = {}
for u in backup_list['storages']['storage']:
    srvuuidorg = u['origin']
    backup_status = u['state']
    backup[srvuuidorg] = backup_status
    print(backup)

#Retrieve storage uuid and backup status
backupsts = defaultdict(list)
for u in backup_list['storages']['storage']:
    srvuuidorg = u['origin']
    backup_uuid = u['uuid']
    backupsts[srvuuidorg].append(backup_uuid)
    backup[srvuuidorg].append(status)