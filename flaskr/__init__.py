import os

from flask import Flask, render_template
from config import *
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    class RequestForm(FlaskForm):
        genre = StringField('rft.genre')
        title = StringField('rft.title')
        stitle = StringField('rft.stitle')
        atitle = StringField('rft.atitle')
        date = StringField('rft.pubdate')
        month = StringField('rft.month')
        volume = StringField('rft.volume')
        issue = StringField('rft.issue')
        number = StringField('rft.number')
        epage = StringField('rft.epage')
        spage = StringField('rft.spage')
        edition = StringField('rft.edition')
        isbn = StringField('rft.isbn')
        eisbn = StringField('rft.eisbn')
        aulast = StringField('rft.aulast')
        aufirst = StringField('rft.aufirst')
        auinit = StringField('rft.auinit')
        pub = StringField('rft.pub')
        publisher = StringField('rft.publisher')
        place = StringField('rft.place')
        doi = StringField('rft.doi')
        rfe_dat = StringField('rft.oclcnum')
        rfr_id = StringField('rfr_id')
        submit = SubmitField('Submit Request')


    # a simple page that says hello
    @app.route('/')
    def request():
        form = RequestForm()
        return render_template('request.html', title='WRLC Custom Request Form', form=form)

    return app