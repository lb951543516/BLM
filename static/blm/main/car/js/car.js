$(function () {
//    点击 加号添加到购物车
    $('.add').click(function () {
        //    获取id
        var c_id = $(this).attr('c_id')
        var $button = $(this)
        $.get('/blmcar/addgood/',
            {'c_id': c_id},
            function (data) {
                $button.prev().text(data['g_num'])
                $('#pay_money').html(data['money'])
            }
        )
        // window.location.href = '/blmcar/car/';
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
                $('#pay_money').html(data['money'])
            }
        )
        // window.location.href = '/blmcar/car/';
    })

    //     修改单选的状态
    $('.confirm').click(function () {
        var $div = $(this);
        var c_id = $div.parent().attr('c_id');
        $.post(
            '/blmcar/changestatus/',
            {'c_id': c_id},
            function (data) {
                if (data['car.is_buy']) {
                    $div.find('span').find('span').html('✔');
                    $('#pay_money').html(data['money'])
                } else {
                    $div.find('span').find('span').html('');
                    $('#pay_money').html(data['money'])
                }
                if (data['is_all_buy']) {
                    $('.all_select').find('span').html('✔');
                    $('#pay_money').html(data['money'])
                } else {
                    $('.all_select').find('span').html('');
                    $('#pay_money').html(data['money'])
                }
            }
        )
        // window.location.href = '/blmcar/car/';
    })


    //     修改全选框的状态
    $('.all_select').click(function () {

        var select_list = [];
        var unselect_list = [];

        $('.confirm').each(function () {
            var c_id = $(this).parent().attr('c_id');
            if ($(this).find('span').find('span').html()) {
                select_list.push(c_id);
            } else {
                unselect_list.push(c_id);
            }
        })

        if (unselect_list.length == 0) {
            $.ajax({
                url: '/blmcar/allselect/',
                data: {'c_id_list': select_list.join('#')},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    $('.confirm').find('span').find('span').html('');
                    $('.all_select').find('span').html('');
                    $('#pay_money').html(data['money'])
                }
            })
            // window.location.href = '/blmcar/car/';
        } else {
            $.ajax({
                url: '/blmcar/allselect/',
                data: {'c_id_list': unselect_list.join('#')},
                type: 'GET',
                dataType: 'json',
                success: function (data) {
                    $('.confirm').find('span').find('span').html('✔');
                    $('.all_select').find('span').html('✔');
                    $('#pay_money').html(data['money'])
                }
            })
            // window.location.href = '/blmcar/car/';
        }
    })


})