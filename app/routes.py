from app import app
from flask import render_template


# add routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sports')
def sports():
    sports = ['Basketball', 'Baseball', 'Football', 'Chess', 'Karate']
    return render_template('sports.html', sports=sports)

@app.route('/food')
def food():
    food = ['Chicken Sandwich', 'Tacos', 'Jerk Chicken', 'BBQ Bacon Burger', 'Mac & Cheese']
    return render_template('food.html', food=food)

@app.route('/hobbies')
def hobbies():
    hobbies = ['Coding', 'Gaming', 'Fitness', 'Editing', 'Drawing']
    return render_template('hobbies.html', hobbies=hobbies)

@app.route('/videogames')
def videogames():
    games = ['Battlefield', 'Diablo', 'Modern Warfare', 'PUBG', 'League Of Legends']
    return render_template('videogames.html', games=games)