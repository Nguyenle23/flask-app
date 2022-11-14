
from routes.MovieRouter import MovieRouter
from routes.UserRouter import UserRouter

class Router:
  def run(app):
    app.register_blueprint(UserRouter, url_prefix='/user')
    app.register_blueprint(MovieRouter, url_prefix='/movie')