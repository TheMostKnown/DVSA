from flask import Flask, request, render_template, make_response

app = Flask(__name__)

flag_easy = "sne{Th47_w4$_e@5y}"
flag_medium = "sne{b3773r_7h4n_my_Gr4ndm4}"
flag_hard = "sne{W3_r1ch}"


def is_blacklisted(url):
    blacklist = ['127.0.0.1', 'localhost', '192.168.0.1']
    for item in blacklist:
        if item in url:
            return True
    return False


def is_whitelisted(url):
    whitelist = ['example.com', 'api.example.com', 'google.com']
    for item in whitelist:
        if item in url:
            return True
    return False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first', methods=['GET', 'POST'])
def simple_ssrf():
    url = request.args.get('url')
    if url.startswith('http://ssrf.stsctf.sne/flag'):
        return render_template('flag.html', flag=flag_easy)
    else:
        return render_template('error.html', error="Access denied")


@app.route('/second', methods=['GET', 'POST'])
def local_file_ssrf():
    file_path = request.args.get('file')
    if '/flag/flag.txt' == file_path:
        try:
            with open('flag/flag.txt', 'r') as file:
                file_content = file.read()
                resp = make_response(render_template('flag.html', flag=file_content))
        except FileNotFoundError:
            file_content = 'File not found'
        return resp
    else:
        return render_template('error.html', error="FILE NOT FOUND")


@app.route('/third', methods=['GET'])
def black_white_lists():
    url = request.args.get('url')
    if url:
        if is_blacklisted(url):
            return render_template('error.html', error="Access denied. URL is blacklisted.")
        elif not is_whitelisted(url):
            return render_template('error.html', error="Access denied. URL is not whitelisted.")
        else:
            return render_template('flag.html', flag=flag_hard)
    else:
        return render_template('error.html', error="URL parameter is missing")


if __name__ == '__main__':
    app.run(debug=True)
