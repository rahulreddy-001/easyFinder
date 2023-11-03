from flask import Blueprint

from routes._register_person import register
from routes._search_person import search
from routes._search_image import search_image
api = Blueprint('api', __name__)

api.register_blueprint(register)
api.register_blueprint(search)
api.register_blueprint(search_image)

