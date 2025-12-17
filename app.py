from flask import Flask, render_template, redirect, url_for
from forms import RecommendationForm
import pickle
import numpy as np

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Load the trained model
with open('models/crop_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return redirect(url_for('recommend'))

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    form = RecommendationForm()
    if form.validate_on_submit():
        # Get form data
        N = form.nitrogen.data
        P = form.phosphorus.data
        K = form.potassium.data
        temperature = form.temperature.data
        humidity = form.humidity.data
        ph = form.ph.data
        rainfall = form.rainfall.data
        soil_type = form.soil_type.data
        
        # Create feature vector
        features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        
        # Make prediction
        prediction = model.predict(features)
        
        return render_template('recommendation.html', 
                            crop=prediction[0], 
                            soil_type=soil_type,
                            N=N, P=P, K=K,
                            temperature=temperature,
                            humidity=humidity,
                            ph=ph,
                            rainfall=rainfall)
    return render_template('recommendation_form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
