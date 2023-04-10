# Standard library imports
import os

# 3rd party imports
import openai
from flask import Flask, redirect, render_template, request, url_for

# Instantiate app
app = Flask(__name__)

# Get API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Index page
@app.route('/', methods=('GET', 'POST'))
def index():

    # This is executed for a POST request
    if request.method == 'POST':

        # Get input from input field
        animal = request.form['animal']

        # Generate superhero names with OpenAI model
        response = openai.Completion.create(
            model='text-davinci-003', # Define model
            prompt=generate_prompt(animal), # Build prompt using helper function
            temperature=0.6, # Set parameter which decides how determinate the model behaves
        )

        # Redirect to the same page, now with the result parameter defined
        return redirect(url_for('index', result=response.choices[0].text))

    # Extract result from request object if a GET request is executed.
    # This could be initially loading the page or a refresh.
    result = request.args.get('result')

    # Render index page
    return render_template('index.html', result=result)

# Helper function for generating prompt given animal
def generate_prompt(animal):

    # Return prompt
    return f'''Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {animal.capitalize()}
Names:'''

# Run app if script is executed as main.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)