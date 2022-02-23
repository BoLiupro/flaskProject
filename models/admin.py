import parser


from flask_restful import reqparse, Resource

from models.mysql import conn

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help='please set an int')
parser.add_argument('password', type=int, help='please set an int')
parser.add_argument('newPassword', type=int, help='please set an int')

class user_admin(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id=args['id']
        sql = "select * from users where id =" + str(id)
        cursor.execute(sql)
        infomation_of_users = cursor.fetchall()
        return {
            "id":infomation_of_users[0][0],
            "password":infomation_of_users[0][1],
            "name":infomation_of_users[0][2],
            "follow":infomation_of_users[0][3],
            "order":infomation_of_users[0][4]
        }

    def put(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        newPassword = args['newPassword']
        sql = "update users set password=" + str(newPassword) + " where id=" + str(id)
        cursor.execute(sql)
        conn.commit()
        return "success"

    def delete(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id = args['id']
        sql ="delete from users where id="+str(id)
        cursor.execute(sql)
        conn.commit()
        return "sucess"

    def post(self):
        args = parser.parse_args()
        id = args['id']
        password = args['password']
        cursor = conn.cursor()
        sql = "insert into users(id,password) values (" + str(id) + "," + str(password) + ")"
        cursor.execute(sql)
        conn.commit()
        return "success"
