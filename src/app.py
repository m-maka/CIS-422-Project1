import os
import execute
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_EXTENSIONS'] = set(['.gpx'])
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        full_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(full_path)
        #execute function will pass the file path in and use it to open/read the file
        g.result = execute.execute(full_path)

    return redirect(url_for('index'))


if __name__ == '__main__':
   app.run(debug = True)