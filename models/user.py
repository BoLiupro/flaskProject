import re

from flask import url_for, render_template, request
from flask_restful import reqparse, Resource
from werkzeug.utils import secure_filename, redirect

from models.mysql import conn
from flask_mail import Message
from my_mail import mail

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help='please set an int')
parser.add_argument('password', type=int, help='please set an int')
parser.add_argument('newPassword', type=int)
parser.add_argument('newName', type=str)
parser.add_argument('follow', type=str)
parser.add_argument('order', type=str)
parser.add_argument('seller_id', type=int)
parser.add_argument('goods', type=str)
parser.add_argument('classfication', type=str)



class login_user(Resource):
    def get(self):
        args = parser.parse_args()
        id = args['id']
        password = args['password']
        cursor = conn.cursor()
        cursor.execute('select id from users;')
        id_all = cursor.fetchall()
        cursor.execute('select password from users;')
        password_all = cursor.fetchall()
        check = False
        for i in range(len(id_all)):
            if ((id == id_all[i][0]) & (password == password_all[i][0])):
                check = True
        if (check):
            return "success"
        else:
            return "failed"


class register(Resource):
    def get(self):
        args = parser.parse_args()
        id = args['id']
        password = args['password']
        cursor = conn.cursor()
        sql = "insert into users(id,password) values (" + str(id) + "," + str(password) + ")"
        cursor.execute(sql)
        conn.commit()
        return "success"




class cancellation(Resource):
    def get(self):
        args = parser.parse_args()
        id = args['id']
        password = args['password']
        cursor = conn.cursor()
        cursor.execute('select id from users;')
        id_all = cursor.fetchall()
        cursor.execute('select password from users;')
        password_all = cursor.fetchall()
        check = False
        for i in range(len(id_all)):
            if ((id == id_all[i][0]) & (password == password_all[i][0])):
                check = True
        if (check):
            sql = "delete from users where id=" + str(id)
            cursor.execute(sql)
            conn.commit()
            return "success"
        else:
            return "failed"


class changePassword(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        newPassword = args['newPassword']
        sql = "update users set password=" + str(newPassword) + " where id=" + str(id)
        cursor.execute(sql)
        conn.commit()
        return "success"


class changeName(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        newName = args['newName']
        sql = "update users set name='" + newName + "' where id=" + str(id)
        cursor.execute(sql)
        conn.commit()
        return "success"


class follow(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        follow = args['follow']
        cursor.execute('select follow from users where id =' + str(id))
        follow_all = cursor.fetchall()
        follow = str(follow_all[0][0]) + "&" + follow
        sql = "update users set follow='" + follow + "' where id=" + str(id)
        cursor.execute(sql)
        conn.commit()
        return "success"


class order(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        order = args['order']
        sql = "update users set orderOfB='" + order + "' where id=" + str(id)
        cursor.execute(sql)
        conn.commit()
        return "success"


class searchBySeller(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        seller_id = args['seller_id']
        sql = 'select * from seller where id =' + str(seller_id)
        cursor.execute(sql)
        infomation_of_seller = cursor.fetchall()
        conn.commit()
        return {
            "id": infomation_of_seller[0][0],
            "classfication": infomation_of_seller[0][1],
            "comment": infomation_of_seller[0][2],
            "like": infomation_of_seller[0][3],
            "collection": infomation_of_seller[0][4],
            "forward": infomation_of_seller[0][5],
            "goods": infomation_of_seller[0][6]
        }


class searchByGoods(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        goods = args['goods']
        sql = "select * from seller where goods ='" + goods + "'"
        cursor.execute(sql)
        infomation_of_seller = cursor.fetchall()
        conn.commit()
        return {
            "id": infomation_of_seller[0][0],
            "classfication": infomation_of_seller[0][1],
            "comment": infomation_of_seller[0][2],
            "like": infomation_of_seller[0][3],
            "collection": infomation_of_seller[0][4],
            "forward": infomation_of_seller[0][5],
            "goods": infomation_of_seller[0][6]
        }


class searchByClassfication(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        classfication = args['classfication']
        sql = "select * from seller where classfication ='" + str(classfication) + "'"
        cursor.execute(sql)
        infomation_of_seller = cursor.fetchall()
        conn.commit()
        return {
            "id": infomation_of_seller[0][0],
            "classfication": infomation_of_seller[0][1],
            "comment": infomation_of_seller[0][2],
            "like": infomation_of_seller[0][3],
            "collection": infomation_of_seller[0][4],
            "forward": infomation_of_seller[0][5],
            "goods": infomation_of_seller[0][6]
        }


# @app.route('/user/upload', methods=['POST', 'GET'])
# def upload():
#     args = parser.parse_args()
#     id = args['id']
#     if request.method == 'POST':
#         f = request.files['file']
#         regex = re.compile('\..*')
#         x = regex.findall(secure_filename(f.filename))
#         f.save("/Users/liubo/Desktop/upload/user/"+str(id)+x[0])
#         return redirect(url_for('upload'))
#     return render_template('upload.html')

# class upload_user(Resource):
#     def post(self):
#         args = parser.parse_args()
#         id = args['id']
#         if request.method == 'POST':
#             f = request.files['file']
#             regex = re.compile('\..*')
#             x = regex.findall(secure_filename(f.filename))
#             f.save("/Users/liubo/Desktop/upload/user/" + str(id) + x[0])
#             return redirect(url_for('upload_user'))
#         return render_template('upload.html')

class upload_user(Resource):
    def post(self):
        args = parser.parse_args()
        id = args['id']
        f = request.files['file']
        regex = re.compile('\..*')
        x = regex.findall(secure_filename(f.filename))
        f.save("/Users/liubo/Desktop/upload/user/" + str(id) + x[0])
        return redirect(url_for('upload_user'))

    def get(self):
        args = parser.parse_args()
        id = args['id']
        return render_template('upload.html')


class send_mail(Resource):
    def get(self):
        message=Message(
            subject="cs",
            recipients="2149237461@qq.com",
            body="测试"
        )
        mail.send(message)
        return "success"



