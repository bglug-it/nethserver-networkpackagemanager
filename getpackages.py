#!/usr/bin/env python

from subprocess import Popen, PIPE
import json
import sys

def getpackages(role):
    result = {'role': role, 'addpkg': [], 'delpkg': []}
    try:
        db = Popen(['db', 'roles', 'getjson'], stdout=PIPE).communicate()[0]
        for data in json.loads(db):
            if data['name'] == role:
                result['addpkg'] = data['props']['Addpkg'].split()
                result['delpkg'] = data['props']['Delpkg'].split()
                return result
    except:
        pass
    return result

print getpackages(sys.argv[1])
