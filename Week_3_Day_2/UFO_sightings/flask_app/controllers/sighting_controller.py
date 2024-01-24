from flask_app import app
from flask import Flask, render_template, request, redirect, session, flash
from flask_app.models.sighting_model import Sighting
from flask_app.models.user_model import User

#route that leads us to the create sighting page

@app.route('/sightings/new')
def create_new_sighting_page():
  print("hello I have reached this part in the app")
  if 'user_id' not in session:
    flash("You must be logged in to view this page")
    return redirect('/')
  
  
  return render_template("create_sighting.html")


# route that recieves form data from create sighting page

@app.route('/sightings/create', methods=["POST"])
def create_new_sighting():
  #we will recieve the data from request form: request.form['title'], request.form['description']
  
  data = {
    'user_id': session['user_id'],
    'title': request.form['title'],
    'description': request.form['description'],
    'location': request.form['location'],
    'date_seen': request.form['date_seen'],
    'abducted': request.form['abducted']
    
  }
  
  if not Sighting.validate_sighting(request.form):
      return redirect('/sightings/new')
  
  Sighting.create_sighting(data)
  return redirect('/sightings')
  
# route to read one sighting
@app.route('/sightings/<int:id>')
def show_one_sighting(id):
  if 'user_id' not in session:
    flash("You must be logged in to view this page")
    session.clear()
    return redirect('/')
  
  data = {
    'id': id
    }
  
  current_user = User.get_user_by_id({'user_id': session['user_id']})
  
  
  
  
  sighting = Sighting.read_one_sighting(data)
  
  return render_template('read_one_sighting.html', sighting = sighting, current_user = current_user)


# route to the edit one sighting page

@app.route('/sightings/edit/<int:id>')
def edit_one_page(id):
  if 'user_id' not in session:
    flash('You must be logged in to view this page')
    session.clear()
    return redirect('/')
  data = {
    "id":id
  }
  
  sighting = Sighting.read_one_sighting(data)
  
  return render_template('edit_sighting.html', sighting=sighting)

# route to edit the one sighting we are currently viewing

@app.route('/sightings/update', methods=['POST'])
def edit_sighting():
  
  data = {
    'id' : request.form['id'],
    'user_id': session['user_id'],
    'title' : request.form['title'],
    'description' : request.form['description'],
    'location' : request.form['location'],
    'date_seen': request.form['date_seen'],
    'abducted': request.form['abducted']
  }
  id = request.form['id']
  
  if not Sighting.validate_sighting(request.form):
    # print("------------------hello we reached line 95 in sighting controller-----------------")
      return redirect(f'/sightings/edit/{id}')
    
  Sighting.update_sighting(data)
  
  return redirect('/sightings')

# DELETE route to remove a Sighting

@app.route('/sightings/delete/<int:sighting_id>')
def delete_sighting(sighting_id):
  if 'user_id' not in session:
    flash('You must be logged in')
    session.clear()
    return redirect('/')
    this_sighting  = {
      'id': sighting_id
    }
    Sighting.delete_sighting(this_sighting)

    return redirect('/sightings')