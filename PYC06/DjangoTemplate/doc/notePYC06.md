## 快捷键
- command+Click 进入源码
- Alt+Enter 快速 Import 缺失的包, 单双引号转换, 测试正则表达式
- 生成代码格式：for→Tab→ {% for foo in %} {% endfor %}
- 查找：双击shift

- Refactor 重构
    - command+Alt+L 格式化代码
    - command+Alt+T 代码块包围(Try Except 等)
    - shift+F6 重命名
    - command+shift+Alt+T 变量名重构
    - command+Alt+V Extract Variable, 提取变量
    - command+Alt+P Extract Parameter, 提取参数 (在Function方法中使用)
    - command+Alt+C Extract Constant, 提取常量
    - command+Alt+M Extract Method, 提取方法
    - command+Alt+F Extract Field 提取字段 (在 class 类中使用)
- Edit 编辑
    - command+/ 注释
    - shift+Tab 取消缩进
    - command+shift+⬆/⬇ 移动代码 / 代码块
    - ctrl+shift+J Join, 两行代码合并为一行
    - Alt+Enter 快速 Import 缺失的包, 单双引号转换, 测试正则表达式
    - command+d,复制一行
    
    
## 注释
- 单行注释
    - {# XXXXX #}
- 多行注释
    - {% comment %}
            内容
      {% endcomment %}
      

## 标签
- 标识符{% %}
- 标签分为单标签和成对标签
- 成对标签不可以省略，开始标签和结束标签


## 结构标签
- block
    - 块
    - 用来规划布局
    - 首次出现，代表规划
    - 第二次出现，代表填充以前的规划
    - 第三次出现，代表填充以前的规划,默认是覆盖
        - 如果不想覆盖，可以添加{{ block.super }}
        - 使得实现了增量式操作
        
- extends
    - 继承
    - 可以获取父模版中的所有结构
    
    
- block + extends
    - 化整为零


- include
    - 包含
    - 可以将页面作为一部分，嵌入到其他页面中， 提高复用率
    
    
- include + block
    - 由零聚合为一
    
    
- 三标签可以混合使用


- 可以选择block+extends,则尽量不用include，其效率低


## 静态资源
- 动静分离
- 创建静态文件夹
- 在settings中进行注册STATICFILES_DIRS=[]
- 在模版中使用
    - 先加载静态资源： {% load static %}
    - 使用{% static 'xxx' %} xxx为相对路径
- 坑点
    - 仅在DEBUG模式下使用
    - 以后需要自己单独处理
    
    
## urls
- 路由器
    - 按照列表的书写顺序进行匹配的
    - 从上到下，没有最优匹配的概念
- 路由器编写规则
    - 在结尾处直接添加反斜线
- 路由路径中的参数使用()进行获取
    - 一个圆括号对用视图函数中的一个参数
    - 参数
        - 路径参数
            - 位置参数
                - 按照书写顺序进行匹配
            - 关键字参数
                - 按照参数名称匹配，和顺序无关了
        - 参数个数必须和视图函数中的参数个数一致（除了默认的request以外）


- 反向解析
    - 根据路由中注册的namespace和在子路由中注册name,这两个参数来动态获取我们的路径
    - 在模版中使用{% url 'namespace:name'%}
    - 如果带有位置参数{% url 'namespace:name' value1 value2 [valuen] %}
    - 如果带有关键字参数{% url 'namespace:name' key1=value1 key2=value2 [keyn=valuen] %}
    

## 错误页面定制
- 在模版中重写对应错误状态码页面
- 关闭DEBUG
- 实现原则
    - 就近原则
    
    
## 双R
- Request
    - 内置属性
        - method
        - path
        - GET
            - 类字典结构
            - 一个key允许对应多个值
            - get 获取单个value
            - getlist 获取多个value
        - POST
        - META
            - 各种客户端元信息
            - REMOTE_ADDR 远端访问IP
- Response

    
    
## 知识点
- locals
    - 内置函数
    - 将局部变量，使用字典的方式进行打包
    - key是变量名，value是变量中存储的数据

    
