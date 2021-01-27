import os

from flask import Flask, render_template, request as req
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
        rft_genre = StringField('rft.genre')
        rft_title = StringField('rft.title')
        rft_stitle = StringField('rft.stitle')
        rft_atitle = StringField('rft.atitle')
        rft_date = StringField('rft.pubdate')
        rft_month = StringField('rft.month')
        rft_volume = StringField('rft.volume')
        rft_issue = StringField('rft.issue')
        rft_number = StringField('rft.number')
        rft_epage = StringField('rft.epage')
        rft_spage = StringField('rft.spage')
        rft_edition = StringField('rft.edition')
        rft_isbn = StringField('rft.isbn')
        rft_eisbn = StringField('rft.eisbn')
        rft_aulast = StringField('rft.aulast')
        rft_aufirst = StringField('rft.aufirst')
        rft_auinit = StringField('rft.auinit')
        rft_pub = StringField('rft.pub')
        rft_publisher = StringField('rft.publisher')
        rft_place = StringField('rft.place')
        rft_doi = StringField('rft.doi')
        rfe_dat = StringField('rft.oclcnum')
        rfr_id = StringField('rfr_id')
        submit = SubmitField('Submit Request')

    # a simple page that says hello
    @app.route('/')
    def request():
        form = RequestForm()
        # TODO: Parse URL params and pre-populate form fields
        query = req.args
        for k, v in query.items():
            k = k.replace('.', '_')
            if k == 'rft_au':
                au = v.split(',')
                aulast = au[0]
                aufirst = au[1]
                form.rft_aulast.data = aulast
                form.rft_aufirst.data = aufirst
            else:
                form[k].data = v

        return render_template('request.html', title=query, form=form)

    return app
