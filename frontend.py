
from flask import Flask, request, render_template
import sqlite3
from app import add_seasonal_flavor, update_ingredient, add_customer_suggestion, create_tables

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_flavor', methods=['POST'])
def add_flavor():
    name = request.form['name']
    season = request.form['season']
    add_seasonal_flavor(name, season)
    return "Flavor added successfully!"


@app.route('/update_ingredient', methods=['POST'])
def update_flavor_ingredient():
    name = request.form['name']
    quantity = request.form['quantity']
    update_ingredient(name, quantity)
    return "Ingredient updated successfully!"


@app.route('/add_suggestion', methods=['POST'])
def add_suggestion():
    customer_name = request.form['customer_name']
    suggested_flavor = request.form['suggested_flavor']
    allergy_concern = request.form['allergy_concern']
    add_customer_suggestion(customer_name, suggested_flavor, allergy_concern)
    return "Customer suggestion added successfully!"



@app.route('/view_flavors')
def view_flavors():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, season FROM flavors")
    flavors = cursor.fetchall()
    conn.close()

    
    flavors_list = [{'id': flavor[0], 'name': flavor[1], 'season': flavor[2]} for flavor in flavors]

    return render_template('flavors.html', flavors=flavors_list)

@app.route('/view_ingredients')
def view_ingredients():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, quantity FROM ingredients")
    ingredients = cursor.fetchall()
    conn.close()

    
    ingredients_list = [{'id': ingredient[0], 'name': ingredient[1], 'quantity': ingredient[2]} for ingredient in ingredients]

    return render_template('ingredients.html', ingredients=ingredients_list)



@app.route('/view_suggestions')
def view_suggestions():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT customer_name, suggested_flavor, allergy_concern, suggestion_date FROM customer_suggestions")
    suggestions = cursor.fetchall()
    conn.close()

   
    suggestions_list = [{'customer_name': suggestion[0], 
                         'suggested_flavor': suggestion[1], 
                         'allergy_concern': suggestion[2], 
                         'suggestion_date': suggestion[3]} for suggestion in suggestions]

    return render_template('suggestions.html', suggestions=suggestions_list)


if __name__ == '__main__':
    create_tables()  
    app.run(debug=True)
