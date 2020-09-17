$(function () {
        var user_Boolean = false;
        var password_Boolean = false;
        var varconfirm_Boolean = false;
        var email_Boolean = false;
        var yzm_Boolean = false;
        var Mobile_Boolean = false;

// username
        $('#reg_user').blur(function () {
            if ((/^[a-zA-Z0-9_-]{6,12}$/).test($("#reg_user").val())) {
                var un = $('#reg_user').val()
                //获取登陆信息
                var formData = new FormData()
                formData.append('username', un)
                $.ajax({
                    type: 'POST',
                    url: '/user/regcheck/',
                    data: formData,
                    datatype: "json",
                    processData: false,
                    contentType: false,
                    success: function (data) {
                        if (data['msg'] == '用户名已存在或有误！') {
                            $('.user_hint').html("×").css("color", "red");
                            user_Boolean = false;
                        } else {
                            $('.user_hint').html("✔").css("color", "green");
                            user_Boolean = true;
                        }
                    }
                })
            } else {
                $('.user_hint').html("×").css("color", "red");
                user_Boolean = false;
            }
        })

// phone
        $('#reg_phone').blur(function () {
            if ((/^1[34578]\d{9}$/).test($("#reg_phone").val())) {
                var phone = $('#reg_phone').val()
                //获取登陆信息
                var formData = new FormData()
                formData.append('phone', phone)
                $.ajax({
                    type: 'POST',
                    url: '/user/regcheck/',
                    data: formData,
                    datatype: "json",
                    processData: false,
                    contentType: false,
                    success: function (data) {
                        if (data['msg'] == '手机号已被绑定或有误！') {
                            $('.phone_hint').html("×").css("color", "red");
                            Mobile_Boolean = false;
                        } else {
                            $('.phone_hint').html("✔").css("color", "green");
                            Mobile_Boolean = true;
                        }
                    }
                })
            } else {
                $('.phone_hint').html("×").css("color", "red");
                Mobile_Boolean = false;
            }
        })

// Email
        $('#reg_email').blur(function () {
            if ((/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/).test($("#reg_email").val())) {
                var email = $('#reg_email').val()
                //获取登陆信息
                var formData = new FormData()
                formData.append('email', email)
                $.ajax({
                    type: 'POST',
                    url: '/user/regcheck/',
                    data: formData,
                    datatype: "json",
                    processData: false,
                    contentType: false,
                    success: function (data) {
                        if (data['msg'] == '邮箱已被绑定或有误！') {
                            $('.email_hint').html("×").css("color", "red");
                            email_Boolean = false;
                        } else {
                            $('.email_hint').html("✔").css("color", "green");
                            email_Boolean = true;
                        }
                    }
                })
            } else {
                $('.email_hint').html("×").css("color", "red");
                email_Boolean = false;
            }
        })


// password
        $('#reg_password').blur(function () {
            if ((/^[a-zA-Z0-9_-]{6,12}$/).test($("#reg_password").val())) {
                $('.password_hint').html("✔").css("color", "green");
                password_Boolean = true;
            } else {
                $('.password_hint').html("×").css("color", "red");
                password_Boolean = false;
            }
        });
// password_confirm
        $('#reg_confirm').blur(function () {
            if (($("#reg_password").val()) == ($("#reg_confirm").val())) {
                $('.confirm_hint').html("✔").css("color", "green");
                varconfirm_Boolean = true;
            } else {
                $('.confirm_hint').html("×").css("color", "red");
                varconfirm_Boolean = false;
            }
        });
//验证码
        $().ready(function () {
            code_draw();
            // 点击后刷新验证码
            $("#canvas").on('click', function () {
                code_draw();
            })
        })
        $("#reg_yzm").blur(function () {
            // 将输入的内容转为大写，可通过这步进行大小写验证
            var val = $("#reg_yzm").val().toLowerCase();
            // 获取生成验证码值
            var num = $('#canvas').attr('data-code');

            if (val != num) {
                $('.yzm_hint').html("×").css("color", "red");
                yzm_Boolean = false;
                draw(show_num);
            } else if (val == num) {
                $('.yzm_hint').html("✔").css("color", "green");
                yzm_Boolean = true;
                draw(show_num);
            }
        })


//前端密码加密(base64),,表单的submit事件的返回值 只有为true的时候 才可以提交表单
        $('form').submit(function () {
            var result = user_Boolean & password_Boolean & varconfirm_Boolean & email_Boolean & Mobile_Boolean & yzm_Boolean

            if (result == 1) {
                var pwd = $('#reg_password').val()
                var cpwd = $('#reg_confirm').val()

                // //md5加密
                // new_pwd = md5(pwd)
                // new_cpwd = md5(cpwd)
                // $("#reg_password").val(new_pwd);
                // $("#reg_confirm").val(new_cpwd);

                // //base64加密
                // var bas = new Base64();
                // var hash = bas.encode(pwd);
                // var hash2 = bas.encode(cpwd);
                // // $("#reg_password").val(hash);
                // // $("#reg_confirm").val(hash2);
                // //base64解密
                // //var str = bas.decode(hash);
                // //$("#password").val(str);


                return true
            } else {
                alert("请完善信息")
                $("#reg_password").val('');
                $("#reg_confirm").val('');
                return false
            }
        })
    }
)
