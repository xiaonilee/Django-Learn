# 爬虫

## 爬虫过程：
- 模拟人去请求数据
- 提取有用的数据
- 存储数据

## 爬虫核心内容：
- 数据爬取(会有加密页面，以及动态页面)
- 数据提取(正则，框架等)
- 数据存储(mangoDB..)
- 提高效率
    - 线程
    - 进程
    - 协程
    
    
## JSON
- JsonObject
    - { }
    - key - value
- JsonArray
    - [ ]
    - 列表中可以是普通数据类型，也可以是JsonObject
- JsonObject和JsonArray可以嵌套
- 给移动端的Json
- 给Ajax
    - 前后端分离
    - DRF框架
- Google Chrome
    - JsonFomatter
    - JsonView
    
    
## HttpResponse
- HttpResonseRedirect
    - 重定向，暂时
    - status_code = 302
    - 简写 redirect
- JsonResponse
    - 以Json格式返回数据
    - 重写了__init__,序列化Jsons数据，指定content_type为application/json
- HttpResponsePermanentRedirect
    - 永久性的重定向
    - status_code = 301
- HttpResponseBadRequest
    - status_code = 400
- HttpResponseNotFound
    - status_code = 404
- HttpResponseForbidden
    - status_code = 403
- HttpResponseNotAllowed
    - status_code = 405
- HttpResponseServerError
    - status_code = 500
- Http404
    - Exception
    - raise主动抛异常
    
    
## 会话技术
- 出现场景
    - 服务器如何识别客户端
    - Http在web开发中基本都是短链接
- 请求生命周期
    - 从Request开始
    - 到Response结束
- 种类
    - Cookies
        - 客户端会话技术
            - 数据存储在客户端
        - 以键值对存储
        - 支持过期时间
        - 默认Cookie会自动携带本网站所有Cookie
        - Cookie不能跨域名，不能跨网站
        - 通过HttpResponse
        - Cookie默认不支持中文
        - 可以加盐
            - 加密
            - 获取的时候需要解密
    - Session
        - 服务端会话技术
        - 数据存储在服务器中
        - 默认Session存储在内存中
        - Django中默认会把Session持久化到数据库中
        - Django中的session默认过期时间是14天
        - 主键是字符串
        - 数据是使用了数据安全的
            - 使用的是base64
            - 添加了混淆串（通过在线google解码工具获得https://www.base64decode.org/）
        - Session依赖于Cookie
    - Token
        - 服务端会话技术
        - 自定义的Session
        - 如果web页面开发中
            - 使用起来和Session基本一致
        - 如果使用移动端或者客户端开发中
            - 通常以Json形式传输，需要移动端自己存储Token，需要获取Token关联数据的时候，主动传递Token
            
     - Cookie，Session与Token三者相比
        - Cookie使用更加简洁，服务器压力更小，数据不是很安全
        - Session服务器需要维护Session，数据相对安全
        - token拥有Session的所有优点，自己维护略微麻烦，支持更多的终端
        
        
## CSRF
- 防止跨站攻击
- 防止恶意注册，确保客户端是我们自己的客户端
- 使用了cookie中的csrftoken进行验证，传输
- 服务器发送给客户端，客户端将cookie获取过来，还要进行编码转换（数据安全）
- 实现机制：
    - 页面中存在{% csrf_token %}时，
    - 在渲染的时候会向Response中添加csrftoken的Cookie
    - 在提交的时候，会被添加到请求体中，会验证有效性
    # 也可以如下理解：
    - 在我们存在csrf_token标签的页面中，响应会自动设置一个cookie：csrftoken
    - 当我们提交的时候，会自动验证csrftoken
    - 验证通过，会正常执行以后流程；验证不通过，会直接403，Forbidden
    
      
## 算法
- 编码解码
    - Base64
    - urlencode
- 摘要算法，指纹算法，杂凑算法
    - MD5，SHA
        - MD5默认128的二进制
        - 32位的十六进制
        - 32位的Unicode
    - 单向不可逆
    - 不论输入多长，输出都是固定长度
    - 只要输入有任意的变更，输出都会发生巨大的变化
- 加密
     - 对称加密
        - 一把钥匙
        - DES，AES
        - 加密和解密效率高
        - 钥匙一旦丢失，所有数据全丢
     - 非对称加密
        - 两把钥匙，成对的
        - 公钥和私钥
        - RSA，PGP
        - 安全性最高
        - 算法复杂，需要时间长
        - 支付宝和微信，都是RSA

## 好的程序
- 松耦合
    - 解耦合
- 高内聚
    
    
# 登陆
- 首先，有一个页面
    - 页面中有输入框
    - 有登陆按钮
- 点完登陆，默认进入个人中心
- 个人中心可以显示用户名
    

    
    