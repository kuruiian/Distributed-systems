from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'flask_user',
    'password': 'flask_password',
    'database': 'order_db'
}

@app.route('/orders', methods=['GET'])
def get_orders():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(orders)

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (product_id, quantity, price) VALUES (%s, %s, %s)",
                   (data['product_id'], data['quantity'], data['price']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Order created'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
