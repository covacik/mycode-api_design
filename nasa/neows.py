#!/usr/bin/python3
import requests
import datetime
## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def validate_date(date_text):
        try:
            datetime.date.fromisoformat(date_text)
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()
    print('Start date in YYYY-MM-DD format or just hit enter')
    sdate=input('>')
    if sdate:
        validate_date(sdate)
        startdate = "start_date="+sdate
    else:
        startdate = "start_date=2019-11-11"
    ## update the date below, if you like
    startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
