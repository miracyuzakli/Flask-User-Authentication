from app import app, db, login_manager
from app.forms import RegisterForm, LoginForm
from app.models import Users

from flask import Flask, flash, render_template, redirect, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user, user_logged_in


from flask_login import LoginManager, UserMixin


@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(int(user_id)).first()



@app.route("/")
def index():


    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        if not (form.password.data == form.confirmPassword.data):
                    
            flash('Passwords do not match.')

            return render_template('register.html', form=form)

        else:
            hashed_password = generate_password_hash(
                form.password.data, method='sha256')

            new_user = Users(username=form.username.data,
                            email=form.email.data,
                            firstname=form.firstname.data,
                            lastname=form.lastname.data,
                            password=hashed_password)
            
            db.session.add(new_user)
            db.session.commit()

            flash('Your registration has been successfully completed! Please login.')

            return redirect(url_for('login'))


    return render_template("register.html", form = form)



@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Invalid email or password')

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


