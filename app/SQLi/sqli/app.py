from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def sqli_index():
    return (render_template("index.html" ))

@app.route('/1/')
def sql1_app():
    num = 1
    return (render_template('index_1.html', number=num))

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