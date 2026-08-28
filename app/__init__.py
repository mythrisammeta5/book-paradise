from flask import Flask
from config import config
from app.extensions import db

def create_app(config_name='development'):
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    with app.app_context():
        # Import models
        from app.models import (
            User, Book, Category, Rental, Favorite, Review,
            Reward, GameScore, StudyBooking, Invoice
        )
        
        # Create tables
        db.create_all()
        
        # Register blueprints
        from app.routes import (
            main_bp, auth_bp, books_bp, rentals_bp,
            library_bp, rewards_bp, games_bp, ai_bp,
            invoice_bp, study_bp
        )
        
        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(books_bp)
        app.register_blueprint(rentals_bp)
        app.register_blueprint(library_bp)
        app.register_blueprint(rewards_bp)
        app.register_blueprint(games_bp)
        app.register_blueprint(ai_bp)
        app.register_blueprint(invoice_bp)
        app.register_blueprint(study_bp)
        
        # Initialize database with seed data if empty
        if User.query.first() is None:
            from app.seed import seed_database
            seed_database()
    
    return app
