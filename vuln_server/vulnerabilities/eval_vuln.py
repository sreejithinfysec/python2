import os
from cryptography.fernet import Fernet
from flask import request, redirect, render_template
import random

from vuln_server.outputgrabber import OutputGrabber
import ast
from flask import request, redirect, render_template

def bypass(self):
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour.
        if request.form.get('input_data') != '':
            # Define a regex pattern to check for dangerous characters
            pattern = re.compile(r'[\w\.\!\$\*\(\)\+\-\=\[\]\{\}\|\:\;\'\<\>\?\@\\\"\,\/\ ]*')
            # Use the pattern to check the input data
            if pattern.fullmatch(request.form['input_data']):
                try:
                    # Use ast.literal_eval to safely evaluate the input data
                    data = ast.literal_eval(request.form['input_data'])
                    return "Data evaluated successfully"
                except (ValueError, SyntaxError) as e:
                    return "Invalid input: {}".format(str(e))
            else:
                return "Invalid input: unsafe data detected"
        else:
            return redirect(request.url)
    return render_template('eval.html')












































































































