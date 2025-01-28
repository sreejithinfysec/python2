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
            data = os.urandom(1).randint(1, 1000)
            try:
                # Eval input data and execute code from it
                if data != int(request.form['input_data']):
                    pass
                return "Server Error: Random number does not match input."
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('eval.html')


































































































































