# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 13:42:17 2019

@author: Lenovo
"""
import requests
city = str(input('City? '))
api_url = 'http://api.openweathermap.org/data/2.5/weather'
params = {
        'q': city,
        'appid': '444e093996c587185374196fe83fa56b',
        'units': 'metric'
}
res = requests.get(api_url, params = params)
data = res.json() #json_loads() to res
temp = 'Current weather temperature in {} is {} C°'
print(temp.format(city, data['main']['temp']))