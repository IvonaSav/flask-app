from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/average_spending_by_age', methods=['GET'])
def average_spending_by_age():

    user_id = request.args.get('user_id', type=int)


    connection = sqlite3.connect('users_vouchers.db')
    cursor = connection.cursor()


    cursor.execute('''
        SELECT u.user_id, u.name, u.email, u.age, SUM(us.money_spent) AS total_spending
        FROM user_info u
        JOIN user_spending us ON u.user_id = us.user_id
        WHERE u.user_id = ?
        GROUP BY u.user_id
    ''', (user_id,))

    result = cursor.fetchone()


    cursor.close()
    connection.close()

 
if __name__ == '__main__':
    app.run(debug=True)
