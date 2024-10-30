class Config:
    SECRET_KEY = '5your secret key should be here '
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'willimsnotcorrect@gmail.com'
    MAIL_PASSWORD = 'this is secret'
