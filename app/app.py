from flask import (
    Flask,
    render_template,
)


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'lyTYhtC55KCPXySD7z5JgOQebERcD93IfZENOSfTcghla87a9'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/invitations')
def invitations():
    pass


@app.route('/aboutus')
def aboutus():
    pass


def show_posts():
    posts = []

    posts = sorted(posts, key=lambda k: k['date'], reverse=True)
    return render_template('show_posts.html', posts=posts)


if __name__ == '__main__':
    app.run()
