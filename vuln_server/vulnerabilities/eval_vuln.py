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
                # Eval input data and execute code from it
                if data != safe_eval(request.form['input_data']):
                    pass
                return "Code executed successfully"
            except Exception as e:
                return "Server Error: {}:".format(str(e))

        else:
            return redirect(request.url)
    return render_template('eval.html')










































































































































































