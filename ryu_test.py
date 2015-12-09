import requests

r = requests.get('http://localhost:8080/stats/switches')
print r.text
r = requests.get('http://localhost:8080/stats/desc/264705663479227')
print r.text

flow = """{
    "dpid": 264705663479227,
    "cookie": 1,
    "cookie_mask": 1,
    "idle_timeout": 30,
    "hard_timeout": 30,
    "priority": 11111,
    "flags": 1,
    "match":{
        "in_port":1
    },
    "actions":[
        {
            "type":"OUTPUT",
            "port": 2
        }
    ]
    }"""

r = requests.post('http://localhost:8080/stats/flowentry/add', data=flow)
print r.status_code
print r.text

r = requests.get('http://localhost:8080/stats/table/264705663479227')
print r.text

r = requests.get('http://localhost:8080/stats/tablefeatures/264705663479227')
print r.text

r = requests.get('http://localhost:8080/stats/flow/264705663479227')
print r.text
