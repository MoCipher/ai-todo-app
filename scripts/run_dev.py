import os
import sys
from src.ai_todo.main import app

def run_dev():
    # Set the environment to development
    os.environ['FLASK_ENV'] = 'development'
    
    # Run the Flask application
    app.run(debug=True)

if __name__ == '__main__':
    run_dev()