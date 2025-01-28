import subprocess

from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class SubprocessVuln():

def bypass(self):
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour.
        input_data = request.form.get('input_data', '')
        if input_data != '':
            try:
                # Execute system command with an unsafe input parameter
                # Replaced subprocess.call with subprocess.check_output
                # Use shlex.split to sanitize and split the input
                result = subprocess.check_output(shlex.split("ping -c1 " + input_data))
                return result.decode('utf-8')
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('subprocess.html')





