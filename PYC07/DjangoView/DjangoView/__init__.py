'''
pip install pymysql 执行之后，
需要在该文件中添加初始化代码
'''

import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()