from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('skeleton.html')


@app.route('/about')
def about():
    return render_template('public/about.html')

@app.route('/contact')
def contact():
    return render_template('public/contact.html')

@app.route('/birthday')
def birthday():
    return render_template('public/birthday-invite.html')

@app.route('/movie')
def movie():
    return render_template('public/movie-ranking.html')



if __name__ == '__main__':
    app.run(debug=True)



