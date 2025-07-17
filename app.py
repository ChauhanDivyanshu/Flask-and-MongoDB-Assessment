""" from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Open and read data from file
        with open('data.json', 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) """
    
    
"""from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)"""

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://divyanshuchauhan1200:<JtnPetGHcHobgqTG>@cluster0.v7zfish.mongodb.net/myDB?retryWrites=true&w=majority")
db = client['myDB']
collection = db['submissions']

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        try:
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except PyMongoError as e:
            error = f"Error submitting data: {str(e)}"

    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)


