import re

from django.http import request
from django.shortcuts import redirect
from flask import url_for, render_template, request
from flask_restful import reqparse, Resource
from werkzeug.utils import secure_filename, redirect


from models.mysql import conn

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('comment', type=str)

class like(Resource):
    def post(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        cursor.execute("select * from seller where id = "+str(id))
        like = cursor.fetchall()[0][3]
        cursor.execute("update seller set lik=" + str(like+1) + " where id=" + str(id))
        conn.commit()
        return "success"

class collection(Resource):
    def post(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        cursor.execute("select * from seller where id = "+str(id))
        collection = cursor.fetchall()[0][4]
        cursor.execute("update seller set Collection=" + str(collection+1) + " where id=" + str(id))
        conn.commit()
        return "success"

class forward(Resource):
    def post(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        cursor.execute("select * from seller where id = "+str(id))
        forward = cursor.fetchall()[0][5]
        cursor.execute("update seller set forward=" + str(forward+1) + " where id=" + str(id))
        conn.commit()
        return "success"

class comment(Resource):
    def post(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        new_comment = args['comment']
        id = args['id']
        cursor.execute("select * from seller where id = "+str(id))
        comment=cursor.fetchall()[0][2]
        cursor.execute("update seller set comment='" + comment+"&"+new_comment + "' where id=" + str(id))
        conn.commit()

# @app.route('/seller/upload', methods=['POST', 'GET'])
# def upload():
#     args = parser.parse_args()
#     id = args['id']
#     if request.method == 'POST':
#         f = request.files['file']
#         regex = re.compile('\..*')
#         x = regex.findall(secure_filename(f.filename))
#         f.save("/Users/liubo/Desktop/upload/seller/"+str(id)+x[0])
#         return redirect(url_for('upload'))
#     return render_template('upload.html')

class upload_seller(Resource):
    def post(self):
        args = parser.parse_args()
        id = args['id']
        f = request.files['file']
        regex = re.compile('\..*')
        x = regex.findall(secure_filename(f.filename))
        f.save("/Users/liubo/Desktop/upload/seller/" + str(id) + x[0])
        return redirect(url_for('upload_seller'))

    def get(self):
        args = parser.parse_args()
        id = args['id']
        return render_template('upload.html')
