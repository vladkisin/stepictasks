# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 14:13:21 2019

@author: Lenovo
"""
import operator
import requests
import json
client_id = '059562a589971386f79c'
client_secret = 'dc6aeec64b0488df62a508b0f8e1f457'
user_data = {'client_id' : client_id,
'client_secret' : client_secret}
r = requests.post("https://api.artsy.net/api/tokens/xapp_token", data = user_data)
j = json.loads(r.content.decode('utf-8')) #get the token
token = j['token']
#work with requests
headers = {"X-Xapp-Token" : token}
output_data = {}
with open('dataset_24476_4.txt', 'r') as f:
    for name_id in f:
        name_id = name_id.rstrip()
        url = "https://api.artsy.net/api/artists/"+ name_id
        res = requests.get(url, headers=headers)
        j = json.loads(res.content.decode('utf-8'))
        output_data[j['sortable_name']] = j['birthday']
sorted_x = sorted(output_data.items(), key=operator.itemgetter(1))
with open ('ans.txt','w', encoding = 'utf-8') as t:
    for artist in sorted_x:
        t.write(artist[0] + '\n')