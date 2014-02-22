from flask import render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Nigel' } # A fake user
    posts = [
            {'author': {'nickname': 'John'},
             'body': 'Beautiful day in Portland!'
            },

            {
            'author': {'nickname': 'Susan'},
            'body': 'The Movie was so cool!'

            }
            ]

    return render_template("index.html",
            title= "Home",
            user=user,
            posts=posts)
