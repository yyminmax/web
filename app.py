from flask import Flask, make_response, render_template, url_for, session, redirect
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
	name = StringField('What is your name?', validators=[Required()])
	submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
	#name = None
	form = NameForm()
	if(form.validate_on_submit()):
		old_name = session.get('name')
		if(old_name is not None and old_name != form.name.data):
			flash('Maybe you have a new name.')
		session['name'] = form.name.data
		return redirect(url_for('index'))
	return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template('500.html'), 500

if(__name__ == '__main__'):
	manager.run()
