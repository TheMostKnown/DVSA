from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def sqli_index():
    return (render_template("index.html" ))

@app.errorhandler(404)
def page_not_found(e):
    return redirect("/", code=302)

@app.route('/1/first', methods=['GET', 'POST'])
def sql1_app():
    if request.method == 'POST':
        login = request.form.get('username')
        password = request.form.get('password')

        return (render_template('flag.html', flag="sne{where_was_a_simple_shielding}"))
    else:
        return (render_template('index_1.html'))

@app.route('/2/')
def sql2_app():
    num = 2
    return (render_template('index_2.html', number=num))

@app.route('/3/')
def sql3_app():
    num = 3
    return (render_template('index_3.html', number=num))

if __name__ == 'main':
  app.run(debug=True, host='0.0.0.0', port=80)