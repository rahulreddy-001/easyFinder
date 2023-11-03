from flask import Flask, render_template

from routes.api import api
from storage.storage import storage

app = Flask(__name__,template_folder='static/templates')

app.register_blueprint(api)
app.register_blueprint(storage)


@app.route('/')
def index():
    return render_template('index.html')

    
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

