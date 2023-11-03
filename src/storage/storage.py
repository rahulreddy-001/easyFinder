import os
from flask import Blueprint, current_app, send_from_directory

storage = Blueprint('storage', __name__)

@storage.route('/storage/images/<path:filename>', methods=['GET'])
def index(filename):
    file_path = os.path.join('storage/images', filename)
    
    if os.path.exists(file_path):
        return send_from_directory(os.path.join(current_app.root_path, 'storage/images'), filename)
    else:
        return send_from_directory(os.path.join(current_app.root_path, 'storage/images'), 'default.png')

