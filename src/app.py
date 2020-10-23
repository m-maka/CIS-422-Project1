import os
import execute 
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory, g, flash 
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = set(['.gpx'])
app.config['UPLOAD_PATH'] = 'uploads'



################################################################
# API functions for Flask App
################################################################
def execute(filename, apikey):
    
    # Read the gpx file and turn it into a list of Lattitude/Longitude
    # Coordinates
    coordinates = gpxparse.read(filename)
    
    # Read Google API key from text file and insert it
    keyfile = open(apikey)
    key = keyfile.read().replace("\n", " ")
    gmaps = findturns.googlemaps.Client(key=key)
    
    # Divide the track into smaller segments that the Google API can work with
    segments = findturns.createSegments(coordinates)

    # Get directions for the created track segments
    directions = findturns.getDirections(gmaps, segments)

    # Convert the directions into instructions that are easier to read
    instructions = findturns.parseDirections(directions)

    # Turn instructions into a text file
    findturns.instructionsToText(instructions)

    # Return the instructions
    return instructions


################################################################
# Flask App
################################################################
@app.route('/')
def index():
    return render_template('index.html')

#Handling upload file
@app.route('/', methods=['POST'])
def upload_files():
    # Holds the submitted file object
    uploaded_file = request.files['file']
    # Holds 
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            #Redirect to index if not a gpx file
            flash("Please select a gpx file")
            return redirect(url_for('index'))
        full_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(full_path)
        #execute function will pass the file path in and use it to open/read the file
        g.results = execute(full_path, API_KEY)
    return render_template('display.html')


if __name__ == '__main__':
   app.run(debug = True)