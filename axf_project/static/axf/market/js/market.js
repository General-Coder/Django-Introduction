var cate_toggle_tag = false;
var sort_toggle_tag = false;

$(function () {
    // 全部类型添加点击时间
    $('#all_cate').click(cate_toggle);
    $('#cates').click(cate_toggle);


    //排序
    $('#all_sort').click(sort_toggle);
    $('#shorts').click(sort_toggle);

    //加操作
    $('.addShopping').click(function () {
        $current_bt = $(this);
        //获取点击的商品id
        var g_id = $current_bt.attr('g_id');
        $.ajax({
            url:'/axf/cart_api',
            data:{
                'g_id':g_id,
                'type':'add'
            },
            method:'post',
            success:function (res) {
                if(res.code==2){
                    window.open(res.data,target="_self")
                }else if(res.code==1){
                    $current_bt.prev('span').html(res.data)
                }
            }

        })
    })
    $('.subShopping').click(function () {
        $current_bt = $(this);
        var g_id = $current_bt.attr('g_id');
        //判断当前现实的是否为0，是0就return，不发送请求
        if($current_bt.next('span').html() == 0){
            return;
        }
        $.ajax({
             url:'/axf/cart_api',
            data:{
                'g_id':g_id,
                'type':'sub'
            },
            method:'post',
            success:function (res) {
                if(res.code==2){
                    window.open(res.data,target="_self")
                }else if(res.code==1){
                    $current_bt.next('span').html(res.data)
                }
            }
        })
    })



});

function cate_toggle() {
    $('#cates').toggle();
    if(cate_toggle_tag == false){
         $(this).find('span').removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up");
        cate_toggle_tag = true;
    }else{
         $(this).find('span').removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down");
        cate_toggle_tag = false;
    }
}

function sort_toggle() {
    $('#sorts').toggle();
    if (sort_toggle_tag==false){
        $(this).find('span').removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up");
        sort_toggle_tag = true;
    } else {
         $(this).find('span').removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down");
        sort_toggle_tag = false
    }
}