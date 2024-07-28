from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['Secret_Key']="AintSecret"

posts=[
    {
        'author':'Sridhar',
        'title':'Post 1',
        'content':'First Post',
        'date_posted':'July 28,2024'
    },
    {
        'author':'Unicourt',
        'title':'Post 2',
        'content':'Second Post',
        'date_posted':'July 29,2024'
    }
]

@app.route('/')
def index():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title="About")

@app.route('/register')
def reg():
    form=RegistrationForm()
    return render_template('register.html',title='Register',form=form)

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html',title='Register',form=form)

if __name__ == "__main__":
    app.run(debug=True)
