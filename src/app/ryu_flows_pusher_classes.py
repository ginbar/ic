
import ryu.app.ofctl_rest as ryu

def insert_block_by_ip(ip):
    flow_format = """{
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
    }
 }""".replace('target_ip', ip)

 def remove_block_by_ip(ip):
     flow_format = """{
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
    }
 }""".replace('target_ip', ip)
