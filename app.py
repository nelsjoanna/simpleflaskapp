from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

#create variable Articles and set it to that Articles function
Articles = Articles()

#create route in Flask
@app.route('/')
def home():
    return render_template('home.html')

#add the About route
@app.route('/about')
def about():
    return render_template('about.html')

#create the Articles route and pass in the data
@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)


if __name__ == '__main__':
    app.run(debug=True)
