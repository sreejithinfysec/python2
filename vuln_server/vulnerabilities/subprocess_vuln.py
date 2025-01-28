import subprocess

from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class SubprocessVuln():

def bypass(self):
        if request.method == 'POST':
            # Check if data is not empty, post forms has all params defined
            # which may be empty and cause unexpected behaviour.
            if request.form['input_data'] != '':
                try:
                    # Instanciate a different stdout grabber for subprocess
                    output = OutputGrabber()
                    with output:
                        # Execute system command with an unsafe input parameter
                        subprocess.run(["ping", "-c1", request.form['input_data']], 
                                       check=True, 
                                       stdout=subprocess.PIPE, 
                                       stderr=subprocess.PIPE)
                    return output.capturedtext
                except subprocess.CalledProcessError as e:
                    return "Server Error: {}:".format(str(e.stderr))
            else:
                return redirect(request.url)
        return render_template('subprocess.html')







