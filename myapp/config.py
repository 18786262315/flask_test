# import os

class Config:
    # SECRET_KEY = os.urandom (24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ycc962464@127.0.0.1:3306/tests'
    SQLALCHEMY_COMMIT_ON_TEARDOWN =True
    SQLALCHEMY_TRACK_MODIFICATIONS = True



    @staticmethod
    def init_app(app):
        pass
