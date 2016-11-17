#!/usr/bin/env python
#-*- coding:utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import time
import urllib.parse
import json


HOST_NAME = sys.argv[1]
PORT_NUMBER = int(sys.argv[2])


def handle_hook(payload):

    script_dir = os.path.join(os.curdir, 'scripts')
    repo = payload['repository']['name']
    branch = payload['ref'].split('/')[2]

    possible_scripts = [
    os.path.join(script_dir, repo),
    os.path.join(script_dir, '%s-%s' % (repo, branch)),
    os.path.join(script_dir, "all"),
    ]

    # Run all scripts that exist for either repo, repo-branch, or all
    for script in possible_scripts:
        if os.path.exists(script):
            os.system("%s" % script)
            # os.system("%s \'%s\'" % (script, json_payload))

    pass


class HookHandler(BaseHTTPRequestHandler):
    server_version = "HookHandler/0.1"
    def do_GET(s):
        s.wfile.write(bytes('Status: OK', 'utf8'))
        s.send_response(200)

    def do_POST(s):
        # Validate request source ip is in GitHub ip range
        if not any(s.client_address[0].startswith(IP) for IP in ('192.30.252', '192.30.253', '192.30.254', '192.30.255')):
            s.send_error(403)

        # Validate request secret key is correct

        # Read in the json payload
        length = int(s.headers['Content-Length'])
        post_data = parse.parse_qs(s.rfile.read(length).decode('utf-8'))
        payload = json.loads(post_data['payload'][0])

        # Process the payload
        handle_hook(payload)

        # Report success.
        s.send_response(200)

if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), HookHandler)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
