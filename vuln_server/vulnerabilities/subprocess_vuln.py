import subprocess

from vuln_server.outputgrabber import OutputGrabber
from flask import request, redirect, render_template


class SubprocessVuln():

def bypass(self):
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour.
        if request.form['input_data'] != '':
            # Validate and sanitize the user input
            input_data = re.sub(r"[^\w\s]", '', request.form['input_data'])
            try:
                # Instanciate a different stdout grabber for subprocess
                output = OutputGrabber()
                with output:
                    # Execute system command with sanitized input parameter
                    subprocess.run(["ping", "-c1", input_data], shell=False, check=True)
                return output.capturedtext
            except subprocess.CalledProcessError as e:
                # Use a logging library to handle log entries
                logger = logging.getLogger(__name__)
                logger.error("Server Error: %s", str(e))
                return "Server Error: {}:".format(str(e))
        else:
            return redirect(request.url)
    return render_template('subprocess.html')










