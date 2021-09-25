
## session机制

### 原理


<br>

<a href='https://www.bilibili.com/video/av68746921/?p=19' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>


我们来思考一个问题。

一个网站，比如一个购物网站，服务成千上万的客户。

这么多客户同时访问网站，挑选商品，购物结算，都是通过HTTP请求访问网站的。

这个网站服务程序 怎么每个HTTP请求（比如付费 HTTP 请求）对应的是哪个客户的呢？

网站是怎么做到这点的呢？

一种常见的方式就是：通过  ```Session机制``` 


session 翻译成中文就是 ```会话``` 的意思

session 机制大体原理如下图所示 ：

![image](http://cdn1.python3.vip/imgs/gh/36257654_65581391-f38dbf00-dfad-11e9-859a-b30c9adcfebc.png)

<br>

![image](http://cdn1.python3.vip/imgs/gh/36257654_65583492-e5da3880-dfb1-11e9-9b3e-f533d8c534b4.png)

用户使用客户端登录，服务端进行验证（比如验证用户名、密码）。

验证通过后，服务端系统就会为这次登录创建一个session。

session就是一个数据结构，保存该客户这次登录操作相关信息。通常保存在数据库中。

同时创建一个唯一的sessionid（就是一个字符串），标志这个session。

然后，服务端通过HTTP响应，把sessionid告诉客户端。

客户端在后续的HTTP请求消息头中，都要包含这个sessionid。这样服务端就会知道，这个请求对应哪个session，从而知道对应哪个客户。


---

从上图可以看出， 服务端是通过 HTTP的响应头   ```Set-Cookie``` 把产生的 sessionid 告诉客户端的。

客户端的后续请求，是通过 HTTP的请求头 ```Cookie``` 告诉服务端它所持有的sessionid的。

cookie 英文就是小甜饼的意思，这里表示一小段数据。

HTTP 协议规定了， 网站服务端放HTTP响应中 消息头  ```Set-Cookie```  里面的数据， 叫做 cookie 数据， 浏览器客户端 必须保存下来。 

而且后续访问该网站，必须在 HTTP的请求头 ```Cookie``` 中携带保存的所有cookie数据。


白月SMS系统使用的就是典型 session 区分用户的机制。

大家先看视频中关于白月SMS系统的session讲解。

<br>

### requests处理session-cookie 


<br>

<a href='https://www.bilibili.com/video/av68746921/?p=20' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>

我们在Python代码中如果接收到服务端HTTP响应，其中Set-Cookie的数据怎么保存呢？ 后续怎样放到请求消息头中 Cookie中呢？

前面 学过 HTTP响应中 如何 获取响应头， 构建请求怎样设置请求头，完全可以自己处理。

而且，requests库给我们提供一个 ```Session```  类 。

通过这个类，无需我们操心， requests库自动帮我们保存服务端返回的 cookie数据， HTTP请求自动 在消息头中放入 cookie 数据。

如下所示：

```py
import requests

# 打印HTTP响应消息的函数
def printResponse(response):
    print('\n\n-------- HTTP response * begin -------')
    print(response.status_code)

    for k, v in response.headers.items():
        print(f'{k}: {v}')

    print('')

    print(response.content.decode('utf8'))
    print('-------- HTTP response * end -------\n\n')


# 创建 Session 对象
s = requests.Session()

# 通过 Session 对象 发送请求
response = s.post("http://127.0.0.1/api/mgr/signin",
       data={
           'username': 'byhy',
           'password': '88888888'
       })

printResponse(response)

# 通过 Session 对象 发送请求
response = s.get("http://127.0.0.1/api/mgr/customers",
      params={
          'action'    :  'list_customer',
          'pagesize'  :  10,
          'pagenum'   :  1,
          'keywords'  :  '',
      })

printResponse(response)
```



<br>