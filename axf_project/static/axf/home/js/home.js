$(function () {
    //初始化
    init_top_swiper();
    init_menu_swiper();
})


function init_top_swiper() {
    var mySwiper = new Swiper('#topSwiper', {
        // direction: 'vertical',
        loop: true,
        autoplay:1000,
        // 如果需要分页器
        pagination: '.swiper-pagination',

        // 如果需要前进后退按钮
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
    })
}

function init_menu_swiper() {
    var mySwiper = new Swiper('#swiperMenu', {
        slidesPerView: 3,
    })
}