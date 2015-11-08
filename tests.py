import json
import requests

r = requests.post('http://0.0.0.0:8000/add_by_ip', data={"ip":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/delete_by_ip', data={"ip":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/add_by_mac', data={"mac":"666"})
print r.status_code
r = requests.post('http://0.0.0.0:8000/delete_by_mac', data={"mac":"666"})
print r.status_code
