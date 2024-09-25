import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'mysql+pymysql://admin:DatabaseL0ck1849!@ky-database-1.cz86mwc2sye6.us-east-2.rds.amazonaws.com/asset_management'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

