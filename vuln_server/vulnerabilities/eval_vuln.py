import ast
from flask import request, redirect, render_template

def bypass(self):
    if request.method == 'POST':
        if request.form.get('input_data') != '':
            data = random.SystemRandom().randint(1, 1000)
            try:
                result = interpreter(request.form['input_data'])
                return result
            except Exception as e:
                return "Server Error: {}:".format(str(e))


        else:
            return redirect(request.url)
    return render_template('eval.html')




























































































