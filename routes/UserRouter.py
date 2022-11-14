from flask import Blueprint

from controllers.UserController import UserController
UserRouter = Blueprint('UserRouter', __name__)

UserRouter.route('/', methods=['POST'])(UserController.createUser)
UserRouter.route('/', methods=['GET'])(UserController.getALlUsers)
UserRouter.route('/<userID>', methods=['GET'])(UserController.getUserByID)
UserRouter.route('/<userID>', methods=['PUT'])(UserController.updateUserByID)
UserRouter.route('/<userID>', methods=['DELETE'])(UserController.deleteUserByID)

