import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split,KFold

import os
import logging
import warnings

def get_recommendations(weight, height, age, gender, activity_level, goal, preferred_cuisine, preferred_diet_type):
    # Setup to suppress warnings and logging
    warnings.filterwarnings('ignore')
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow logging to FATAL
    logging.getLogger('tensorflow').setLevel(logging.FATAL)

    # Load dataset
    data = pd.read_csv('data/data.csv')

    # Data preparation and feature engineering
    data['TotalCalories'] = data['Protein(g)'] * 4 + data['Carbs(g)'] * 4 + data['Fat(g)'] * 9

    # Encoding and normalizing
    encoder = OneHotEncoder(sparse=False)
    scaler = MinMaxScaler()
    categorical_features = data[['Cuisine_type', 'Diet_type']]
    numerical_features = data[['Protein(g)', 'Carbs(g)', 'Fat(g)', 'TotalCalories']]
    categorical_encoded = encoder.fit_transform(categorical_features)
    numerical_normalized = scaler.fit_transform(numerical_features)
    features = np.concatenate([categorical_encoded, numerical_normalized], axis=1)

    # Model setup
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(features.shape[1],)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Labels and splitting
    labels = (data['TotalCalories'] < 2000).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Model training
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    for train_index, val_index in kf.split(X_train):
        X_train_fold, X_val_fold = X_train[train_index], X_train[val_index]
        y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]
    model.fit(X_train_fold, y_train_fold, epochs=50, batch_size=16, validation_data=(X_val_fold, y_val_fold), verbose=0)
   
    # Model evaluation
    loss, accuracy = model.evaluate(X_test, y_test, verbose=1)
    print(f'Test Accuracy: {accuracy * 100:.2f}%')

    # BMR and daily calorie needs calculation
    bmr, daily_calories = calculate_calories(weight, height, age, gender, activity_level, goal)

    # Meal grading and recommendations
    data = grade_meals(data, daily_calories)
    recommendations = filter_meals(data, preferred_cuisine, preferred_diet_type, daily_calories)

    return format_recommendations(recommendations)

def calculate_calories(weight, height, age, gender, activity_level, goal):
    if gender == 'M':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    activity_factors = {
        'sedentary': 1.2, 'light': 1.375, 'moderate': 1.55, 'heavy': 1.725, 'very heavy': 1.9
    }
    bmr *= activity_factors.get(activity_level, 1.2)
    
    if goal == 'lose weight':
        daily_calories = bmr - 500
    elif goal == 'gain muscle':
        daily_calories = bmr + 500
    else:  # maintain weight
        daily_calories = bmr

    return bmr, daily_calories

def grade_meals(data, daily_calories):
    """
    Grade meals based on their calorie content relative to a third of the user's daily calorie needs.
    """
    # Applying the Meal Grading Logic
    data['HealthGrade'] = data['TotalCalories'].apply(lambda x: '5 stars - Very Healthy' if x <= (daily_calories / 3)
                                                      else '4 stars - Moderately Healthy' if x <= (daily_calories / 2.5)
                                                      else '3 stars - Healthy' if x <= (daily_calories / 2)
                                                      else '2 stars - Unhealthy' if x <= (daily_calories / 1.5)
                                                      else '1 star - Obese risk' if x > (daily_calories / 1.5)
                                                      else '0 stars - Malnourished risk')
    return data

def filter_meals(data, preferred_cuisine, preferred_diet_type, daily_calories):
    """
    Filter meals based on the user's cuisine and diet type preferences, as well as their calorie limits.
    """
    # Filtering the dataset based on user preferences and calorie limits
    filtered_data = data[(data['Cuisine_type'].str.lower() == preferred_cuisine) &
                         (data['Diet_type'].str.lower() == preferred_diet_type) &
                         (data['TotalCalories'] <= daily_calories)]
    
    return filtered_data.sort_values(by=['HealthGrade', 'TotalCalories'], ascending=[True, True])

def format_recommendations(filtered_data):
    """
    Format the filtered dataset into a list of dictionaries for display.
    """
    recommendations = []
    for index, row in filtered_data.iterrows():
        recommendation = {
            'Recipe_name': row['Recipe_name'],
            'Cuisine_type': row['Cuisine_type'],
            'Diet_type': row['Diet_type'],
            'TotalCalories': f"{row['TotalCalories']:.2f}",
            'HealthGrade': row['HealthGrade']
        }
        recommendations.append(recommendation)
    return recommendations if recommendations else []

