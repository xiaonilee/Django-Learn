
## 08282020

## Cache 缓存
- 提升服务器响应速度
- 将执行过的操作数据存储下来，在一定时间内，再次获取数据的时候，直接从缓存中获取
- 比较理想的方案，缓存使用内存级缓存
- Django内置缓存框架

- 安装django-redis和django-redis-cache
    - pip install django-redis
    - pip install django-redis-cache 

- 安装redis
    - brew info redis
    - brew install redis
    
- settings中CACHES设置：
- 'redis_backend': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
    
- 启动 redis服务器
    - redis-server
    
- 查看redis cache
    - redis-cli
    - select 1
    - get :1:news
    - ttl :1:news
    
    
## AOP中间件
- 实现统计功能
    - 统计IP
    - 统计浏览器
- 实现权重控制
    - 黑名单
    - 白名单
- 实现反爬~~~~
    - 反爬虫
        - 10秒之内只能搜索一次
    - 实现频率控制
- 界面友好化
- 应用交互友好化


## 中间件
- 调用顺序
    - 中间件注册的时候是一个列表
    - 如果没有在切点处直接进行返回，中间件会依次执行
    - 如果在切点处直接进行来返回， 后续中间件就不再执行了
- 切点
    - process_request
    - process_view
    - process_template_response
    - process_response
    - process_exeption
- 切面


## 快捷键
- command + Z 后退
- control + A 光标移到行首