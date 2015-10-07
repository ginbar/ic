
import ryu.app.ofctl_rest as ryu_con

def insert_block_by_ip(ip):
    uri = '/stats/flowentry/add'
    flow_format = """ """.replace('target_ip', ip)

def remove_block_by_ip(ip):
    flow_format = """ """.replace('target_ip', ip)
