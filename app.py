from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    team_members = [
        {'img':'boni.png',    'name':'Alex Muriithi',  'role':'Project Lead & AI Engineer',      'link':'https://linkedin.com/in/alexmuriithi'},
        {'img':'boni.png',    'name':'Faith Njeri',    'role':'Network Security Specialist',     'link':'https://linkedin.com/in/faithnjeri'},
        {'img':'brian.png',   'name':'Brian Otieno',   'role':'Backend & Deployment Engineer',   'link':'https://linkedin.com/in/brianotieno'},
        {'img':'boniface.png','name':'Boniface',       'role':'Security Analyst',                'link':'https://linkedin.com/in/boniface'},
        {'img':'emanuel.png', 'name':'Emanuel',        'role':'Data Scientist & Model Trainer',  'link':'https://linkedin.com/in/emanuel'},
        {'img':'robert.png',  'name':'Robert',         'role':'Mentor & Project Guide',          'link':'https://linkedin.com/in/robert'},
        {'img':'john.png',    'name':'John',           'role':'UI/UX Designer',                  'link':'https://linkedin.com/in/john'},
        {'img':'kelvin.png',  'name':'Kelvin',         'role':'Network Security Analyst',        'link':'https://linkedin.com/in/kelvin'},
        {'img':'nderu.png',   'name':'Dr. Nderu',      'role':'Supervising Director',            'link':'https://linkedin.com/in/drnderu'},
    ]
    return render_template('index.html', team_members=team_members)

if __name__ == '__main__':
    app.run(debug=True)
