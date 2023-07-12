
from flask import Flask, jsonify, request
import mysql.connector

class UserClass:
    def __init__(self):
        print("Enter UserClass __init__()")

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

def get_user_list():
    user = []
    query =  "SELECT * FROM user"
    db, cursor = query_handle(query)
    results = cursor.fetchall()
    for row in results:
        item = {'id': row[0]}
        item['name'] = row[1]
        item['mail'] = row[2]
        item['native_lang'] = row[3]
        item['line_id'] = row[4]
        user.append(item)
    db.close()

    return jsonify(user), 200

def get_user_data(id):
    user = []
    query =  f"SELECT * FROM user WHERE `id`='{id}'"
    db, cursor = query_handle(query)
    results = cursor.fetchall()
    for row in results:
        item = {'id': row[0]}
        item['name'] = row[1]
        item['mail'] = row[2]
        item['native_lang'] = row[3]
        item['line_id'] = row[4]
        user.append(item)
    db.close()

    return jsonify(user), 200