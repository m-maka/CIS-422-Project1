'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

This file contains functions to take a list of (lat, long) tuples, and
convert them into directions a human can follow.

Powered by Google Maps
'''

import googlemaps

def instructionsToText(instructions):
    '''
    Takes in the instructions list created by parseDirections
    and writes it to a text file, in a readable HTML form
    '''
    with open("uploads/directions.txt", 'w') as directions:
        for line in instructions:
            directions.write(f"{line[2]}: {line[1]} and travel for {line[0]}\n")
        

def parseDirections(directions):
    '''
    Takes a list of directions from the Google Maps Directions api, and parses
    out the relevant directional info that a human needs/can read

    returns a list of (distance of direction, direction to be done, total distance traveled) tuples
    '''
    instructions = []
    miles = 0.00
    feet = 0
    for segment in directions:
        for step in segment[0]['legs'][0]['steps']:
            #instructions.append((step['distance']['text'], step['html_instructions']))
            distance = step['distance']['text']
            line = step['html_instructions']

            # remove destination messages
            index = line.find('<d')
            if index != -1:
                line = line[:index]
                
            # creat tuple for each intsruction
            instructions.append((distance, line, f"{miles} mi"))

            # update running total
            numb, units = distance.split()
            numb = float(numb)
            if units == 'ft':
                # convert feet to miles
                numb = numb/5280
            miles = round(miles + numb, 2)

    return instructions

def getDirections(client, segments):
    '''
    Takes a googlemaps client, and a list of dictionaries (1 for each segment of the track,
    and uses them to get directions from the Google Maps Directions api

    returns the directions as a list of lists(each containing directions for their segment)
    '''
    directions = []
    for segment in segments:
        # Check that there are waypoints, before making a request with them
        if 'waypoints' in segment.keys():
            directions.append(client.directions(segment['start'], segment['end'], "bicycling", segment['waypoints']))
        else:
             directions.append(client.directions(segment['start'], segment['end'], "bicycling"))

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

    # Do for every segment
    for segment in range(segNumb):
        segments.append({'start' : latlongs[index]})
        waypoints = []
        index += 1

        # min(index + pointCount, length - 2) to determine if this is the last segment
        # -2 to account for segment overlap, as well as endpoint not being a waypoint
        for index in range(index, min(index + pointCount,length - 2)):
            waypoints.append(f'via:{latlongs[index][0]},{latlongs[index][1]}')
        
        if len(waypoints):
            segments[segment]['waypoints'] = waypoints
            index += 1
        segments[segment]['end'] = latlongs[index]

    return segments
