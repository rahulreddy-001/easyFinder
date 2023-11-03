from flask import Blueprint, render_template, request
import os

from routes.face_recognition.search import compare_face
from routes.database.select import get_from_ids

target_directory = 'storage/images/test'

def save_photo(photo):
    if photo.filename == '':
        return None
    filename = photo.filename
    target = os.path.join(target_directory, filename)
    photo.save(target)
    return target

search_image = Blueprint('search_image', __name__)

@search_image.route('/search_image', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        path = save_photo(image)
        target_ids = compare_face(path)
        if len(target_ids) == 0:
            return render_template('search_results.html', results=[])
        else:
            result = get_from_ids(target_ids)
            print(result)
            return render_template('search_results.html', results=result)

    
    if request.method == 'GET':
        return render_template('search_image.html')
    