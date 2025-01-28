import os
from cryptography.fernet import Fernet
from flask import request, redirect, render_template
import random
from vuln_server.outputgrabber import OutputGrabber
import ast
from flask import request, redirect, render_template

def bypass(self):
    logger = get_logger()
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour.
        input_data = request.form.get('input_data')
        if input_data and re.match("^[0-9]+$", input_data): # Validate input data is a number
            data = flask.helpers.safe_join(random.SystemRandom(), range(1, 1000)) # Use safe_join to avoid path traversal
            try:
                # Instanciate a different stdout grabber for subprocess
                output = OutputGrabber()
                with output:
                    # Eval input data and execute code from it
                    if data != int(input_data):
                        pass
                return output.capturedtext
            except Exception as e:
                logger.error("Server Error: {}".format(str(e)))
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('eval.html')



































































































































