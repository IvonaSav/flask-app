from flask import Flask, request, jsonify
import sqlite3
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask API!'

#FIRST ENDPOINT
@app.route('/total_spending_by_age/<int:user_id>', methods=['GET'])
def total_spending_by_age(user_id):
    print(request.url)
    # return jsonify({'message': 'This is the total spending!'})
    # user_id = request.args.get('user_id', type=int)
    print(request.url)


    print(f"User ID: {user_id}")

    if user_id is None:
        return jsonify({'error': 'Invalid user_id parameter'}), 400
    pass
    

    db_path = 'C:\\Users\\User\\Desktop\\users_vouchers.db'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('''
        SELECT u.user_id, u.name, u.email, u.age, SUM(us.money_spent) AS total_spending
        FROM user_info as u
        JOIN user_spending as us ON u.user_id = us.user_id
        WHERE u.user_id = ?
        GROUP BY u.user_id
    ''', (user_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result:
        user_info = {
            'user_id': result[0],
            'name': result[1],
            'email': result[2],
            'age': result[3],
            'total_spending': result[4]
        }
        return jsonify(user_info)
    else:
         return jsonify({'error': 'User not found'}), 404

#SECONDENDPOINT
@app.route('/total_spent/<int:user_id>', methods=['GET'])
def total_spent(user_id):
    age_ranges = {
        '18-24': (18, 24),
        '25-30': (25, 30),
        '31-36': (31, 36),
        '37-47': (37, 47),
        '>47': (48, float('inf')),
    }

    db_path = 'C:\\Users\\User\\Desktop\\users_vouchers.db'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute('SELECT age FROM user_info WHERE user_id = ?', (user_id,))
    age_result = cursor.fetchone()

    cursor.close()
    connection.close()

    if age_result:
        age = age_result[0]

        found_range = None

        for range_name, age_range in age_ranges.items():
            if age_range[0] <= age <= age_range[1]:
                found_range = range_name
                break

        if found_range is not None:
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            cursor.execute('''
                SELECT AVG(us.money_spent) as average_spending
                FROM user_info as u
                JOIN user_spending as us ON u.user_id = us.user_id
                WHERE u.age >= ? AND u.age <= ?
            ''', age_range)


            average_spending = cursor.fetchone()[0]

            cursor.close()
            connection.close()


            return jsonify({'average_spending': average_spending})
        else:
            return jsonify({'error': 'No matching age range found'}), 404


#THIRDENDPOINT
    
client = MongoClient('mongodb://localhost:27017/')
db= client['flask_appDb']
collection= db['flask_app']

@app.route('/write_to_mongodb', methods=['POST'])
def write_to_mongodb():
    try:
        data = request.get_json()

        # Validate the input JSON
        if 'user_id' not in data or 'total_spending' not in data:
            return jsonify({'error': 'Invalid input JSON'}), 400

        user_id = data['user_id']
        total_spending = data['total_spending']

        # Insert data into MongoDB
        result = collection.insert_one({'user_id': user_id, 'total_spending': total_spending})

        return jsonify({'message': 'Data successfully inserted', 'inserted_id': str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500
  

#     return jsonify({'message': 'Data successfully written to MongoDB'})

if __name__ == '__main__':
    app.run(debug=True)