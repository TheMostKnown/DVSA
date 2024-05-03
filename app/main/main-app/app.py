from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_app():
    return (render_template('index.html'))

if __name__ == 'main':
  app.run(debug=True, host='0.0.0.0', port=80)