from flask import Flask, render_template, send_file, request

app = Flask(__name__)

flag_basic = "sne{y0u_570l3_my_53cr375}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_basic')
def get_basic():
    filename = request.args.get('file')
    if filename == 'secret.txt':
        return flag_basic
    else:
        return "File not found"


@app.route('/get_medium')
def get_medium():
    filename = request.args.get('file')
    if filename.endswith('.txt'):
        return send_file(filename)
    else:
        return "Invalid file type"


@app.route('/get_advanced')
def get_advanced():
    filename = request.args.get('file').replace("../","")
    print(filename)
    try:
        with open(f"templates/{filename}", 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


if __name__ == '__main__':
    app.run(debug=True)
