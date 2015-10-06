
import web
import flows_handler_classes

urls = (
    'flows/block/ip' , 'FlowsBlockIP'
    'flows/block/mac' , 'FlowsBlockMAC'
    'flows/block/port' , 'FlowsBlockPort'
    'flows/block/betweentimes' , 'FlowsBlockTimes'
    'flows/nonblock/betweentimes' , 'FlowsNonblockTimes'
    'flows/block/protocol' , 'FlowsBlockProtocol'
    'flows/block/protocolport' , 'FlowsBlockProtocolPort'
    'flows/block/list' , 'FlowsBlockList'
    'flows/nonblock/list' , 'FlowsNonblockList'
    'flows/block/all', 'FlowsBlockAll'
)

def setting_server():
    app = web.application(urls, globals())
    return app
