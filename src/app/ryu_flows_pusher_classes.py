
import ryu.app.ofctl_rest as ryu_con
import requests

dp_id = 264705663479227

def uri_format():
    return 'http://localhost:8080/uri'

def insert_block_by_ip(ip):
    print 'insert_block_by_ip foi invocado com ip: ' + ip
    uri = 'stats/flowentry/add'
    flow_format = {
        "dpid": dp_id,
        "match":{"ipv4_dst":ip},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def remove_block_by_ip(ip):
    print 'remove_block_by_ip foi invocado com mac: ' + ip
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
        "dpid": dp_id,
        "match":{"ipv4_dst":ip},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def insert_block_by_mac(mac):
    print 'insert_block_by_mac foi invocado com mac: ' + mac
    uri = 'stats/flowentry/add'
    flow_format = {
        "dpid": dp_id,
        "match":{"eth_dst":mac},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def remove_block_by_mac(mac):
    print 'insert_block_by_mac foi invocado com mac: ' + mac
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
        "dpid": dp_id,
        "match":{"eth_dst":mac},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def insert_block_by_port(port):
    print 'insert_block_by_mac foi invocado com mac: ' + mac
    uri = 'stats/flowentry/add'
    flow_format = {
        "dpid": dp_id,
        "match":{"tp_dst":port},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    requests.post(uri_format().replace('uri', uri), flow_format)


def remove_block_by_port(port):
    print 'insert_block_by_mac foi invocado com mac: ' + mac
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
        "dpid": dp_id,
        "match":{"tp_dst":port},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    requests.post(uri_format().replace('uri', uri), flow_format)
