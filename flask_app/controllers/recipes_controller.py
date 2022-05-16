from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.recipes_model import Recipes



@app.route('/new')
def new():
    print('found new recipe route')
    return render_template('new.html')

@app.route('/createRecipe', methods=['POST'])
def createRecipe():
    #print(f"form: {request.form}")
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instructions": request.form['instructions'],
        "thirty_min": request.form['thirty_min'],
        "date_name": request.form['date_name'],
        "users_id": session["user_id"]
    }
    id = Recipes.create(data)
    return redirect(f'/recipe/{id}')

@app.route('/recipe/<int:id>')
def showRecipe(id):
    print('in showRecipe route')
    # get recipe by id
    data = { "id": id}
    result = Recipes.get_by_recipe_id(data)
    return render_template('showRecipe.html', recipe=result)