from flask import Blueprint

app04=Blueprint('app04',__name__,url_prefix='/app04')

@app04.route('/')
def show():
    return 'app04.hello'