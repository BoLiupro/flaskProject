from models.admin import user_admin
from models.rider import task, income, login_rider
from models.seller import like, collection, forward, comment, upload_seller
from models.user import register, cancellation, changePassword, changeName, follow, order, searchBySeller, \
    searchByGoods, searchByClassfication, login_user, upload_user,send_mail

from my_mail import mail

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)


mail.init_app(app)

api.add_resource(login_user, '/user/login')
api.add_resource(register, '/user/register')
api.add_resource(cancellation, '/user/cancellation')
api.add_resource(changePassword, '/user/changePassword')
api.add_resource(changeName, '/user/changeName')
api.add_resource(follow, '/user/follow')
api.add_resource(order, '/user/order')
api.add_resource(searchBySeller, '/user/searchBySeller')
api.add_resource(searchByGoods, '/user/searchByGoods')
api.add_resource(searchByClassfication, '/user/searchByClassfication')
api.add_resource(upload_user, '/user/upload_user')

api.add_resource(login_rider, '/rider/login')
api.add_resource(task, '/rider/task')
api.add_resource(income, '/rider/income')

api.add_resource(like, '/seller/like')
api.add_resource(collection, '/seller/collection')
api.add_resource(forward, '/seller/forward')
api.add_resource(comment, '/seller/comment')
api.add_resource(upload_seller, '/seller/upload_seller')

api.add_resource(user_admin, '/admin/user')

api.add_resource(send_mail, '/mail')



if __name__ == '__main__':
    app.run()
