from app.model import users
import json
from app import db
from flask import Blueprint,request, make_response, Response, render_template, url_for

app01=Blueprint('app01',__name__,url_prefix='/app01')

@app01.route('/login',methods=['POST', 'get'])
def show():
    # return 'sssss'
    # json格式参数 请求
    gets = request.form.get
    # username = request.get_json()
    # password = request.form.get('password')
    # phone = request.form.get('phone')
    # print(username)
    newobj = users(phone = gets('phone') , name=gets('username'),  passowd=gets('password'))
    db.session.add(newobj)
    db.session.commit()
    # usersa = users.query.all()

    # print(usersa)
    userss = {
            'code': 0,
            'msg': '登录成功',
            'data': {
                'username':'admin',
                'password':'admin',
                'uuid': 'admin-uuid', 
                'name': '管理员',
                'token': '8dfhassad0asdjwoeiruty'
            }
            }

    return json.dumps(userss, ensure_ascii=False)
