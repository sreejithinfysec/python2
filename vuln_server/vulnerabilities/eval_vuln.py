import ast
from flask import request, redirect, render_template
import random

def bypass(self):
    if request.method == 'POST':
        if request.form['input_data'] != '':
            try:
                output = OutputGrabber()
                with output:
                    json.JSONDecoder(object_hook=lambda d: {k: v for k, v in d.items() if isinstance(k, str) and isinstance(v, str)}).decode(html.escape(request.form['input_data']))
                return output.capturedtext
            except Exception as e:
                logging.warning("Server Error: {}".format(str(e)))
                return str(e)
        else:
            return redirect(request.url)
    return render_template('eval.html')








































































































































































































































