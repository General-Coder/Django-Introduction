$(function () {
   $('#sub').click(login)
});

function login() {
    //拿到用户输入
    var name = $('#u_id').val();
    var pwd = $('#u_pwd').val();
    //校验数据格式
    if(name.length < 3){
        alert('用户名过短');
        return;
    }
    if (pwd.length < 6){
        alert('密码过短');
        return;
    }
    //给密码作md5
    var enc_pwd = md5(pwd);
    $.ajax({
        url:'/axf/login',
        data:{
            'name':name,
            'pwd':enc_pwd
        },
        method:'post',
        success:function (res) {
            //成功跳转mine页面
            if(res.code == 1){
                window.open(res.data,target='_self');
            }else{
                alert(res.msg)
            }
        },
        error:function () {

        },
        complete:function () {
          //请求完成时，不管成功失败
        }
    })
}