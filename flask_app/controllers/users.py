from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.tvshow import Tvshow
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route('/register/user', methods=['POST'])
def register():
    # validate the form here ...
    if not User.validate_user(request.form):
        # redirect to the route 
        return redirect('/')
    # create the hash
    pw_hash = bcrypt.generate_password_hash(request.form['pwd'])
    print(pw_hash)
    # put the pw_hash into the data dictionary
    
    data = {
            **request.form, 'pwd':pw_hash
        }
    # Call the save @classmethod on User
    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/shows")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password","login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['pwd']):
        # if we get False after checking the password
        flash("Invalid Email/Password","login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    
    return redirect("/shows")

@app.route("/shows")
def user_show():
    if 'user_id' not in session:
        return redirect ("/")
    user_to_show = User.get_one({'id':session['user_id']})
    all_tvshows = Tvshow.get_all_tvshows()
    user_likes=Tvshow.get_all_user_likes({'id':session['user_id']})
    print('user likes',user_likes)
    return render_template("shows.html",user=user_to_show,tvshows=all_tvshows,user_likes=user_likes,liked='unlike')
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
