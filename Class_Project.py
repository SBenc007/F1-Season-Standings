from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

class FetchForm(FlaskForm):
    season = StringField('Season', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def fetch():
    form = FetchForm()
    if form.validate_on_submit():
        season = form.season.data
        return f1_driver_standings(season)
    return render_template('fetch.html', form=form)


def f1_driver_standings(season):
    url = f'http://ergast.com/api/f1/{season}/driverStandings.json'
    response = requests.get(url)
    standings = response.json()
    return render_template('standings.html', standings=standings)


if __name__ == '__main__':
    app.run(debug=True)