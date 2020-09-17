//    点击 加号添加到购物车
$('.add').click(function () {
    //    获取id
    var c_id = $(this).attr('c_id')
    var $button = $(this)
    $.get('/blmcar/addgood/',
        {'c_id': c_id},
        function (data) {
            $button.prev().text(data['g_num'])
        }
    )
    window.location.href = '/blmcar/car/';
})
//    点击 减号添加到购物车
$('.reduce').click(function () {
    //    获取id
    var c_id = $(this).attr('c_id')
    var button = $(this)
    $.get('/blmcar/reducegood/',
        {'c_id': c_id},
        function (data) {
            button.next().text(data['g_num'])
        }
    )
    window.location.href = '/blmcar/car/';
})