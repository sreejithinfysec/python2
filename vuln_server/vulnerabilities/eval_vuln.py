import ast
from flask import request, redirect, render_template
import random

def bypass(self):
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour.
        if request.form.get('input_data') != '':
            data = random.SystemRandom().randint(1, 1000)
            try:
                # Instanciate a different stdout grabber for subprocess
                output = OutputGrabber()
                with output:
                    # Execute code from it
                    code = ast.parse(request.form['input_data'], mode='exec')
                    for element in code.body:
                        if isinstance(element, ast.Expr):
                            exec(compile(element.value, filename="<ast>", mode="exec"))
                        elif isinstance(element, ast.Assign):
                            exec(compile(element, filename="<ast>", mode="exec"))
                return output.capturedtext
            except Exception as e:
                return "Server Error: {}:".format(str(e))

        else:
            return redirect(request.url)
    return render_template('eval.html')












































































































































