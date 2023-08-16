#bullshit ass class
import json

class ReadJson:
    def __init__(self, data, ticket, cap, vms, username, nodes):
        self.data = data
        self.ticket = ticket
        self.cap = cap
        self.vms = vms
        self.username = username
        self.nodes = nodes

with open("response3.json", "r") as ofile:
    openj = json.load(ofile) # dict

json_object = ReadJson(openj["data"], openj["data"]["ticket"], openj["data"]["cap"], openj["data"]["cap"]["vms"], openj["data"]["username"])

print(json_object.username)

