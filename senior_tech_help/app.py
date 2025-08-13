import os
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, request as flask_request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length


def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
	app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///senior_tech_help.db')
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	return app


app = create_app()
db = SQLAlchemy(app)


class HelpRequest(db.Model):
	__tablename__ = 'help_requests'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), nullable=False)
	email = db.Column(db.String(255), nullable=False)
	phone = db.Column(db.String(50), nullable=True)
	topic = db.Column(db.String(120), nullable=False)
	description = db.Column(db.Text, nullable=False)
	status = db.Column(db.String(50), nullable=False, default='open')
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class VolunteerOffer(db.Model):
	__tablename__ = 'volunteer_offers'
	id = db.Column(db.Integer, primary_key=True)
	request_id = db.Column(db.Integer, db.ForeignKey('help_requests.id'), nullable=False)
	volunteer_name = db.Column(db.String(120), nullable=False)
	volunteer_email = db.Column(db.String(255), nullable=False)
	message = db.Column(db.Text, nullable=True)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	help_request = db.relationship('HelpRequest', backref=db.backref('offers', lazy=True))


TOPIC_CHOICES = [
	('smartphone', 'Smartphone'),
	('computer', 'Computer'),
	('internet', 'Internet & Wi‑Fi'),
	('apps', 'Apps & Accounts'),
	('security', 'Security & Privacy'),
	('other', 'Other'),
]


class SeniorRequestForm(FlaskForm):
	name = StringField('Your name', validators=[DataRequired(), Length(max=120)])
	email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
	phone = StringField('Phone (optional)', validators=[Length(max=50)])
	topic = SelectField('Topic', choices=TOPIC_CHOICES, validators=[DataRequired()])
	description = TextAreaField('How can we help?', validators=[DataRequired(), Length(max=5000)])
	submit = SubmitField('Submit request')


class VolunteerOfferForm(FlaskForm):
	volunteer_name = StringField('Your name', validators=[DataRequired(), Length(max=120)])
	volunteer_email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
	message = TextAreaField('Message to the senior (optional)', validators=[Length(max=2000)])
	submit = SubmitField('Offer help')


@app.route('/')
def home():
	open_requests = HelpRequest.query.filter_by(status='open').order_by(HelpRequest.created_at.desc()).all()
	return render_template('home.html', open_requests=open_requests)


@app.route('/request', methods=['GET', 'POST'])
def create_request():
	form = SeniorRequestForm()
	if form.validate_on_submit():
		help_request = HelpRequest(
			name=form.name.data,
			email=form.email.data,
			phone=form.phone.data,
			topic=form.topic.data,
			description=form.description.data,
		)
		db.session.add(help_request)
		db.session.commit()
		flash('Your request has been submitted. Volunteers will get in touch directly via your email or phone.', 'success')
		return redirect(url_for('home'))
	return render_template('create_request.html', form=form)


@app.route('/request/<int:request_id>', methods=['GET', 'POST'])
def view_request(request_id: int):
	help_request = HelpRequest.query.get_or_404(request_id)
	form = VolunteerOfferForm()
	if form.validate_on_submit():
		offer = VolunteerOffer(
			request_id=help_request.id,
			volunteer_name=form.volunteer_name.data,
			volunteer_email=form.volunteer_email.data,
			message=form.message.data,
		)
		db.session.add(offer)
		db.session.commit()
		flash('Thanks for offering help! The senior can see your contact info here.', 'success')
		return redirect(url_for('view_request', request_id=help_request.id))
	return render_template('view_request.html', help_request=help_request, form=form)


@app.route('/request/<int:request_id>/close', methods=['POST'])
def close_request(request_id: int):
	help_request = HelpRequest.query.get_or_404(request_id)
	help_request.status = 'closed'
	db.session.commit()
	flash('This request has been closed.', 'info')
	return redirect(url_for('home'))


@app.cli.command('init-db')
def init_db_command():
	"""Initialize the database."""
	db.create_all()
	print('Initialized the database.')


if __name__ == '__main__':
	with app.app_context():
		db.create_all()
	app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)