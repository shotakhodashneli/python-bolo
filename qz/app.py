from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schedule.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'quiz56'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


db.create_all()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']

        if username and password:
            check_user = User.query.filter_by(username=username).first()
            if check_user is not None:
                if check_user.password == password:
                    session['username'] = username
                    return redirect(url_for('profile'))
                else:
                    flash('პაროლი არასწორია.')
            else:
                flash('მომხმარებელი ვერ მოიძებნა.')

    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']

        if username and password:
            check_user = User.query.filter_by(username=username).first()
            if check_user is None:
                user = User(username=username, password=password)
                db.session.add(user)
                db.session.commit()
                session['username'] = username
                return redirect(url_for('profile'))
            else:
                flash('მომხმარებელი ამ იუზერნეიმით უკვე არსებობს.')
        else:
            flash('გთხოვთ შეავსოთ ფორმა.')

    return render_template('register.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
