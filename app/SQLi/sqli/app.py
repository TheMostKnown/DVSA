from flask import Flask, render_template, redirect, request, flash
import sqlite3
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8e977ef74bf745ac153c117a2c9e76c6'

command_dict = [(" OR ",""), (" UNION ",""), (" AND ",""), 
                ("SELECT",""), (" or ",""), (" and ",""), 
                (" union ",""), (" select ",""), (" --","")]

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
    conn.commit()
    c.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT, content TEXT )')
    conn.commit()
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
    c.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, link TEXT, title TEXT, category TEXT )')
    conn.commit()
    c.execute('''INSERT INTO items (link, title, category) VALUES 
              ("NaN"," You got a secret!","hidden"),
              ("https://thecichlidstage.com/wp-content/uploads/2017/12/fish-bandaged.jpeg","You can get a fish","fish"),
              ("https://s.mxmcdn.net/images-storage/albums/3/1/9/2/2/7/29722913_800_800.jpg","This girl is on fire!!!","fire"),
              ("https://i.pinimg.com/736x/e9/d1/25/e9d125637730d936152ed6086e9d4d26.jpg","Get lost in three birches","tree"),
              ("https://sun9-42.userapi.com/impf/c631628/v631628524/1538e/okaU89SYv4s.jpg?size=511x511&quality=96&sign=df72c5ae8e39664ea18c19e34c30e0d4&c_uniq_tag=UDZREl9NzQTyupCu5iVn5m8d1W-39zaylbUI64U275E&type=album","The king of rock","rock"),
              ("https://www.clipartmax.com/png/full/61-615148_present-clip-art-free-december-birthday-clip-art.png", "A gift for you", "gift"),
              ("https://get.wallhere.com/photo/anime-night-Moon-light-shape-737997.jpg","The dark moon","moon") ''')
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

def getArticles(search_str):
    conn = sqlite3.connect('sqli.db')

    c = conn.cursor()
    try:
        if not search_str:
            c.execute("SELECT title, content FROM posts")
        else:
            c.execute("SELECT title, content FROM posts WHERE content LIKE \"%" + search_str+"%\"" )
    except Exception as e:
        flash(e, 'error')
    results = c.fetchall()
    conn.close()
    return results

def getItems(search_str):
    conn = sqlite3.connect('sqli.db')
    c = conn.cursor()
    if search_str=="all":
        search_str=""
    try:
        if not search_str:
            c.execute("SELECT link, title, category FROM items WHERE category<>'hidden'")
        else:
            c.execute("SELECT link, title, category FROM items WHERE category=\"" + search_str+"\"" )
    except Exception as e:
        flash(e, 'error')
    results = c.fetchall()
    conn.close()
    return results


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

        return (render_template('flag.html', flag="sne{where_was_@_simple_replacing}"))
    else:
        return (render_template('index_1.html'))


@app.route('/2/second', methods=['GET', 'POST'])
def sql2_app():
    article = []
    if request.method == 'POST':
        article = getArticles(request.form.get('search'))
        for x in article:
            if "TheStrongiestPassword" in x:
                return (render_template('flag.html', flag="sne{uNiOn_request_is_@_bug}"))
    else:
        article = getArticles("")

    return (render_template('index_2.html', articles=article))

@app.route('/3/third', methods=['GET', 'POST'])
def sql3_app():
    items = []
    if request.method == 'POST':
        items = getItems(request.form.get('category'))
        for x in items:
            if "hidden" in x:
                return (render_template('flag.html', flag="sne{buttons_@re_not_secure}"))
    else:
        items = getItems("")

    return (render_template('index_3.html', items=items))


if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0', port=80)
