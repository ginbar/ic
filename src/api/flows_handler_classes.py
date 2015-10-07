
import json
import web
import re
import app.ryu_flows_pusher_classes as ryu_con
import app.pyke_facts_insert_classes as pyke

class FlowsBlockIP:
    def POST():
        msg = web.data()
        ip = json.loads(msg)
        ryu_con.insert_block_by_ip(ip)

    def DELETE():
        msg = web.data()
        ip = json.loads(msg)
        ryu_con.remove_block_by_ip(ip)


"""
class FlowsBlockMAC:
    def POST():

    def DELETE():

class FlowsBlockPort:
    def POST():
    def DELETE():

class FlowsBlockTimes:
    def POST():
    def DELETE():

class FlowsNonblockTimes:
    def POST():
    def DELETE():

class FlowsBlockProtocol:
    def POST():
    def DELETE():

class FlowsBlockProtocolPort:
    def POST():
    def DELETE():

class FlowsBlockList:
    def GET():

class FlowsNonblockList:
    def GET():

class FlowsBlockAll
    def POST():
    def DELETE():
"""
