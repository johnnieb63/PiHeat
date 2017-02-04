from urllib2 import Request, urlopen, URLError
import json
import time
import requests
import urllib
from flask import Flask, jsonify, abort, request, render_template
from relaydefinitions import relays, relayIdToPin


try:
            url = "https://api.particle.io/v1/devices/2532478653876533/hot?access_token=399453764532765432875236487624"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)

            if (parsed_json['result']) == 0:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/4', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}


            if (parsed_json['result']) == 1:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/4', verify=False, json={"state": "on"})
                headers = {'Content-type': 'application/json'}


            url = "https://api.particle.io/v1/devices/25002400jhgasjhdgjhagjhgasd31/digivalue1?access_token=3940ba7897325987523895896b032f3d24"

            json_string = urllib.urlopen(url).read()
            parsed_json = json.loads(json_string)
            cTemp = (parsed_json['result'])

            r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/5', verify=False, json={"state": cTemp})
            headers = {'Content-type': 'application/json'}

            if cTemp < 20:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/3', verify=False, json={"state": "on"})
                headers = {'Content-type': 'application/json'}

                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/1', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}

                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/2', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}

            if cTemp > 22:
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/1', verify=False, json={"state": "on"})
                headers = {'Content-type': 'application/json'}

                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/2', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}

                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/3', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}

            if ((cTemp >= 20) and (cTemp <= 22)):
                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/2', verify=False, json={"state": "on"})
                headers = {'Content-type': 'application/json'}

                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/1', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}

                r = requests.put('http://192.168.0.112:80/WebRelay/api/relays/3', verify=False, json={"state": "off"})
                headers = {'Content-type': 'application/json'}


except URLError, e:
            print "something happened"







