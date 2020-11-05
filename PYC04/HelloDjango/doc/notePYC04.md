# Django

## 快捷键
- 万能键
    - option + enter
- control + p
    - 参数提示
    
## 实现一个请求
- 注册一个路由
    - urls中
        - url
            - 参数1 匹配规则 正则
            - 视图函数
                - 对应的是views中的一个函数
                    - 函数没有括号
- 去views中实现对应的视图函数
    - 第一个参数是request
    - 第二个参数是Response

## html,tab键补齐，生成标签对
- ul>li
- ul*5
- ul>li*5 

## 模版配置
- 两种
    - 在App中进行模版配置
        - 只需要在App的根目录创建templates文件夹即可
        - 如果想让代码自动提示，应该标记文件夹为'模版文件夹'
    - 在项目目录中进行模版配置
        - 需要在项目目录中创建templates文件夹并进行标记
        - 需要在settings中进行注册
- 在开发中使用第二种
    - 因为模版可以继承，复用

## 路由优化配置
- 项目如果逻辑过于复杂，可以进行拆分
    - 拆分为多个App
    - 继续拆分urls路由器
        - 在App中创建自己的urls
            - urlpatterns路由规划列表
            - 在根urls中进行子路由的包含
        - 子路由的使用
            - 根路由 + 子路由规则

## models 使用了ORM技术
- Object Relational Mapping 对象关系映射
- 将业务逻辑与sql进行了一个解耦合
    - object.save()
    - object.delete()
- 关系型数据库
    - DDL定义数据库
    - 通过models定义实现数据库表的定义   
- 数据操作
    - 增删改查
    - 存储
        - save()
    - 查询
        - 查所有 objects.all()
        - 查单个 objects.get(pk=xx)
    - 更新
        - 基于查询得到的
        - 查好的对象， 修改属性， 然后save()
    - 删除
        - 基于查询得到的
        - 调用delete()
## 数据迁移
- 生成迁移
    - python manage.py makemigrations
- 执行迁移
    - python manage.py migrate
    

## 连接mysql驱动
- mysqlClient
    - python2,python3均兼容，可以直接使用
    - 致命缺点
        - 对mysql安装有要求，必须在指定位置存在配置文件
- python-mysql
    - python2,支持很好
    - python3，不支持
- pymysql
    - python2, python3 都支持
    - 它可以伪装成前面的库
    - 下载安装：pip install pymysql
    - 如果速度太慢，换源重新下载安装：pip install pymysql -i https://pypi.douban.com/simple

## 配置mysql
- settings.py文件中，给'DATABASES'添加mysql相关信息
- 连接mysql server:
    - open docker应用程序
    - 对'docker-compose.yml'选择'open in terminal'
    - 在终端执行：docker-compose -f docker-mariadb.yml up -d           
## 在终端安装mysql客户端：
- brew install mysql-client
- 继续执行brew cleanup
- 在终端执行：echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.zshrc
- source ~/.zshrc
## 进入mysql终端:
- mysql -h127.0.0.1 -uroot -p123456
- 退出mysql-client: quit;
- 退出 mysql server: docker-compose down
    
    
## 创建应用
- python manage.py startapp <appname>
- 将应用'appname'注册加入到settings.py的INSTALLED_APPS中 

## 项目目录介绍
- __init__.py: 暂无内容，使得app成为一个包
- admin.py: 管理站点模型的声明文件，默认为空
- apps.py: 应用信息定义文件，，在其中生成了APPConfig
- models.py: 添加模型层数据类文件
- views.py: 定义URL相应函数（路由）
- migrations包:自动生成，迁移文件
- test.py: 测试代码文件 
- urls.py: 
    - 基于模块化的设计，通常会在每个app中定义自己的urls；
    - 然后在项目的urls中将app的urls包含进来
    - 用法： 
        - from django.conf.urls import include
        - url('welcome/',include(appname.urls))

## django shell
- 集成了python环境中的shell终端
- 通常在终端中做一些调试工作
- 进入python shell: python manage.py shell

## 如何看待bug
- 看日志
    - 先看第一条， 相对来说是最重要的
    - 再看最后一条
    - 将错误google
- 梳理思路
    - 看程序在什么位置出现了与预期的偏差

## 表关系
- 1：1
- 1：M
- M：M