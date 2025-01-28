import base64
import pickle
from vuln_server.outputgrabber import OutputGrabber
from flask import flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
import hvac
import bleach

class PickleVuln():

def injection():
    """Pickle object command injection/execution.

    This function will evaluate if the user includes a file or
    a pickle base64 object and load the object.
    """
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour
        if 'input_data' in request.form and request.form['input_data'] != '':
            try:
                # Validate input
                if not re.match("^[A-Za-z0-9+/]*={0,2}$", request.form['input_data']):
                    raise ValueError("Invalid input_data")
                
                # Load base64 encoded pickle object
                pickle.loads(
                    base64.b64decode(request.form['input_data'].encode()))
                    
                return "Successfully loaded pickle object"
            except Exception as e:
                logging.error("Server Error: {}".format(str(e)))
                return "Server Error: {}:".format(str(e))
        else:
            flash('No selected file')
            return redirect(request.url)
    return render_template('pickle.html')

























































































































































