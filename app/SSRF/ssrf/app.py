from flask import Flask, request, render_template

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


@app.route('/first')
def simple_ssrf():
    url = request.args.get('url')
    if url.startswith('http://simple_ssrf/flag'):
        return render_template('flag.html', flag=flag_easy)
    else:
        return "Access denied"


@app.route('/second')
def local_file_ssrf():
    file_path = request.args.get('file')
    if 'etc/passwd' in file_path:
        return render_template('flag.html', flag=flag_medium)
    else:
        return "Access denied"


@app.route('/third')
def black_white_lists():
    url = request.args.get('url')
    if url:
        if is_blacklisted(url):
            return "Access denied. URL is blacklisted."
        elif not is_whitelisted(url):
            return "Access denied. URL is not whitelisted."
        else:
            return render_template('flag.html', flag=flag_hard)
    else:
        return "URL parameter is missing."


if __name__ == '__main__':
    app.run(debug=True)
