

## 学习准备



本教程讲解过程中，需要使用  ```白月SMS系统```  进行演示，请大家按照如下 方法 下载运行 ：

### 下载白月SMS系统

<a href='https://pan.baidu.com/s/1rnWhuroIMNebStzpwLjsTA' target='_blank'>点击百度网盘链接</a> ，下载 白月SMS系统 压缩包 bysms.zip 


下载解压bysms.zip后，进入bysms目录，双击运行runserver.bat 即可启动 白月SMS系统。 出现下面这样的信息

```
\bysms\bysms>bysms.exe runserver 80
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 2 unapplied migration(s). Your project may not work properly 
until you apply the migrations for app(s): auth.
Run 'python manage.py migrate' to apply them.
September 07, 2019 - 22:22:19
Django version 2.2.4, using settings 'bysms.settings'
Starting development server at http://127.0.0.1:80/
Quit the server with CTRL-BREAK.
```

注意：该窗口不能关闭，否则web 系统就会停止

 
然后可以浏览器访问 登录页面 http://127.0.0.1/mgr/sign.html

输入如下管理员账号

用户名 ：byhy
密码： 88888888

即可登录


## HTTP协议简介


<br>

<a href='https://www.bilibili.com/video/av68746921/?p=1' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>

WEB API接口 大都是基于 HTTP 协议的，所以，要进行接口测试 首先要了解 HTTP 协议 的 基础知识。

HTTP 协议 全称是 超文本传输协议，  英文是 Hypertext Transfer Protocol 。 

HTTP 最初是用来 在 浏览器和 网站服务器（web服务）之间 传输超文本（网页、视频、图片等）信息的。 

由于 HTTP 简洁易用，后来，不仅仅是浏览器 和 服务器之间 使用它， 服务器和服务器之间， 手机App 和 服务器之间， 都广泛的采用。 成了一个软件系统间 通信 的首选协议 之一。

HTTP 有好几个版本，包括： 0.9、1.0、1.1、2，当前最广泛使用的是 HTTP/1.1 版本。



HTTP 协议最大的特点是 通讯双方 分为  ```客户端``` 和 ```服务端``` 。

由于 目前 HTTP是基于 TCP 协议的， 所以要进行通讯，客户端 必须先 和服务端 创建 TCP 连接。

而且 HTTP 双方的信息交互，必须是这样一种方式： 

- 客户端  先发送 http请求（request）给 服务端
  
- 然后服务端 发送 http响应（response）给 客户端


特别注意：HTTP协议中，服务端不能主动先发送信息给 客户端。

而且在1.1 以前的版本， 服务端 返回响应给客户端后，连接就会 断开 ，下一次双方要进行信息交流，必须重复上面的过程，重新建立连接，客户端发送请求，服务返回响应。

到了 1.1 版本， 建立连接后，这个连接可以保持一段时间（keep alive）， 这段时间，双方可以多次进行 请求和响应， 无需重新建立连接。


---

如果客户端是浏览器，如何在chrome浏览器中查看 请求和响应的HTTP消息，请参考视频讲解

---


## HTTP请求消息


<br>

<a href='https://www.bilibili.com/video/av68746921/?p=2' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>

下面是2个http请求消息的示例

```yml
GET /mgr/login.html HTTP/1.1
Host: www.baiyueheiyu.com
User-Agent: Mozilla/6.0 (compatible; MSIE5.01; Windows NT)
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate
```


```yml
POST /api/medicine HTTP/1.1
Host: www.baiyueheiyu.com
User-Agent: Mozilla/6.0 (compatible; MSIE5.01; Windows NT)
Content-Type: application/x-www-form-urlencoded
Content-Length: 51
Accept-Language: zh-cn
Accept-Encoding: gzip, deflate

name=qingmeisu&sn=099877883837&desc=qingmeisuyaopin
```

http请求消息由下面几个部分组成

###  请求行 request line
  
是http请求的第一行的内容，表示要操作什么资源，使用的 http协议版本是什么。

里面包含了3部分信息： 请求的方法，操作资源的地址， 协议的版本号

例如

```py
GET /mgr/login.html HTTP/1.1
```

表示要  ```获取``` 资源， 资源的 ```地址 ``` 是  ```/mgr/login.html``` ， 使用的 ```协议``` 是  ```HTTP/1.1``` 

而 

```py
POST /api/medicine HTTP/1.1
```

表示  ```添加``` 资源信息， 添加资源 到 地址  ```/api/medicine``` ， 使用的 ```协议``` 是  ```HTTP/1.1``` 


GET、POST是请求的方法，表示这个动作的大体目的，是获取信息，还是提交信息，还是修改信息等等



常见的HTTP 请求方法包括：

- GET  
  
  从服务器  ```获取```  资源信息，这是一种最常见的请求。

  比如 要 从服务器 获取 网页资源、获取图片资源、获取用户信息数据等等。


- POST，请求方法就应该是 
  
   ```添加``` 资源信息 到 服务器进行处理（例如提交表单或者上传文件）。

  比如 要 添加用户信息、上传图片数据 到服务器 等等

  具体的数据信息，通常在 HTTP消息体中， 后面会讲到 


