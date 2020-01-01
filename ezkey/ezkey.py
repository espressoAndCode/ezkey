import os
import json

def getkey(name):

    # Get user home path and create full filepath
    home = os.path.expanduser("~") + '/'
    keyvault_path = os.path.join(home, '.keyvault.json')

    if (os.path.exists(keyvault_path)):
        with open(keyvault_path, 'r') as f:
            # Guard against empty file
            file = f.read()
            if len(file) > 0:
                keyfile = json.loads(file)

    try:
        return keyfile[name]['value']
    except KeyError:
        return "Error - Key not found"
