import sys
import os
from flask import Flask, request, render_template

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from project2 import recommend_car  # ✅ Import the correct function

app = Flask(__name__)

# ✅ Updated main page to welcome.html
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/start')  # New route to start the car recommendation process
def start():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    price = float(request.form['price'])  # Convert price to float
    fuel_type = request.form['fuel_type']
    seller_type = request.form['seller_type']
    car_type = request.form['car_type']  # Updated from "owner_type"
    driving_experience = int(request.form['driving_experience'])  # ✅ Get driving experience
    low_maintenance = request.form['low_maintenance']  # ✅ Get low maintenance preference
    luxury_preference = request.form.get('luxury_car', 'No')  # ✅ Get luxury car preference (default to "No")

    # Map car_type selection to owner type
    if car_type == "New":
        owner_types = ["First Owner"]  # Only first-owner cars for new cars
    else:  # Used Car
        owner_types = ["Second Owner", "Third Owner", "Fourth & Above Owner"]

    # ✅ Determine transmission preference based on driving experience
    if driving_experience in [1, 2]:
        transmission_types = ["Automatic"]
    else:
        transmission_types = ["Automatic", "Manual"]

    # ✅ Pass transmission_types, low_maintenance & luxury_preference to the function
    recommended_cars = recommend_car(price, fuel_type, seller_type, owner_types, transmission_types, low_maintenance, luxury_preference)

    return render_template('result.html', cars=recommended_cars.to_dict(orient='records'))  # ✅ Convert DataFrame to list of dicts

# ✅ Adding the Contact Us Page Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
