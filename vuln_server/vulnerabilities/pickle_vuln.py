import base64
import pickle
from vuln_server.outputgrabber import OutputGrabber
from flask import flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
import hvac

class PickleVuln():

def injection(self):
    """Pickle object command injection/execution.

    This function will evaluate if the user includes a file or
    a pickle base64 object and load the object.
    """
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour
        if request.form['input_data'] != '':
            try:
                # Load base64 encoded pickle object
                pickle.loads(
                    base64.b64decode(urllib.parse.unquote(request.form['input_data'])))
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        elif request.files['file'].filename != '':
            file_data = request.files['file'].read()
            try:
                pickle.loads(base64.b64decode(urllib.parse.unquote(file_data.decode())))
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            flash('No selected file')
            return redirect(request.url)
    return render_template('pickle.html')























































































































































































































































































































































































































































