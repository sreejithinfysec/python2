import yaml
from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class YAMLVuln():

def injection(self):
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour
        if 'input_data' in request.form and request.form['input_data'] != '':
            try:
                # Instanciate a different stdout grabber for subprocess
                output = OutputGrabber()
                with output:
                    # Load safe YAML input, output from the exploit
                    # is stored into Outputgrabber stdout
                    yaml_data = yaml.safe_load(request.form['input_data'])
                    return yaml_data
            except Exception as e:
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('yaml.html')






