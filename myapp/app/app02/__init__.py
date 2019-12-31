from flask import Blueprint

app02=Blueprint('app02',__name__,url_prefix='/app02')

@app02.route('/')
def show():
    return 'app02.hello'