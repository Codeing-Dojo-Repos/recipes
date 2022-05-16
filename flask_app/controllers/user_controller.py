from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.users_model import User
from flask_app.models.recipes_model import Recipes
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/handleRegistration', methods=['POST'])
def handleRegistration():
    is_valid=True
    if not User.validata_fname(request.form['fname']):
        is_valid = False
    if not User.validata_lname(request.form['lname']):
        is_valid = False
    if not User.validata_email(request.form['email']):
        is_valid = False
    if not User.validata_password(request.form['password'], request.form['cpassword']):
        is_valid = False
    if not request.form['password'] == request.form['cpassword']:
        is_valid = False
    if is_valid == False:
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'fname':request.form['fname'],
        'lname':request.form['lname'],
        'email':request.form['email'],
        'password':pw_hash  #request.form['password']
    }
    user_id = User.insert(data)
    session['user_id'] = user_id
    return redirect('/success')

@app.route('/success', methods=['GET'])
def success():
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        'id': session['user_id']
    }
    result = User.get_user_by_id(data)
    recipes = Recipes.get_all_by_user_id(data)
    return render_template('success.html', user=result, recipes=recipes)

@app.route('/handleLogin', methods=['POST'])
def handleLogin():
    is_valid=True
    # grab the user info in the db by the email addy
    print("trying to login: " + request.form['email'])
    data = {
        'email':request.form['email'] 
    }
    user_info = User.get_user_by_email(data)
    if not user_info:
        print('user not found!')
        flash('invalid user', 'log')
        return redirect('/')
    
    # verify the passwords hashes match
    if not bcrypt.check_password_hash(user_info[0]['password'], request.form['password']):
        flash('invalid password', 'log')
        return redirect('/')
    # if they match, save user in session
    session['user_id'] = user_info[0]['id']
    #else print an error 
    return redirect('/success')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
