from flask import Blueprint
from app.routes.main import main_bp
from app.routes.auth import auth_bp
from app.routes.books import books_bp
from app.routes.rentals import rentals_bp
from app.routes.library import library_bp
from app.routes.rewards import rewards_bp
from app.routes.games import games_bp
from app.routes.ai_assistant import ai_bp
from app.routes.delivery import delivery_bp
from app.routes.admin import admin_bp

__all__ = [
    'main_bp',
    'auth_bp',
    'books_bp',
    'rentals_bp',
    'library_bp',
    'rewards_bp',
    'games_bp',
    'ai_bp',
    'delivery_bp',
    'admin_bp'
]
