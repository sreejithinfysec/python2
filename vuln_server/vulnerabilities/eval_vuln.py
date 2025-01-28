import os
from cryptography.fernet import Fernet
from flask import request, redirect, render_template
import random

from vuln_server.outputgrabber import OutputGrabber
import ast
from flask import request, redirect, render_template

def bypass(self):
        if request.method == 'POST':
            if request.form['input_data'] != '':
                try:
                    output = OutputGrabber()
                    with output:
                        if random.randint(1, 1000) != json.loads(request.form['input_data']):
                            pass
                    return output.capturedtext
                except Exception as e:
                    return "Server Error: {}:".format(str(e))
            else:
                return redirect(request.url)
        return render_template('eval.html')






























