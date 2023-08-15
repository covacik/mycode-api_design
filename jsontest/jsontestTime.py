

#!/usr/bin/python3

import requests

# define the URL we want to use
DATEURL = "http://date.jsontest.com/"

def main():
    # use requests library to send an HTTP GET
    resp = requests.get(DATEURL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    respjson = resp.json()

    # display our PYTHONIC data (LIST / DICT)
    print(respjson)

    # JUST display the value of "ip"
    print(f"The timestamp is --> {respjson['milliseconds_since_epoch']}")

if __name__ == "__main__":
    main()