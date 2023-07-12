import os
from flask import Flask, jsonify, request
import mysql.connector
from flask_cors import CORS
import user_module

app = Flask(__name__)

app.config["DEBUG"] = True
CORS(app)

api_base = '/api/'

def query_handle(query):
    db = mysql.connector.connect(
        host = "DB_HOST",
        user = "DB_USER", 
        passwd = "DB_PASSWD", 
        db = "DB_NAME"
    )
    cursor = db.cursor()
    cursor.execute(query)
    return db, cursor

@app.route( api_base + 'user/<int:Number>', methods=['GET'])
def get_user_data(Number):
    return user_module.get_user_data(Number)


@app.route( api_base + 'user', methods=['GET'])
def get_user_list():
    return user_module.get_user_list()

# [ GET ] http://localhost:5000/api/zh/shop/1
# 整理成 shop 資料 ＆ menu 資料
@app.route( api_base + '<Lang>/shop/<int:Number>', methods=['GET'])
def get_shop_data(Lang, Number):
    shop_data = []
    
    query_shop_name =  f"SELECT * FROM `shop_name` WHERE `shop_id`='{Number}' AND `lang`='{Lang}'"
    db, cursor = query_handle(query_shop_name)
    shop_results = cursor.fetchall()

    menu = []

    query_shop_menu =  f"SELECT * FROM `menu` WHERE `shop_id`='{Number}' AND `lang`='{Lang}'"
    db, cursor = query_handle(query_shop_menu)
    menu_results = cursor.fetchall()
    for row in menu_results:
        item = {'id': row[0]}
        item['name'] = row[3]
        item['description'] = row[4]
        item['price'] = row[5]
        menu.append(item)

    for row in shop_results:
        shop = {'id': row[0]}
        shop['shop_id'] = row[1]
        shop['lang'] = row[2]
        shop['name'] = row[3]
        shop['menu'] = menu
        shop_data.append(shop)

    db.close()
    return jsonify(shop_data), 200

# http://localhost:5000/api/zh/shops
@app.route( api_base + '<Lang>/shops', methods=['GET'])
def get_shops(Lang):
    shops = []
    query =  f"SELECT * FROM `shop_name` WHERE `lang`='{Lang}'"

    db, cursor = query_handle(query)
    results = cursor.fetchall()
    for row in results:
        shop = {'id': row[0]}
        shop['shop_id'] = row[1]
        shop['lang'] = row[2]
        shop['name'] = row[3]
        shops.append(shop)
    db.close()
    
    return jsonify(shops), 200
 
if __name__ == "__main__":
    # app.run(debug=True, host='0.0.0.0', port=8888)
    app.run(debug=True, host='0.0.0.0')