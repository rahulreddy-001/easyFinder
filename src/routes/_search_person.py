from flask import Blueprint, render_template, request
from routes.database.select import get_from_db

search = Blueprint('search', __name__)

@search.route('/search', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        gender = request.form.get('gender')
        height = request.form.get('height')
        weight = request.form.get('weight')
        missing_date = request.form.get('missing-date')

        if age:
            age = int(age)
        if height:
            height = float(height)
        if weight:
            weight = float(weight)

        search_criteria = {}

        if name:
            search_criteria['name'] = name
        if gender:
            search_criteria['gender'] = gender
        if missing_date:
            search_criteria['missing_date'] = missing_date

        if age:
            search_criteria['age'] = {'$gte': age - 3, '$lte': age + 3}
        if height:
            search_criteria['height'] = {'$gte': height - 0.5, '$lte': height + 0.5}
        if weight:
            search_criteria['weight'] = {'$gte': weight - 3, '$lte': weight + 3}
        
        print(search_criteria)
        response = get_from_db(search_criteria)
        if response:
            for person in response:
                del person['_id']
                print(person['photo'])
                if person['photo'] == None or person['photo'] == '' or person['photo'] == 'null':
                    person['photo'] = '/storage/images/default.png'

                    
                for key in person:
                    if person[key] == 'None' or person[key] == '':
                        person[key] = 'N/A'
            return render_template('search_results.html', results=response)
        else:
            return render_template('search_results.html', results=[])
    
    if request.method == 'GET':
        return render_template('search.html')
