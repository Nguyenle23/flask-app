from flask import Blueprint

from controllers.UserController import getALlUsers, getUserByID
UserRouter = Blueprint('UserRouter', __name__)

UserRouter.route('/', methods=['GET'])(getALlUsers)
UserRouter.route('/<userID>', methods=['GET'])(getUserByID)


