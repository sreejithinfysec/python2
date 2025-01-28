import ast
from flask import request, redirect, render_template
import random

def bypass(self):
    if request.method == 'POST':
        # Check if data is not empty, post forms has all params defined
        # which may be empty and cause unexpected behaviour.
        if request.form.get('input_data') != '':
            # Whitelist of allowed characters
            allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/() ')
            # Check if input data contains only allowed characters
            if set(request.form['input_data']).issubset(allowed_chars):
                try:
                    # Eval input data and execute code from it
                    result = eval(request.form['input_data'])
                    return "Code executed successfully"
                except Exception as e:
                    return "Server Error: {}:".format(str(e))
            else:
                return "Invalid input data"
        else:
            return redirect(request.url)
    return render_template('eval.html')























































































































































































