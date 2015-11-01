import web
import json
import re
import app.ryu_flows_pusher_classes as ryu_con
import app.pyke_facts_insert_classes as pyke_rules

urls = (
    '/add_by_ip' , 'AddBlockIP',
    '/delete_by_ip', 'DeleteBlockIP',
    '/add_by_mac' , 'AddBlockMAC',
    '/delete_by_mac' , 'DeleteBlockMAC',
    '/add_by_port' , 'AddBlockPort',
    '/delete_by_port' , 'DeleteBlockPort',
    '/add_blockbetweentimes' , 'AddBlockTimes',
    '/delete_blockbetweentimes' , 'DeleteBlockTimes',
    '/add_nonblockbetweentimes' , 'AddNonblockTimes',
    '/delete_nonblockbetweentimes' , 'DeleteNonblockTimes',
    '/add_by_protocol' , 'AddBlockProtocol',
    '/delete_by_protocol' , 'DeleteBlockProtocol',
    '/add_by_protocolport' , 'AddBlockProtocolPort',
    '/add_by_protocolport' , 'DeleteBlockProtocolPort',
    '/list' , 'ListBlock',
    '/lock', 'Lock',
    '/unlock', 'Unlock'
)


def setting_server():
    app = web.application(urls, globals())
    return app


class AddBlockIP:
    def POST(self):
        msg = web.input()
        ip = msg.ip
        ryu_con.insert_block_by_ip(ip)


class DeleteBlockIP:
    def POST(self):
        msg = web.input()
        ip = msg.ip
        ryu_con.remove_block_by_ip(ip)


class AddBlockMAC:
    def POST(self):
        msg = web.input()
        mac = msg.mac
        ryu_con.insert_block_by_mac(mac)


class DeleteBlockMAC:
    def POST(self):
        msg = web.input()
        mac = msg.mac
        ryu_con.remove_block_by_mac(mac)

"""
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
