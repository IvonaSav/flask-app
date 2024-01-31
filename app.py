from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/total_spending_by_age', methods=['GET'])
def total_spending_by_age():
    print(request.url)
    return jsonify({'message': 'This is the total spending!'})


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/total_spent/<int:user_id>', methods=['GET'])
def total_spent(user_id):
    return f'Welcome to the Flask API! User ID: {user_id}'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/write_to_mongodb', methods=['POST'])
def write_to_mongodb():
  

    return jsonify({'message': 'Data successfully written to MongoDB'})

if __name__ == '__main__':
    app.run(debug=True)