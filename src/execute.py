'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

This is the main file in the program. It will take a GPX file as an input, then
call all the necessary functions to execute the program, and return a list
of directions/instructions for the inputed track.
'''

import gpxparse
import findturns

def execute(filename):
    
    # Read the gpx file and turn it into a list of Lattitude/Longitude
    # Coordinates
    coordinates = gpxparse.read(filename)
    
    # Ask for Google API key
    gmaps = findturns.googlemaps.Client(key='your key here')
    
    # Divide the track into smaller segments that the Google API can work with
    segments = findturns.createSegments(coordinates)

    # Get directions for the created track segments
    directions = findturns.getDirections(gmaps, segments)

    # Convert the directions into instructions that are easier to read
    instructions = findturns.parseDirections(directions)

    # Return the instructions
    return instructions


if __name__ == '__main__':
    main()
