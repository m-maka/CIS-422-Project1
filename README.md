# CIS-422-Project 1

Project 1 for CIS 422 at the University of Oregon, Fall 2020.

## Authors

Mapuana Maka, Brandon Bower, Max Aguirre

## Brief Description

This program is a reverse geocoder that runs on Flask. It converts a record consisting of a sequence of coordinates into a list of turn-by-turn directions.

The program takes a GPX file as an input, which contains GPS data stored in the GPS Exchange format.

The program will then extract a sequence of lattitude/longitude coordinate pairs from the file, and use them to create a set of directions for the track that was traveled.

To make the conversion into directions, the program makes use of the Google Maps API.

The program then outputs a list of directions to the user, which can be used to retrace the route that generated the GPX file.

## Build Process Summary

Please refer to the 'Installation_Instructions.txt' in the 'documents' folder

## Subdirectory Information

src: Contains all python files for the source code of the program.

documents: Contains text files of all documentation for the project

tests: Contains files that can be used to test whether the source code is working correctly.

version-0-files (working name): Contains files that belonged to the first pursued version of this program. More info in the txt file.