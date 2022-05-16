import os


class Config:
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wamaitha:Wammy@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = 'Yellow'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("pitcher24@gmail.com")
    MAIL_PASSWORD = os.environ.get("1234567")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
     
   
    

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')# or the relevant config var
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgress://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgress://","postgressql://",1)
        
        #rest of connection code using the connection string 'uri'


class DevConfig(Config):
    

    DEBUG = True
    

config_options={
'development':DevConfig,
'production':ProdConfig
}