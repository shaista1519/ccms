from flask import Flask, render_template, url_for, redirect, flash
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter-the-worst-password'

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "Test" and form.password.data == "test":
            flash(f'Welcome {form.username.data}', 'success')
            return redirect(url_for('index'))
        else:
            flash('Username or Password is incorrect', 'danger')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)