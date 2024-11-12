class Config:
    SECRET_KEY  = 'gfdngidrngidfufbuifbvudgbdfgnfbkfvndjkvbdfuibfgjbjhdbfjhfgbnjfgg' 
    DEBUG       = True

class DevelopmentConfig(Config):
    ''' MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'lectura' '''
    #pythonanywhere
    MYSQL_HOST      = 'lecturaapp.mysql.pythonanywhere-services.com'
    MYSQL_USER      = 'lecturaapp'
    MYSQL_PASSWORD  = 'polloman05'
    MYSQL_DB        = 'lecturaapp$lectura' 


config = {
    'development': DevelopmentConfig
}