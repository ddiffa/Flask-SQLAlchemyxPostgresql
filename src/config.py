import os

class Development(object):
    """
    Development environment configuration
    """
    
    DEBUG = True
    TESTING = False
    # JWT_SECRET_KEY="hhgaghhgsdhdhdd"
    # SQLALCHEMY_DATABASE_URI="postgres://diffa:diffa@localhost/free_event"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    QR_CODE = os.getenv('QR_CODE')

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    # JWT_SECRET_KEY='hhgaghhgsdhdhdd'
    # SQLALCHEMY_DATABASE_URI='postgres://diffa:diffa@localhost/free_event'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    QR_CODE = os.getenv('QR_CODE')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

app_config = {
    'development': Development,
    'production': Production,
}