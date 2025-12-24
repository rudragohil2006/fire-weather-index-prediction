🔥 Fire Weather Index (FWI) Prediction

End-to-End Machine Learning Web Application

📌 Overview

An end-to-end Machine Learning project that predicts the Fire Weather Index (FWI)

Helps assess forest fire risk based on weather and environmental conditions

Includes complete pipeline: data preprocessing → model training → deployment

Deployed locally using a Flask web application

🎯 Objectives

Build a regression model to predict Fire Weather Index

Implement a real-world ML workflow

Provide a clean and user-friendly web interface

Follow industry-standard project structure

🧠 Machine Learning Details

Problem Type: Regression

Algorithms Used: Ridge Regression, Lasso Regression

Final Model: Ridge Regression

Preprocessing: Feature Scaling using StandardScaler

Model Persistence: Pickle (.pkl files)

🛠️ Tech Stack

Language: Python

Libraries: NumPy, Pandas, Scikit-learn

Web Framework: Flask

Frontend: HTML, CSS

Tools: VS Code, Jupyter Notebook

📊 Input Features

Temperature (°C)

Relative Humidity (%)

Wind Speed (km/h)

Rainfall (mm)

Fine Fuel Moisture Code (FFMC)

Duff Moisture Code (DMC)

Initial Spread Index (ISI)

Fire Occurrence Class (0 = No Fire, 1 = Fire)

Region (0 = Bejaia, 1 = Sidi Bel Abbes)

🌐 Application Workflow

User enters meteorological data through the web form

Inputs are validated and scaled using a saved scaler

Scaled data is passed to the trained ML model

Predicted Fire Weather Index is displayed on the UI