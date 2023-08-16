import requests
import datetime
import reverse_geocoder
# define base URL
URL = "http://api.open-notify.org/iss-now.json"

def main():

    #part1
    iss_resp = requests.get(URL)
    iss_json = iss_resp.json()
    print(iss_json)
    
    #part2
    print('')
    print(f"CURRENT LOCATION OF THE ISS:\nLatitude: {iss_json['iss_position']['latitude']} \nLongitude: {iss_json['iss_position']['longitude']}")
    
    #part3
    print((''))
    ts = datetime.datetime.fromtimestamp(iss_json['timestamp']).strftime('%Y-%m-%d %H:%M:%S')
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {ts}\nLatitude: {iss_json['iss_position']['latitude']} \nLongitude: {iss_json['iss_position']['longitude']}")

    #part4
    print('')
    loc_name= reverse_geocoder.search((iss_json['iss_position']['latitude'],iss_json['iss_position']['longitude']))
    city= loc_name[0]["name"]
    # slice the object again to return the country
    country= loc_name[0]["cc"]
    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {ts}\nLatitude: {iss_json['iss_position']['latitude']} \nLongitude: {iss_json['iss_position']['longitude']}\nCity/Country: {city}, {country}")

    
    
if __name__ == "__main__":
    main()