from flask import Blueprint, render_template, request, redirect
from routes.database.insert import save_to_db

import os
import uuid

target_directory = 'storage/images/'

def save_photo(id , photo):
    if photo.filename == '':
        return None
    filename = id + '.jpg'
    target = os.path.join(target_directory, filename)
    photo.save(target)
    return target
    
register= Blueprint('register', __name__)

@register.route('/register', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        id = str(uuid.uuid4())
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        height = request.form.get('height')
        weight = request.form.get('weight')
        description = request.form.get('description')
        photo = request.files['photo']
        missing_date = request.form.get('missing-date')
        photo_path = save_photo(id, photo)

        person_data = {
            'id': id,
            'name': name,
            'age': int(age),
            'gender' : gender,
            'height': float(height),
            'weight': float(weight),
            'description': description,
            'photo': photo_path,
            'missing_date': missing_date,
        }

        if save_to_db(person_data):
            # return "Edit link: <a href='#'> /edit/" + str(id) + "</a>"
            return render_template("register_success.html")
        else:
            return "Registration failed!"
        

    if request.method == 'GET':
        return render_template('register.html')
