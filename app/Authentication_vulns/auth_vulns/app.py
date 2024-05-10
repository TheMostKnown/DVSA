from flask import Flask, request, make_response, render_template

app = Flask(__name__)
FLAG_1 = "cne{bru73_br0}"
FLAG_2 = "cne{1_l0v3_3471n6_c00k135}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    login = request.form.get('login')
    password = request.form.get('password')
    print(login, password)
    if login == "Bob" and password == "pass":
        return render_template('flag.html', flag=FLAG_1)
    elif login == 'admin' and password == '1234qwer':
        resp = make_response(render_template('success.html'))
        resp.set_cookie('admin', 'True')
        return resp
    else:
        return render_template('login.html')


@app.route('/flag', methods=['GET'])
def get_flag():
    if request.cookies.get('admin') == 'True':
        return render_template('flag.html', flag=FLAG_2)
    else:
        return render_template('fail.html')


if __name__ == '__main__':
    app.run()
