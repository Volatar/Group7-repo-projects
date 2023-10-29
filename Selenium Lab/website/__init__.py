from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret'

    from .views import views
    from .movies import movie
    from .checkout import checkout

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(movie, url_prefix="/")
    app.register_blueprint(checkout, url_previs="/")

    return app
