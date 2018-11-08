$(function () {
    $('#sub').click(function () {
        var u_tel = $('#u_tel').val();
        var u_addr = $('#u_addr').val();
        $.ajax({
            url:'/axf/change_user',
            data:{
                'u_tel':u_tel,
                'u_addr':u_addr
            },
            method:'post',
            success:function (res) {
                if(res.code==1){
                    window.open(res.data,target='_self')
                }
            }
        })
    })
});