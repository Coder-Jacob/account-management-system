import platform

_DEBUG = False
# _STATIC_URL = '/static/'
WINDOWS = 'Windows'
LINUX = 'Linux'
MacOS = 'Darwin'
CURRENT_SYSTEM = platform.system()

if CURRENT_SYSTEM == WINDOWS or CURRENT_SYSTEM == MacOS:
    _DEBUG = True
    # import pymysql
    from .secret import LOCAL as DB
    _DB = DB
    # pymysql.version_info = (1, 4, 13, "final", 0)
    # pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库

else:
    """
        生产环境 
    """
    # import pymysql
    from .secret import PRODUCTION as DB
    _DB = DB
    # pymysql.version_info = (1, 4, 13, "final", 0)
    # pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库

print(f"this app is running on {CURRENT_SYSTEM},DEBUG:{_DEBUG}")
