from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    team_members = [
    {'img':'boni.png',    'name':'Dr. Nderu',       'role':'Supervising Director',            'link':'https://linkedin.com/in/drnderu'},
    {'img':'robert.png',  'name':'Mr.Robert',       'role':'Mentor & AI Specialist',          'link':'https://www.linkedin.com/in/robert-ndungu/'},
    {'img':'mnisaa.jpg',  'name':'John Gitau',      'role':'UI/UX Designer',                  'link':'https://linkedin.com/in/brianotieno'},
    {'img':'boni.jpg',    'name':'Boniface Manda',  'role':'Security Analyst',                'link':'https://linkedin.com/in/boniface'},
    {'img':'layii.png',   'name':'Ruth Khalayi',    'role':'Data Scientist',                  'link':'https://linkedin.com/in/emanuel'},
    {'img':'manu.jpg',    'name':'Emanuel Mudasia', 'role':'Network Security Engineer',       'link':'https://linkedin.com/in/robert'},
    {'img':'joshua.jpg',  'name':'Joshua Mativo',   'role':'Model Trainer',                   'link':'https://linkedin.com/in/john'},
    {'img':'a1-lex.jpg',  'name':'Alex Maina',      'role':'Full-stack Developer',            'link':'https://www.linkedin.com/in/alex-maina'},
    {'img':'mato.jpg',    'name':'Martin',          'role':'Research & Documentation Lead',   'link':'https://linkedin.com/in/drnderu'},
]

    return render_template('index.html', team_members=team_members)

if __name__ == '__main__':
    app.run(debug=True)
