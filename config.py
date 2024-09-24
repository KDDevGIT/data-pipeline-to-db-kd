import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://username:password@your-rds-endpoint/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
