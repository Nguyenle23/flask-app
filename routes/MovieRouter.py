from flask import Blueprint

from controllers.MovieController import MovieController
MovieRouter = Blueprint('MovieRouter', __name__)

MovieRouter.route('/', methods=['POST'])(MovieController.createMovie)
MovieRouter.route('/', methods=['GET'])(MovieController.getALlMovies)
MovieRouter.route('/<movieID>', methods=['GET'])(MovieController.getMovieByID)
MovieRouter.route('/<movieID>', methods=['PUT'])(MovieController.updateMovieByID)
MovieRouter.route('/<movieID>', methods=['DELETE'])(MovieController.delteMovieByID)


