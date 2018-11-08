# Django的csrf中间件

​	CSRF：跨站请求伪造Cross Site Request Forgery



# CSRF的攻击流程

用户a 访问可信站点1做业务处理，此时浏览器会保存该网站的cookie，当用户a 访问不可信站点2时，如果站点2有指向站点1的链接时候，那么攻击就用可能发生

Eg:

1、包含站点1的链接，点击跳转

2、mg 的src属性值是站点1的链接

3、Js加载，js里有跳转的动作



# Django的解决方法

Django预防CSRF攻击的方法是在用户提交的表单中加入一个csrftoken的隐含值，这个值和服务器中保存的csrftoken的值相同

# 前后端的使用

## 后端

全局使用（禁用）

局部使用或禁用

from django.views.decorators.csrf import csrf_exempt（不使用CSRF验证）, csrf_protect（使用CSRF校验）

## 前端

Form表单

Ajax  方式

~~~
<script src="//cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>

<script src="//cdn.bootcss.com/jquery-cookie/1.4.1/jquery.cookie.js"></script>

~~~

