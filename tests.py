import json
import requests

r = requests.post('http://0.0.0.0:8000/add_by_ip', data={"ip":"666"})
print r.status_code

#r = requests.post('http://0.0.0.0:8000/delete_by_ip', data={"ip":"666"})
#print r.status_code

r = requests.post('http://0.0.0.0:8000/add_blockbetweentimes',
                    data={"ip": "666", "t1": "18:00", "t2": "19:00"})
print r.status_code

"""
r = requests.post('http://0.0.0.0:8000/delete_by_ip', data={"ip":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/add_by_mac', data={"mac":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/delete_by_mac', data={"mac":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/add_by_port', data={"port":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/delete_by_port', data={"port":"666"})
print r.status_code
"""
