from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configurations
    app.config['DEBUG'] = True
    
    # Register blueprints/routes
    from .routes import bp
    app.register_blueprint(bp)
    
    return app
