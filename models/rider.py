import parser
from datetime import datetime
from flask_restful import reqparse, Resource

from models.mysql import conn

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, help='please set an int')
parser.add_argument('password', type=int, help='please set an int')
parser.add_argument('user_id', type=int, help='please set an int')

class login_rider(Resource):
    def get(self):
        args = parser.parse_args()
        id = args['id']
        password = args['password']
        cursor = conn.cursor()
        cursor.execute('select id from rider;')
        id_all = cursor.fetchall()
        cursor.execute('select password from rider;')
        password_all = cursor.fetchall()
        check=False
        for i in range(len(id_all)):
            if((id==id_all[i][0])&(password==password_all[i][0])):
                check=True
        if(check):return  "success"
        else : return "failed"

class task(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id=args['id']
        user_id = args['user_id']
        cursor.execute('select orderOfB from users;')
        order = cursor.fetchall()[user_id-1][0]
        sql = "update users set orderOfB = 'None' where id = "+str(user_id)
        cursor.execute(sql)
        seller_id=int(order)
        # st=time.time()
        st=datetime.now()
        sql = "update rider set task_user_id=" + str(user_id) + " where id=" + str(id)
        cursor.execute(sql)
        sql = "update rider set task_seller_id=" + str(seller_id) + " where id=" + str(id)
        cursor.execute(sql)
        sql = "update rider set start_task_time='" + str(st) + "' where id=" + str(id)
        cursor.execute(sql)
        cursor.execute('select income from rider;')
        income = cursor.fetchall()[id-1][0]
        new_income=income+5
        sql = "update rider set income=" + str(new_income) + " where id=" + str(id)
        cursor.execute(sql)
        conn.commit()

class income(Resource):
    def get(self):
        cursor = conn.cursor()
        args = parser.parse_args()
        id=args['id']
        sql = "select income from rider where id="+str(id)
        cursor.execute(sql)
        conn.commit()
        income = cursor.fetchall()[0]
        return income
