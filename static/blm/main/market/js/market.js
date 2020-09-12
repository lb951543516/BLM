$(function () {
    $('.content').css('height', $('.right').height());
    $('.left ul li').eq(0).addClass('active');

    //当前浏览器窗口添加滚动事件
    $(window).scroll(function () {
        //滚动条的垂直偏移量
        if ($(window).scrollTop() >= 40) {
            $('.swiper-container-ul').css('position', 'fixed');
            $('#all_type_container').css('top', '40px');
            $('.left').css('position', 'fixed');
            $('.right').css('margin-left', $('.left').width());
        } else {
            $('.swiper-container-ul').css('position', '');
            $('#all_type_container').css('top', '80px');
            $('.left').css('position', '');
            $('.right').css('margin-left', '');
        }
        ;
        //滚动到标杆位置,左侧导航加active
        $('.right ul li').each(function () {
            var target = parseInt($(this).offset().top - $(window).scrollTop() - 40);
            //alert(target);
            var i = $(this).index();
            if (target <= 0) {
                $('.left ul li').removeClass('active');
                $('.left ul li').eq(i).addClass('active');
            }
        });
    });
    $('.left ul li').click(function () {
        var i = $(this).index('.left ul li');
        $('body, html').animate({scrollTop: $('.right ul li').eq(i).offset().top - 40}, 500);
    });
});


//分类 排序 按钮
$(function () {
    $('#all_type').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');
        $('#all_type_container').toggle();
    })

    $('#sort_rule').click(function () {
        $(this).find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down');
        $('#type_sort_container').toggle();
    })
})