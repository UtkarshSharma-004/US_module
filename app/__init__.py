from flask import Flask 
from flask_cors import CORS
from config import setup_logging
from .routes import main 
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    CORS(app,resources={r"/*": {"origin": "*"}})
    
    logger = setup_logging

    app.register_blueprint(main)

    return app

