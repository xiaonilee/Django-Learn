## Model
- 在企业中，通常是从数据开始开发的

## ORM
- 对象关系映射
- 可以理解为翻译机
- 核心思想：解耦合
    - 将业务逻辑和SQL进行了解耦
    
## 数据库中的数据类型
- 字符串
- 数值
- 日期时间

## 模型过滤
- filter
- exclude
- 连续使用
    - 链式调用
    - Person.objects.filter().filter().filter().....exclude().exclude()...

## 快捷键
- .re 快捷生成return
- .if 快捷生成 if....:

## 方法
- 对象方法
    - 可以调用对象的属性，也可以调用类的属性
- 类方法
    - 不能调用对象属性，只能调用类属性
- 静态方法
    - 啥都不能调用，不能获取对象属性，也不能获取类属性
    - 只能寄生在这个类上而已
    
## 状态码
- 2xx
    - 请求成功
- 3xx
    - 转发或重定向
- 4xx
    - 客户端错误
- 5xx
    - 服务器错了
    - 后端开发人员最不想看到的
    
## 获取单个对象
- 查询条件没有匹配的对象，会抛异常，DoesNotExist
- 如果查询条件对应多个对象，也会抛异常，MultipleObjectsReturned

## first and last
- 默认情况下可以正常从QuerySet中获取
- 但是，存在隐藏的bug
    - 可能会出现first和last获取的是相同的对象
        - 显式，手动写排序规则
        
## 切片
- 和python中的切片不太一样
- QuerySet[5:15] 获取第5条到第15条的数据
    - 相当于SQL中的limit和offset
    
## 缓存集
- filter
- exclude
- all
- 都不会真正的去查询数据库
- 只有我们在迭代结果集，或者获取单个对象属性的时候，它才会去查询数据库
- 懒查询
    - 为了优化结构和查询
    
## 查询条件
- 属性_运算符=值
    - gt
    - lt
    - gte
    - lte
    - in 在某一集合中
    - contains 类似模糊查询的like
    - startswith 本质也是like
    - endswith 也是like
    - exact
- 前面同时添加i，表示ignore忽略
    - iexact
    - icontains
    - istartswith
    - iendswith
- Django中查询条件有时区问题
    - 关闭django中自定义的时区
    - 在数据库中创建对应的时区表
    
## F
- 可以获取属性的值
- 可以实现一个模型的不同属性的运算操作
- 还可以支持算数运算


## Q
- 可以对条件进行封装
- 封装之后可以进行逻辑运算
    - 与 & and
    - 或 | or
    - 非 ~ not
        
        
## 模型成员
- 显性属性
    - 开发者手动书写的属性
- 隐性属性
    - 开发者没有书写，ORM自动生成的
    - 如果把隐性属性手动声明了，系统就不会为你产生隐性属性了

