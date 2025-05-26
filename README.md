# ChakaSystem
# The Chaka Dietary Recommendation System 
*Personalised dietary recommendations powered by neural networks*

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12+-orange)](https://www.tensorflow.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.2+-blue)](https://scikit-learn.org/)

## Key Features
- **Personalised Calorie Calculation** using Harris-Benedict equation with activity level adjustments
- **Neural Network Classifier** (64-32-1 architecture) with K-Fold Cross Validation
- **Smart Meal Grading System** (1-5 stars) based on nutritional density
- **Multi-Factor Filtering** (cuisine, diet type, health goals)
- **Robust Feature Engineering** with One-Hot Encoding & Min-Max Scaling

## Tech Stack
```python
- TensorFlow 2.12 | scikit-learn 1.2 | pandas 2.0 | NumPy 1.24
- ML Techniques: Deep Neural Networks, Cross Validation, Feature Engineering
- Health Calculations: BMR, TDEE, Goal-oriented calorie targets
```

## Getting Started

### Installation
```bash
pip install -r requirements.txt

```
### Example Usage
```python
recommendations = get_recommendations(
    weight=70,          # kg
    height=175,         # cm
    age=30,
    gender='M',
    activity_level='moderate',
    goal='lose weight',
    preferred_cuisine='mediterranean',
    preferred_diet_type='balanced'
)
```

### Sample Output
```json
[
  {
    "Recipe_name": "Grilled Chicken Salad",
    "Cuisine_type": "Mediterranean",
    "Diet_type": "Balanced",
    "TotalCalories": "450.00",
    "HealthGrade": "5 stars - Very Healthy"
  },
  ...
]
```

## System Architecture
1. **Data Pipeline**  
   `Feature Engineering → Encoding/Normalisation → Cross Validation Split`

2. **Neural Network Model**  
   ```python
   tf.keras.Sequential([
       Dense(64, activation='relu', input_shape=(features.shape[1],)),
       Dropout(0.2),
       Dense(32, activation='relu'),
       Dropout(0.2),
       Dense(1, activation='sigmoid')
   ])
   ```

3. **Nutrition Logic**  
   - BMR Calculation (Mifflin-St Jeor Equation)
   - Activity Level Multipliers (1.2-1.9)
   - Goal-based Calorie Adjustment (±500 kcal)

## Performance
- Test Accuracy: 89.25% (5-Fold Cross Validation)
- Inference Time: <500ms per recommendation
- Supported Meal Types: 1500+ recipes across 12 cuisines

## Contributing
PRs welcome! Please follow PEP8 guidelines and include comprehensive tests.

---
** Project done by Craig C Machingura
cmach_99@yahoo.com  |  07832299178 |  
www.linkedin.com/in/craig-machingura-b8047719  |  https://github.com/cmach99/ChakaSystem.git




## Deployment Instructions of CDRS on a development server 

Brief setup instructions adapted from Grinberg (2018) are below;
Prerequisites: If intended to deploy on a production or WGSI server ensure Gunicorn server is initiated in the ‘Procfile’ file. Please ensure python3.5+ is pre-installed.

1)	From  https://github.com/cmach99/ChakaSystem.git
Download the zip folder onto your local Desktop. 
2)	Via a terminal prompt navigate to the folder containing the Flask app Folders and file
Create a virtual environment by executing the following code:
python3 -m venv  name_env. # where ‘name_env’ is the name of the virtual environment.
3)	Once created on your bash shell or terminal execute the code below in your project_folder to activate the virtual environment. 
source project_folder /bin/activate (If using a MacOSX)  
4)	Next step is to load all dependencies from the requirement.txt file.
pip3 install -r requirements.txt
5)	Finally execute the code to start the Flask application running:
python3 app.py
This action will initiate a web server. By default, Flask operates on port 5000. Accessing the Online Application - Launch your web browser. Visit `http;//127.0.0.1;5000/` to reach the Chaka Dietary Recommender System.

