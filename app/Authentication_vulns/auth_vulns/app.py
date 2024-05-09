from flask import Flask, request, make_response

app = Flask(__name__)
FLAG = "cne{bru73_br0}"
FLAG_2 = "CTF{cookie_vuln}"


@app.route('/login', methods=['POST'])
def login():
    password = request.form.get('password')
    if password == "pass":
        return "Login successful! Here is your flag: " + FLAG
    else:
        return "Incorrect password."


@app.route('/login', methods=['GET'])
def admin():
    login = request.args.get('login')
    password = request.args.get('password')
    print( login, password)
    if login == 'admin' and password == '1234qwer':
        resp = make_response("Login successful!")
        resp.set_cookie('admin', 'True')
        return resp
    else:
        return 'Incorrect login'


@app.route('/flag', methods=['GET'])
def get_flag():
    if request.cookies.get('admin') == 'True':
        return "Here is your flag: " + FLAG_2
    else:
        return "Access denied."


if __name__ == '__main__':
    app.run()
