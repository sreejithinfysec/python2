import os
from cryptography.fernet import Fernet
from flask import request, redirect, render_template
import random

from vuln_server.outputgrabber import OutputGrabber

def bypass(self):
    if request.method == 'POST':
        if request.form.get('input_data') != '':
            sanitized_input = html.escape(request.form['input_data'])
            try:
                output = OutputGrabber()
                with output:
                    code = compile(sanitized_input, '<string>', 'exec')
                    exec(code, globals(), locals())
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect('/')
    return render_template('eval.html')














































































































