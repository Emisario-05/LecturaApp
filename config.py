class Config:
    SECRET_KEY  = 'gfdngidrngidfufbuifbvudgbdfgnfbkfvndjkvbdfuibfgjbjhdbfjhfgbnjfgg' 
    DEBUG       = True

class DevelopmentConfig(Config):
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'lectura'

config = {
    'development': DevelopmentConfig
}