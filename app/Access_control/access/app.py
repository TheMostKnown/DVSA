from flask import Flask, render_template

app = Flask(__name__)

@app.route('/1/')
def access1_app():
    num = 1
    return (render_template('index_1.html', number=num))

@app.route('/2/')
def access2_app():
    num = 2
    return (render_template('index_2.html', number=num))

@app.route('/3/')
def access3_app():
    num = 3
    return (render_template('index_3.html', number=num))

if __name__ == 'main':
  app.run(debug=True, host='0.0.0.0', port=80)