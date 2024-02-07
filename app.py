from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask API!'


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

if __name__ == '__main__':
    app.run(debug=True)

# @app.route('/total_spent/<int:user_id>', methods=['GET'])
# def total_spent(user_id):
#     return f'Welcome to the Flask API! User ID: {user_id}'

# if __name__ == '__main__':
#     app.run(debug=True)

# @app.route('/write_to_mongodb', methods=['POST'])
# def write_to_mongodb():
  

#     return jsonify({'message': 'Data successfully written to MongoDB'})

# if __name__ == '__main__':
#     app.run(debug=True)