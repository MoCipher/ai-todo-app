from flask import Flask
from ai_todo.api.routes import api_routes
from ai_todo.db.storage import initialize_db

def create_app():
    app = Flask(__name__)
    
    # Initialize database
    initialize_db(app)
    
    # Register API routes
    app.register_blueprint(api_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)