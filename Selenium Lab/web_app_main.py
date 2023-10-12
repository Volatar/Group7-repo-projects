"""Import web-app"""
from website import create_app


"""Initialize web-app"""
app = create_app()


"""Run main"""
if __name__ == '__main__':
    app.run()
