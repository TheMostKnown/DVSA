from flask import Flask, render_template, redirect, request, flash
import sqlite3
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8e977ef74bf745ac153c117a2c9e76c6'

command_dict = [(" OR ",""), (" UNION ",""), (" AND ",""), 
                ("SELECT",""), (" or ",""), (" and ",""), 
                (" union ",""), (" select ",""), (" --",""), ("--","")]

def replace_comands(my_str):
    for x, y in command_dict:
        my_str = my_str.replace(x, y)
    return my_str

def create_database():
    # Connect to the database
    conn = sqlite3.connect('sqli.db')
    c = conn.cursor()
    # Create the users table
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT )')
    # Insert data into the users table
    c.execute('INSERT INTO users (login, password) VALUES ("admin", "TheStrongiestPassword")')
    # Save changes and close the connection

    c.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT )')
    c.execute('''INSERT INTO posts (title, content) VALUES 
              ("Hummingbirds can take over the world in a day!", "One of the smallest birds on earth is hummingbirds. \
              No one even knows what they are capable of. But the long observations of an ornithologist from Murmansk \
              led to unexpected conclusions. These birds are able to literally take over the whole world in a day, \
              but they are hindered by only one thing and that is..."),
              ("The strongiest password is found!", "Every day people live in search of a strong password. \
              Someone needs it for social networks, someone for a nuclear button. No one expected that the most \
              reliable password could exist, but scientists from Petrozavods State University were able to find it \
              and this password is..."),
              ("The new Ubuntu has lost its Python!", "A pet store intern from Kenya named Ubuntu did not keep track of \
              the enclosure where the python lives. And now this starved asp is terrorizing crocodiles living in the sewers  \
              of New York. Even mutated turtles are afraid of this creature. It's the size of it...")''')
    
    conn.commit()
    conn.close()

create_database()

def authVIP(login, password):

    conn = sqlite3.connect('sqli.db')
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM users WHERE login=\""+login+"\" AND password=\""+password+"\"")
    except Exception as e:
        flash(e, 'error')
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
        login = re.escape(replace_comands(login))

        password = request.form.get('password')
        password = replace_comands(password)

        if not authVIP(login, password):
            flash('There is not user like '+login, 'error')
            return (render_template('index_1.html'))

        return (render_template('flag.html', flag="sne{where_was_a_simple_replacing}"))
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