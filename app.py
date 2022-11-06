
from flask import Flask
from config import DEBUG, HOST, PORT, SECRET_KEY
from routes.MovieRouter import MovieRouter
from routes.UserRouter import UserRouter

app = Flask(__name__)  
app.secret_key = SECRET_KEY

app.register_blueprint(UserRouter, url_prefix='/user')
app.register_blueprint(MovieRouter, url_prefix='/movie')

if __name__ == '__main__':  # Running the app
    app.run(host = HOST, port = PORT, debug = DEBUG)
