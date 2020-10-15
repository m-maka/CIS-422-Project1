'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

This file contains functions to take a list of (lat, long) tuples, and convert them into directions a human can follow.

Powered by Google Maps
'''

import googlemaps

def parseDirections(directions):
    '''
    Takes a list of directions from the Google Maps Directions api, and parses
    out the relevant directional info that a human needs/can read

    returns a list of (distance of direction, direction to be done) tuples
    '''
    instructions = []
    for segment in directions:
        for step in segment[0]['legs'][0]['steps']:
            print(step['distance']['text'])
            print(step['html_instructions'])
            instructions.append((step['distance']['text'], step['html_instructions']))
    print()
    return instructions

def getDirections(client, segments):
    '''
    Takes a googlemaps client, and a list of dictionaries (1 for each segment of the track,
    and uses them to get directions from the Google Maps Directions api

    returns the directions as a list of lists(each containing directions for their segment)
    '''
    directions = []
    for segment in segments:
        if 'waypoints' in segment.keys():
            directions.append(client.directions(segment['start'], segment['end'], None, segment['waypoints']))
        else:
             directions.append(client.directions(segment['start'], segment['end']))
    print(directions)

    return  directions


def createSegments(latlongs):
    '''
    A track often contains more points then a directions request can
    have waypoints, so this function divides it into segments that will
    fit within the Google Maps Directions api.
    Each segment starts on the same point the last segment ended on

    returns a list of dictionaries
    '''
    length = len(latlongs)

    # Check for 10 vs 25 waypoints
    if length <=12:
        pointCount = 10
    else:
        pointCount = 25
    # Calculate segments needed (+1 for sub 25 point tracks)
    segNumb = (length // 25) + 1
    index = 0
    segments = []
    for segment in range(segNumb):
        #print(f'start (index {index})')
        #wp = 1
        segments.append({'start' : latlongs[index]})
        waypoints = []
        index += 1

        # min(index + pointCount, length - 2) to determine if this is the last segment
        # - 2 to account for indexing starting at 0, and overlap of segments
        for index in range(index, min(index + pointCount,length - 2)):
            #print(f'wp, {wp} (index {index})')
            #wp += 1
            waypoints.append(f'via:{latlongs[index][0]},{latlongs[index][1]}')
            waypoints.append(latlongs[index])
        
        if len(waypoints):
            segments[segment]['waypoints'] = waypoints
            index += 1
        #print(f'end (index {index})')
        segments[segment]['end'] = latlongs[index]
    return segments


def main():
    '''Just for testing'''
    '''
    latlongs = [(44.2185374, -123.2125012), (44.21857, -123.21163),
                (44.21898, -123.21158), (44.2190527, -123.2089076),
                (44.2225, -123.20905), (44.2223507, -123.2147348),
                (44.22415, -123.21471), (44.22468, -123.21394),
                (44.2264858, -123.2139206)]
    '''
    latlongs = [(44.587662, -123.256691), (44.587395, -123.262154), (44.587502, -123.262497),
                (44.596886, -123.262482), (44.598633, -123.26149), (44.599155, -123.261673),
                (44.60146, -123.263374), (44.602081, -123.263222),(44.602959, -123.262421),
                (44.603649, -123.262161), (44.612709, -123.262253), (44.613117, -123.267418),
                (44.613689, -123.268028), (44.616093, -123.268036), (44.616718, -123.268425),
                (44.616905, -123.26915), (44.616951, -123.274727), (44.6172449, -123.275269),
                (44.618179, -123.275856), (44.618835, -123.275887), (44.6216579, -123.275101),
                (44.622791, -123.274361),(44.62421, -123.27401), (44.626221, -123.27269)]
    gmaps = googlemaps.Client(key='Your Key Here')
    segments = createSegments(latlongs)
    directions = getDirections(gmaps, segments)
    instructions = parseDirections(directions)
    print(instructions)


if __name__ == '__main__':
    main()
