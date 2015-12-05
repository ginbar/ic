
import ryu.app.ofctl_rest as ryu_con
import requests

dp_id = 264705663479227

def uri_format():
    return 'http://localhost:8080/uri'

def insert_block_by_ip(ip):
    uri = 'stats/flowentry/add'
    flow_format = {
        "dpid": dp_id,
        "match":{"ipv4_dst":ip},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    msg = str(flow_format)
    requests.post(uri_format().replace('uri', uri), msg)


def remove_block_by_ip(ip):
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
        "dpid": dp_id,
        "match":{"ipv4_dst":ip},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    msg = str(flow_format)
    requests.post(uri_format().replace('uri', uri), msg)


def insert_block_by_mac(mac):
    uri = 'stats/flowentry/add'
    flow_format = {
        "dpid": dp_id,
        "match":{"eth_dst":mac},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    msg = str(flow_format)
    requests.post(uri_format().replace('uri', uri), msg)


def remove_block_by_mac(mac):
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
        "dpid": dp_id,
        "match":{"eth_dst":mac},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    msg = str(flow_format)
    requests.post(uri_format().replace('uri', uri), msg)


def insert_block_by_port(port):
    uri = 'stats/flowentry/add'
    flow_format = {
        "dpid": dp_id,
        "match":{"tp_dst":port},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    msg = str(flow_format)
    requests.post(uri_format().replace('uri', uri), msg)


def remove_block_by_port(port):
    uri = 'stats/flowentry/delete_strict'
    flow_format = {
        "dpid": dp_id,
        "match":{"tp_dst":port},
        "actions":[{"type":"OUTPUT", "port": 2}]
    }
    msg = str(flow_format)
    requests.post(uri_format().replace('uri', uri), msg)
