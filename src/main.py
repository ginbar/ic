
import api.rest_api.py


def main():
    print 'Starting server...'
    app = web.application(url, globals())
    app.run()
    print 'Server running. Listening for request on port 8080.'


if __name__ == '__main__':
    main()
