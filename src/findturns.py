'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

'''

import requests

def getloc(key, lat, long):
        query = {'point.lat' : str(lat), 'point.lon' : str(long), 'size' : 1}
        response = requests.get(f"https://api.openrouteservice.org/geocode/reverse?api_key={key}",
                                params=query)
        jsonResponse = response.json()
        name = ''
        for dictionary in jsonResponse['features']:
            if 'properties' in dictionary.keys():
                print(dictionary['properties']['label'])
                name = dictionary['properties']['label']
        return name


def turndetect(key, latlongs):
    assert len(latlongs) != 0, "Your gpx file has no lat long points"

    start = getloc(key, latlongs[0][0], latlongs[0][1])
    
    
    

def main():
    key = "you api key here for testing"
    latlongs = [(44.0451248, -123.0756419)]
    turndetect(key, latlongs)


if __name__ == '__main__':

    main()
