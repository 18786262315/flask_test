from app import db,create_app

# from sqlalchemy import create_engine
db.create_all(app=create_app())

# db.create_all()