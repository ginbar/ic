
import api.rest_api as rest
import web
import thread
import pyke.rules_tester as pyke
import logging

def main():
    print 'Pyke: Starting'
    print 'Pyke: Asserting .kfb'
    thread.start_new_thread(pyke.test_rules, ())
    print 'Starting server...'
    app = rest.setting_server()
    thread.start_new_thread(start_server, (app,))
    print 'Server running. Listening for request on port 8080.'
    while True:
        pass

def start_server(app):
    app.run(port=8000)


if __name__ == '__main__':
    main()
