var user_Boolean = false;
var password_Boolean = false;
// var varconfirm_Boolean = false;
// var emaile_Boolean = false;
// var yzm_Boolean = false;
// var Mobile_Boolean = false;

$(function () {
// username
    $('#reg_user').blur(function () {
        if ((/^[a-zA-Z0-9_-]{6,12}$/).test($("#reg_user").val())) {
            $('.user_hint').html("✔").css("color", "green");
            $('#toast').attr("disabled", false);
            user_Boolean = true;
        } else {
            $('.user_hint').html("×").css("color", "red");
            $('#toast').attr("disabled", true);
            user_Boolean = false;
        }
    })
// password
    $('#reg_password').blur(function () {
        if ((/^[a-zA-Z0-9_-]{6,12}$/).test($("#reg_password").val())) {
            $('.password_hint').html("✔").css("color", "green");
            $('#toast').attr("disabled", false);
            password_Boolean = true;
        } else {
            $('.password_hint').html("×").css("color", "red");
            $('#toast').attr("disabled", true);
            password_Boolean = false;
        }
    })


    //前端密码加密(base64)并提交
    $('#toast').click(function () {
        var un = $('#reg_user').val()
        var pwd = $('#reg_password').val()

        if (un == '') {
            alert('请输入用户名！')
        } else if (pwd == '') {
            alert('请输入密码！')
        } else {
            //加密
            var bas = new Base64();
            var hash = bas.encode(pwd);
            $("#reg_password").val(hash);

            //解密
            //var str = bas.decode(hash);
            //$("#password").val(str);

            //获取登陆信息
            var formData = new FormData()
            formData.append('username', un)
            formData.append('password', pwd)
            // 提交登陆信息
            $.ajax({
                type: 'POST',
                url: '/user/login/',
                data: formData,
                datatype: "json",
                processData: false,
                contentType: false,
                success: function (data) {
                    if (data.msg == '用户名有误！') {
                        alert('用户名有误！');
                        $("#reg_password").val('');
                    } else if (data.msg == '密码有误！') {
                        alert('密码有误！');
                        $("#reg_password").val('');
                    } else {
                        window.location.href = '/blmmine/mine/';
                    }
                }
            })
        }
    })
})
