from flask import Flask,render_template

app = Flask(__name__)

posts=[
    {
        'author':'Sridhar',
        'title':'Post 1',
        'Content':'First Post',
        'date_posted':'July 28,2024'
    },
    {
        'author':'Unicourt',
        'title':'Post 2',
        'Content':'Second Post',
        'date_posted':'July 29,2024'
    }
]

@app.route('/')
def index():
    return render_template('home.html',posts=posts)


@app.route('/about')
def about():
    return render_template('about.html',title='About')


if __name__=='__main__':
    app.run(debug=True)