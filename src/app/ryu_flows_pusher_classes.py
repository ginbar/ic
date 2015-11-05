
import ryu.app.ofctl_rest as ryu_con
import requests

def uri_format():
    return 'http://localhost:8080/uri'

def insert_block_by_ip(ip):
    print 'insert_block_by_ip foi invocado com ip: ' + ip
    uri = 'stats/flowentry/add'
    flow_format = {
    "dpid": 1,
    "cookie": 1,
    "cookie_mask": 1,
    "table_id": 0,
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
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def remove_block_by_ip(ip):
    print 'remove_block_by_ip foi invocado com mac: ' + ip
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
    "dpid": 1,
    "cookie": 1,
    "cookie_mask": 1,
    "table_id": 0,
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
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def insert_block_by_mac(mac):
    print 'insert_block_by_mac foi invocado com mac: ' + mac
    uri = 'stats/flowentry/add'
    flow_format = {
    "dpid": 1,
    "cookie": 1,
    "cookie_mask": 1,
    "table_id": 0,
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
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def remove_block_by_mac(mac):
    print 'insert_block_by_mac foi invocado com mac: ' + mac
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
    "dpid": 1,
    "cookie": 1,
    "cookie_mask": 1,
    "table_id": 0,
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
    }
    requests.post(uri_format().replace('uri', uri), flow_format)
