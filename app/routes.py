from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gast'}
    posts = [
        {
            'author': {'username': 'Paul'},
            'body': 'Was fuer ein Tag!'
        },
        {
            'author': {'username': 'Miriam'},
            'body': 'Das Wetter ist gut!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=
        posts)