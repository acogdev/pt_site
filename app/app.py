from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'lyTYhtC55KCPXySD7z5JgOQebERcD93IfZENOSfTcghla87a9'


@app.route('/')
def home():
    return render_template('index.html')

def show_posts():
    posts = []
    for account in stormpath_manager.application.accounts:
        if account.custom_data.get('posts'):
            posts.extend(account.custom_data['posts'])

    posts = sorted(posts, key=lambda k: k['date'], reverse=True)
    return render_template('show_posts.html', posts=posts)


@app.route('/add', methods=['POST'])
@login_required
def add_post():
    if not user.custom_data.get('posts'):
        user.custom_data['posts'] = []

    user.custom_data['posts'].append({
        'date': datetime.utcnow().isoformat(),
        'title': request.form['title'],
        'text': request.form['text'],
    })
    user.save()

    flash('New post successfully added.')
    return redirect(url_for('show_posts'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        try:
            _user = User.from_login(
                request.form['email'],
                request.form['password'],
            )
            login_user(_user, remember=True)
            flash('You were logged in.')

            return redirect(url_for('show_posts'))
        except StormpathError, err:
            error = err.message

    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    logout_user()
    flash('You were logged out.')

    return redirect(url_for('show_posts'))



if __name__ == '__main__':
    app.run()