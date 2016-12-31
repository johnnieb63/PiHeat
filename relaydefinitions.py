# this file must be in the same folder as c-Pi: temp2.py and s-Pi /todo-api/webrelay.py & req.py
relays = [
    { 'id' : 1, 'name' : 'hot', 'state' : 'off'},
    { 'id' : 2, 'name' : 'warm', 'state' : 'off'},
    { 'id' : 3, 'name' : 'cold', 'state' : 'on'},
    #{ 'id' : 4, 'name' : 'temp', 'state' : 'value'}
    ]


relayIdToPin = {
    1 : 12,
    2 : 16,
    3 : 20,
    #4 : 15
    }
