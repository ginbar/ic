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


class PortApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))


def setting_server():
    app = PortApplication(urls, globals())
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


class AddBlockPort:
    def POST(self):
        msg = web.input()
        port = msg.port
        ryu_con.insert_block_by_mac(port)


class DeleteBlockPort:
    def POST(self):
        msg = web.input()
        port = msg.port
        ryu_con.remove_block_by_mac(port)


class AddBlockTimes:
    def POST(self):
        msg = web.input()
        ip, t1, t2 = msg.ip, msg.t1, msg.t2
        pyke_rules.insert_block_between_time(ip, t1, t2)


class DeleteBlockTimes:
    def POST(self):
        msg = web.input()
        ip, t1, t2 = msg.ip, msg.t1, msg.t2
        pyke_rules.remove_block_between_time(ip, t1, t2)


class AddNonblockTimes:
    def POST(self):
        msg = web.input()
        ip, t1, t2 = msg.ip, msg.t1, msg.t2
        pyke_rules.insert_nonblock_between_time(ip, t1, t2)


class DeleteNonblockTimes:
    def POST(self):
        msg = web.input()
        ip, t1, t2 = msg.ip, msg.t1, msg.t2
        pyke_rules.insert_nonblock_between_time(ip, t1, t2)
"""
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
