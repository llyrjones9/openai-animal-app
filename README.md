# OpenAI API Animal Superhero Name Generation App
This is an example Flask app cloned from a repository belonging to OpenAI, changes have been made to OpenAI's version to allow for easier running of the app and containerisation.

Upon navigating to the base URL the user should enter an animal, the page will then generate 3 suggested super hero names for that animal using the OpenAI models via their API.

OpenAI created this repository as a use case for the OpenAI API suite, however in this case the repository has been restructured and modified. The repository now serves as a wider template for building and containerising a flask application.

# Setup
In both cases you will need to create an OpenAI account and retrieve your API key for using OpenAI's API suite.

## Running via local Python installation
1. Set your API key as an environmental variable under the name `OPENAI_API_KEY`
2. Install the `requirements.txt` contents into your Python installation or virtual environment
3. Navigate to the `flaskr` directory
4. Run `app.py`

## Running via local Docker Container
1. Add your API key to the `docker-compose.yml` file
2. Make sure your Docker Daemon is running
3. Run the command `docker-compose up` in your terminal from the repository's route

# Contribute
This project is not in activate development, however use cases for flask and OpenAI's large language models are vast therefore building out the app with additional features is a good place to start. 
