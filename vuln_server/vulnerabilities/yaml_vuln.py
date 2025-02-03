import yaml
from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class YAMLVuln():

def injection(self):
    if request.method == 'POST':
        if request.form['input_data'] != '':
            try:
                output = OutputGrabber()
                with output:
                    yaml.safe_load(request.form['input_data'])
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('yaml.html')


























