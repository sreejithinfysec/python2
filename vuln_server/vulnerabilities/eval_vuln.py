import os
from cryptography.fernet import Fernet
from flask import request, redirect, render_template
import random

from vuln_server.outputgrabber import OutputGrabber

def bypass(self):
    if request.method == 'POST':
        if request.form.get('input_data') != '':
            sanitized_input = bleach.clean(request.form['input_data'], tags=[], strip=True) # Only allow text
            data = secrets.SystemRandom().randint(1, 1000) # Use secrets module for generating cryptographically strong random numbers
            try:
                output = OutputGrabber()
                with output:
                    code = compile(sanitized_input, '<string>', 'exec')
                    exec(code, globals(), locals())
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect('/') # Use relative URLs or absolute URLs that are controlled by the server
    return render_template('eval.html')













































































































