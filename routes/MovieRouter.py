from flask import Blueprint

from controllers.MovieController import getALlMovies, getMovieByID
MovieRouter = Blueprint('MovieRouter', __name__)

MovieRouter.route('/', methods=['GET'])(getALlMovies)
MovieRouter.route('/<movieID>', methods=['GET'])(getMovieByID)