- PUT
  
  请求服务器  ```更新```  资源信息 。

  比如 要 更新  用户姓名、地址 等等

  具体的更新数据信息，通常在 HTTP消息体中， 后面会讲到 

- DELETE
  
  请求服务器  ```删除```  资源信息 。

  比如 要 删除 某个用户、某个药品 等等


HTTP还有许多其他方法，比如 PATCH、HEAD 等，不是特别常用，暂且不讲。


### 请求头 request headers


<br>

<a href='https://www.bilibili.com/video/av68746921/?p=3' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>


请求头是http请求行下面的 的内容，里面存放 一些 信息。

比如，请求发送的服务端域名是什么， 希望接收的响应消息使用什么语言，请求消息体的长度等等。

通常请求头 都有好多个，一个请求头 占据一行

单个请求头的 格式是：  ```名字: 值``` 

HTTP协议规定了一些标准的请求头，<a href='https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers' target='_blank'>点击查看MDN的描述</a>

开发者，也可以在HTTP消息中 添加自己定义的请求头


### 消息体 message body

<br>

<a href='https://www.bilibili.com/video/av68746921/?p=4' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>

请求的url、请求头中 可以存放 一些数据信息， 但是 有些数据信息，往往需要 存放在消息体中。

特别是 POST、PUT等请求，添加、修改的数据信息 通常都是 存放在 请求消息体 中的。

如果 HTTP 请求 有 消息体， 协议规定 需要在  消息头和消息体 之间 插入一个空行， 隔开 它们。


请求消息体中保存了要提交给服务端的数据信息。 


比如：客户端要上传一个文件给服务端，就可以通过HTTP请求发送文件数据给服务端。

文件的数据 就应该在请求的消息体中。


再比如：上面示例中 客户端要添加药品，药品的名称、编码、描述，就存放在请求消息体中。


WEB API 请求消息体 通常是某种格式的文本，常见的有

- Json
- Xml
- www-form-urlencoded

后面会有详细的讲述


## HTTP响应消息


<br>

<a href='https://www.bilibili.com/video/av68746921/?p=5' target='_blank'>点击这里，边看视频讲解，边学习以下内容</a>


下面是1个http响应消息的示例

```yml
HTTP/1.1 200 OK
Date: Thu, 19 Sep 2019 08:08:27 GMT
Server: WSGIServer/0.2 CPython/3.7.3
Content-Type: application/json
Content-Length: 37
X-Frame-Options: SAMEORIGIN
Vary: Cookie

{"ret": 0, "retlist": [], "total": 0}
```

HTTP响应消息包含如下几个部分

### 状态行 status line

状态行在第一行，包含3个部分：  

- 协议版本

  上面的示例中，就是  ```HTTP/1.1``` 

- 状态码 

  上面的示例中，就是  ```200``` 

- 描述状态的短语

  上面的示例中，就是  ```OK``` 


我们重点来看一下状态码，它表示了 服务端对客户端请求的处理结果 。

状态码用3位的数字来表示，第一位 的 数字代表 处理结果的 大体类型，常见的有如下几种：


•	2xx 

 通常 表示请求消息 没有问题，而且  服务器 也正确处理了

 最常见的就是 200



•	3xx

  这是重定向响应，常见的值是 301，302， 表示客户端的这个请求的url地址已经改变了， 需要 客户端 重新发起一个 请求 到另外的一个url。 


•	4xx

 表示客户端请求有错误， 常见的值有：

 ```400 Bad Request```   表示客户端请求不符合接口要求，比如格式完全错误

 ```401 Unauthorized```  表示客户端需要先认证才能发送次请求

 ```403 Forbidden```     表示客户端没有权限要求服务器处理这样的请求， 比如普通用户请求删除别人账号等

 ```404 Not Found```     表示客户端请求的url 不存在


•	5xx

 表示服务端在处理请求中，发生了未知的错误。

 通常是服务端的代码设计问题，或者是服务端子系统出了故障（比如数据库服务宕机了）


### 响应头 response headers


响应头 是 响应状态行下面的 的内容，里面存放 一些 信息。 作用 和 格式 与请求头类似，不再赘述。


### 消息体 message body


有时候，http响应需要消息体。

同样， 如果 HTTP 响应 有 消息体， 协议规定 需要在  消息头和消息体 之间 插入一个空行， 隔开 它们。

比如，白月SMS系统  请求 列出 药品 信息，那么 药品 信息 就在HTTP响应 消息体中

再 比如，浏览器地址栏 输入 登录网址，浏览器 请求一个登录网页的内容，网站服务器，就在响应的消息体中存放登录网页的html内容。

和请求消息体一样，WEB API 响应消息体 通常也是某种格式的文本，常见的有：

- Json
- Xml
- www-form-urlencoded

关于这些格式，我们会在后续课程中进行讲解


<br>

## 课后练习


### 题目1

根据教程 


- 下载运行白月SMS系统


- 练习用chrome浏览器查看 界面操作时，对应的 HTTP请求、响应消息的 各个组成部分，包括：
  
   ```py
   请求行
   请求消息头
   请求消息体
   响应行
   响应消息头
   响应消息体
   ```
