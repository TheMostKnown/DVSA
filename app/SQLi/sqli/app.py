from flask import Flask, render_template, redirect, request, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = '8e977ef74bf745ac153c117a2c9e76c6'

def create_database():
    # Connect to the database
    conn = sqlite3.connect('sqli.db')
    c = conn.cursor()

    # Create the users table
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT )')

    # Insert data into the users table
    c.execute('INSERT INTO users (login, password) VALUES ("admin", "TheStrongiestPassword")')

    # Save changes and close the connection
    conn.commit()
    conn.close()

create_database()

def authVIP(login, password):

    conn = sqlite3.connect('sqli.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE login=? AND password=?", (login, password))
    results = c.fetchall()
    conn.close()

    return not not results

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
        if not authVIP(login, password):
            flash('There is not user like '+login, 'error')
            return (render_template('index_1.html'))

        return (render_template('flag.html', flag="sne{where_was_a_simple_shielding}"))
    else:
        return (render_template('index_1.html'))


@app.route('/2/second')
def sql2_app():
    num = 2
    return (render_template('index_2.html', number=num))

@app.route('/3/third')
def sql3_app():
    num = 3
    return (render_template('index_3.html', number=num))


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0', port=80)