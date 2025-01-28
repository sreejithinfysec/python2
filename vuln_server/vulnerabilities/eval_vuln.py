import os
from cryptography.fernet import Fernet
from flask import request, redirect, render_template
import random

from vuln_server.outputgrabber import OutputGrabber
import ast
from flask import request, redirect, render_template

def bypass(self):
    if request.method == 'POST':
        if request.form.get('input_data') != '':
            sanitized_input = bleach.clean(request.form['input_data'])
            data = random.SystemRandom().randint(1, 1000)
            try:
                output = OutputGrabber()
                with output:
                    code = compile(sanitized_input, '<string>', 'exec')
                    exec(code, globals(), locals())
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('eval.html')















