'''
Authors: Brandon Bower along with Max Aguirre and Mapuana Maka

This is the main file in the program. It will take a GPX file as an input, then
call all the necessary functions to execute the program, and return a list
of directions/instructions for the inputed track.
'''

import gpxparse
import findturns

def main():

    # I assume the file will be fetched differently at the end. ~ Max
    file = "small.gpx"
    
    # Read the gpx file and turn it into a list of Lattitude/Longitude
    # Coordinates
    coordinates = gpxparse.read(file)
    
    # Ask for Google API key
    gmaps = findturns.googlemaps.Client(key='Your Key Here')
    
    # Divide the track into smaller segments that the Google API can work with
    segments = findturns.createSegments(coordinates)

    # Get directions for the created track segments
    directions = findturns.getDirections(gmaps, segments)

    # Convert the directions into instructions that are easier to read
    instructions = findturns.parseDirections(directions)

    # Print the instructions
    print(instructions)


if __name__ == '__main__':
    main()