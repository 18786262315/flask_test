from flask import Blueprint

main=Blueprint('main',__name__,url_prefix='/main')

@main.route('/')
def show():
    return 'mains.hello'
