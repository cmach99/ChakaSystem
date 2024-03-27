from flask import Flask, render_template, request
import personalized_meal_recommendations as recommender

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        # Collecting input from the form
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        age = int(request.form['age'])
        gender = request.form['gender'].upper()
        activity_level = request.form['activity_level'].lower()
        goal = request.form['goal'].lower()
        preferred_cuisine = request.form['preferred_cuisine'].lower()
        preferred_diet_type = request.form['preferred_diet_type'].lower()
        
        # Processing the recommendations using the provided data
        recommendations = recommender.get_recommendations(weight, height, age, gender, activity_level, goal, preferred_cuisine, preferred_diet_type)
        
        # Sending the recommendations to the result page
        return render_template('result.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
