# Django的csrf中间件

​	CSRF：跨站请求伪造Cross Site Request Forgery



# CSRF的攻击流程

用户a 访问可信站点1做业务处理，此时浏览器会保存该网站的cookie，当用户a 访问不可信站点2时，如果站点2有指向站点1的链接时候，那么攻击就用可能发生

Eg:

1、包含站点1的链接，点击跳转

2、img 的src属性值是站点1的链接

3、Js加载，js里有跳转的动作



# Django的解决方法

Django预防CSRF攻击的方法是在用户提交的表单中加入一个csrftoken的隐含值，这个值和服务器中保存的csrftoken的值相同

# 前后端的使用

## 后端

全局使用（禁用）

​	使用中间件操作

局部使用或禁用

from django.views.decorators.csrf import csrf_exempt（不使用CSRF验证）, csrf_protect（使用CSRF校验）

## 前端

Form表单

{%csrf_token%}

Ajax  方式



~~~
<script src="//cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>

<script src="//cdn.bootcss.com/jquery-cookie/1.4.1/jquery.cookie.js"></script>

~~~

~~~
function submit() {
    {#    拿数据#}
        var name = $("#name").val();
        var num = $("#num").val();
        var csrf_token = $.cookie("csrftoken");
        console.log(csrf_token);
        $.ajax({
            url:"/t08/cz",
            data:{
                "name": name,
                "num": num,
                "csrfmiddlewaretoken": csrf_token
            },
            method:"post",
            success: function (res) {
                console.log(res);
            }
        })
    }
~~~

面试回答：

​	1 什么是：跨站请求伪造Cross Site Request Forgery

​	2 举例子：什么是跨站请求攻击：用户a 访问可信站点1做业务处理，此时浏览器会保存该网站的cookie，当用户a 访问不可信站点2时，如果站点2有指向站点1的链接时候，那么攻击就用可能发生

​	3 Django怎么做的：使用了csrf的中间件，具体操作是这样的，当浏览器第一次和Django服务交互的时候，

​		后台会生成一个唯一标识码， 放入到前端，同时后台也保存，那么之后再提交数据 服务端就会做csrf的校验，如果通过那么就正常处理，否则返回403

​	4 使用： **后端**

全局使用（禁用）

​	使用中间件操作

局部使用或禁用

from django.views.decorators.csrf import csrf_exempt（不使用CSRF验证）, csrf_protect（使用CSRF校验）

**前端**

Form表单

{%csrf_token%}

Ajax  方式

