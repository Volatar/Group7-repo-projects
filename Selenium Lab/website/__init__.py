from flask import Flask
from flask_login import LoginManager
import json

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    from .views import views
    from .movies import movie
    from .checkout import checkout
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(movie, url_prefix="/")
    app.register_blueprint(checkout, url_previs="/")

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(email):
        file = open("user_data.json", 'r')
        user_data = json.load(file)
        file.close()
        return user_data

    return app

    return app
