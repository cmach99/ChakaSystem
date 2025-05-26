# ChakaSystem
Dietary Recommender System

The Chaka Dietary Recommendation System is a project that aims to transform personalised nutrition and diet planning. By using technologies and methods this system not only predicts trends and user preferences accurately but also enhances the user experience with customised recommendations. With a focus, on data quality and the use of cutting-edge techniques like neural networks and reinforcement learning the system can identify complex data patterns and adjust suggestions in real time, based on user input and changing trends. By combining methods with demographic, session, and context specific data the system offers tailored recommendations to meet individual health and fitness goals. The goal of the Chaka Dietary Recommendation System is to establish itself as one of the leading platforms, for users looking to align their choices with their well-being promoting a healthier society overall.

Deployment Tools

Flask Application

Flask applications typically consist of routes and views, where routes serve as URL patterns that dictate the application's responses, and views are Python functions responsible for generating responses to incoming web requests. When a user solicits a specific URL within the application, Flask triggers the corresponding view function to create a response comprising simple text, HTML content, JSON data, or file input (Grinberg, 2018). Integrating a dietary machine learning recommender system into a Flask application enables the creation of a robust tool for providing personalised dietary recommendations to users. This system analyses data encompassing dietary preferences, restrictions, nutritional objectives, and health conditions to furnish tailored suggestions encompassing meal plans, recipes, and food choices.

Flask's intrinsic flexibility and extensibility render it an optimal platform for fabricating advanced dietary recommender systems. By seamlessly incorporating machine learning models, data processing pipelines, and external APIs, Flask offers a versatile environment for constructing such systems (Grinberg, 2018).

The lightweight structure and modular design of Flask make it easy to scale and maintain applications that house dietary recommender systems. This ensures optimal performance and reliability for users when interacting with the recommender system. In essence, Flask is the perfect framework for building web applications that integrate machine learning recommender systems, resulting in a seamless user experience and empowering individuals to make informed decisions about their dietary needs. All source code files are found in the appendices section.


•	Main File - 'app.py' - The main file, for the Flask application of the CDRS is called 'app.py'. It serves as the central point of the API for starting the Flask app and defining routes. These routes serve as points where incoming user requests are managed to offer recommendations. In this file endpoints are defined to allow users to interact with the recommendation system, including those that retrieve recommendations based on user input Grinberg (2018).

•	CDRS model file personalised_meal_recommendations.py’ - The CDRS model file is the ‘personalised_meal_recommendations.py’. This file lies the implementation to load the trained model and generate predictions or suggestions. The functions enclosed are invoked by `app.py` to acquire and deliver recommendations based on user inquiries.

•	Dependency loader – ‘requirements.txt’ - The requirements.txt file enumerates and loads all the essential Python libraries upon which the CDRS relies on. Its significance lies in ensuring the correct deployment environment matches the development setup accurately.

•	Templates directory - The templates directory contains two HTML files, the ‘index’ and ‘results’. The index page is intended as the web interface for accepting user inputs to engage the recommender system and the result page emits the recommendations to a webpage from the CDRS.

•	Static directory - The Static directory encompasses static resources such as CSS, JavaScript, and images utilised by the HTML templates to enhance the user experience and aesthetics of the API.

•	Data directory - The data directory houses the dataset ‘data.csv’

•	Procfile Folder - For deployment on production servers - Specifies the commands the app executes on start-up. For instance, define a Gunicorn server to run your Flask app.


Deployment Instructions of CDRS on a development server 

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

