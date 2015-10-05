
import json
import web
import re

class FlowsBlockIP:
    def POST():
        msg = web.data()
        ip = json.loads(msg)

    def DELETE():
        msg = web.data()
        ip = json.loads(msg)
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
