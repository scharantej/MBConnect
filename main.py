
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mbti_type = request.form['mbti_type']
        engineer_specialty = request.form['engineer_specialty']
        session['mbti_type'] = mbti_type
        session['engineer_specialty'] = engineer_specialty
        return redirect(url_for('results'))
    return render_template('index.html')

@app.route('/results')
def results():
    mbti_type = session['mbti_type']
    engineer_specialty = session['engineer_specialty']
    # Query database or API for potential matches based on MBTI type and engineer specialty
    potential_matches = ['Match 1', 'Match 2', 'Match 3']
    return render_template('results.html', potential_matches=potential_matches)

if __name__ == '__main__':
    app.run(debug=True)
