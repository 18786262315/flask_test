from flask import Blueprint

app03=Blueprint('app03',__name__,url_prefix='/app03')

@app03.route('/')
def show():
    return 'app03.hello'