from flask_app import app
from flask import render_template,redirect,request,session,flash,jsonify
from flask_app.models.tvshow import Tvshow
from flask_app.models.user import User


# new tv show
@app.route('/tvshow/new')
def new_tvshow():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_one({'id':session['user_id']})   
    return render_template("new_tvshow.html",user=user) 

# tv show create    
@app.route('/tvshow/create', methods=['POST'])
def create_tvshow():
    # validate the form here ...
    if not Tvshow.validate_tvshow(request.form):
        # redirect to tv show creation 
        return redirect('/tvshow/new')
    # Call the save @classmethod on Recipe
    Tvshow.save_tvshow(request.form)
    return redirect("/shows")

# tv show delete
@app.route('/tvshow/delete/<int:tvshow_id>')
def delete_tvshow(tvshow_id):
    data = {'id':tvshow_id}
    Tvshow.delete_tvshow(data)
    return redirect("/shows")

# tv show edit
@app.route('/shows/edit/<int:tvshow_id>')
def edit_tvshow(tvshow_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {'id':tvshow_id}
    tvshow=Tvshow.get_one_tvshow(data)
    return render_template("edit_tvshow.html",tvshow=tvshow) 

# tv show update
@app.route('/tvshow/update', methods=['POST'])
def update_tvshow():
    if not Tvshow.validate_tvshow(request.form):
        data = {'id':request.form['id']}
        tvshow=Tvshow.get_one_tvshow(data)
        # return to tv show edit
        return render_template("edit_tvshow.html",tvshow=tvshow)  
        
    Tvshow.update_tvshow(request.form)
    return redirect("/shows")

# Add like or remove like from likes table
@app.route('/tvshow/like', methods=['POST'])
def like_tvshow():
    data = request.json
    Tvshow.tvshow_like(data)
    return redirect("/shows")

@app.route('/tvshow/unlike', methods=['POST'])
def unlike_tvshow():  
    data = request.json
    Tvshow.tvshow_unlike(data)
    return redirect("/shows")

# Show tv show
@app.route('/tvshows/<int:tvshow_id>')
def show_tvshow(tvshow_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {'id':tvshow_id}
    tvshow=Tvshow.get_one_tvshow(data)
    nb_liked=Tvshow.get_number_of_likes(data)
    user = User.get_one({'id':session['user_id']})
    return render_template("show_tvshow.html",tvshow=tvshow,user=user,nb_liked=nb_liked) 


