
import web
import flows_handle_classes.py

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


if __name__ == '__main__':
    app = we.application(url, globals())
    app.run()
