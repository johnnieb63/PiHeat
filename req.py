from urllib2 import Request, urlopen, URLError
import json
import time
import requests
import urllib
from flask import Flask, jsonify, abort, request, render_template
from relaydefinitions import relays, relayIdToPin


try:
            url = "https://api.particle.io/v1/devices/your device id/hot?access_token=your access token"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
            time.sleep(2)

            if (parsed_json['result']) == 0:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/4', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}


            if (parsed_json['result']) == 1:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/4', verify=False, json={"state": "on"})
                headers = {'Content-type': 'application/json'}

except URLError, e:
            print "something happened"
