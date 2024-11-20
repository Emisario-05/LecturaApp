class Config:
    SECRET_KEY  = 'gfdngidrngidfufbuifbvudgbdfgnfbkfvndjkvbdfuibfgjbjhdbfjhfgbnjfgg' 
    DEBUG       = True

class DevelopmentConfig(Config):
    MYSQL_HOST      = 'localhost'
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = 'mysql'
    MYSQL_DB        = 'lectura'
 

class Mailconfig(Config):
    MAIL_SERVER             = 'smtp.gmail.com'
    MAIL_PORT               = 587
    MAIL_USE_TLS            = True
    MAIL_USE_SSL            = False
    MAIL_USERNAME           = 'derek.torres5865@alumnos.udg.mx'
    MAIL_PASSWORD           = 'veew onsv htsl ohez'
    Mail_ASCII_ATTACHMENTS  = True
    MAIL_DEFAULT_SENDER     = 'derek.torres5865@alumnos.udg.mx'

config = {
    'development'   : DevelopmentConfig,
    'mail'          : Mailconfig
}