#!/usr/bin/python3

import json
import yaml

dumpme = {"errorips": []}

with open("/home/student/ans/files/log.example") as lef:
    for line in lef:
        if "ERROR" in line:
            loggedip = line.split()[1]
            dumpme["errorips"].append(loggedip)

# print(json.dumps(str(dumpme)))
with open("/home/student/ans/files/parsed.ips","w") as iif:
    iif.write(yaml.dump(dumpme))
