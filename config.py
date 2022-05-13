import os


class Config:
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wamaitha:Wammy@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'Yellow'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
     
   
    

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    

    DEBUG = True
    

config_options={
'development':DevConfig,
'production':ProdConfig
}