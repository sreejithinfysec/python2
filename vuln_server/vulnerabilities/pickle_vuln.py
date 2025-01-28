import base64
import pickle
from vuln_server.outputgrabber import OutputGrabber
from flask import flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os

class PickleVuln():

    def __reduce__(self):
        # This method is called when an object is about to be serialized
        # We return a tuple that represents the function to call and its arguments
        return (self.__class__, ())

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
                    # Load base64 encoded pickle object
                    pickle.loads(
                        base64.b64decode(request.form['input_data'].encode()),
                        # Specify a safe_load function that only allows certain types of objects to be deserialized
                        onload=[pickle.Unpickler],
                        fiximports=True)
                except Exception as e:
                    return "Server Error: {}:".format(str(e))
            elif 'file' in request.files and request.files['file'].filename != '':
                file_data = request.files['file'].read()
                try:
                    pickle.loads(base64.b64decode(file_data),
                                 onload=[pickle.Unpickler],
                                 fiximports=True)
                except Exception as e:
                    return "Server Error: {}:".format(str(e))
            else:
                flash('No selected file')
                return redirect(request.url)
        return render_template('pickle.html')














































































































































