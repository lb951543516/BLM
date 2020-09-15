var user_Boolean = false;
var password_Boolean = false;
var varconfirm_Boolean = false;
var email_Boolean = false;
var yzm_Boolean = false;
var Mobile_Boolean = false;

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
    });
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
    });
// password_confirm
    $('#reg_confirm').blur(function () {
        if (($("#reg_password").val()) == ($("#reg_confirm").val())) {
            $('.confirm_hint').html("✔").css("color", "green");
            $('#toast').attr("disabled", false);
            varconfirm_Boolean = true;
        } else {
            $('.confirm_hint').html("×").css("color", "red");
            $('#toast').attr("disabled", true);
            varconfirm_Boolean = false;
        }
    });

// Email
    $('#reg_email').blur(function () {
        if ((/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/).test($("#reg_email").val())) {
            $('.email_hint').html("✔").css("color", "green");
            $('#toast').attr("disabled", false);
            email_Boolean = true;
        } else {
            $('.email_hint').html("×").css("color", "red");
            $('#toast').attr("disabled", true);
            email_Boolean = false;
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
            $('#toast').attr("disabled", true);
            yzm_Boolean = false;
            draw(show_num);
        } else if (val == num) {
            $('.yzm_hint').html("✔").css("color", "green");
            $('#toast').attr("disabled", false);
            yzm_Boolean = true;
            draw(show_num);
        }
    })


// phone
    $('#reg_phone').blur(function () {
        if ((/^1[34578]\d{9}$/).test($("#reg_phone").val())) {
            $('.phone_hint').html("✔").css("color", "green");
            $('#toast').attr("disabled", false);
            Mobile_Boolean = true;
        } else {
            $('.phone_hint').html("×").css("color", "red");
            $('#toast').attr("disabled", true);
            Mobile_Boolean = false;
        }
    })

    //前端密码加密(base64)并提交
    $('#toast').click(function () {
        var un = $('#reg_user').val()
        var pwd = $('#reg_password').val()
        var cpwd = $('#reg_confirm').val()
        var phone = $('#reg_phone').val()
        var email = $('#reg_email').val()

        if (user_Boolean && password_Boolean && varconfirm_Boolean && email_Boolean && Mobile_Boolean && yzm_Boolean == true) {
            //加密
            var bas = new Base64();
            var hash = bas.encode(pwd);
            var hash2 = bas.encode(cpwd);
            $("#reg_password").val(hash);
            $("#reg_confirm").val(hash2);

            //解密
            //var str = bas.decode(hash);
            //$("#password").val(str);

            //获取登陆信息
            var formData = new FormData()
            formData.append('username', un)
            formData.append('password', pwd)
            formData.append('c_password', cpwd)
            formData.append('phone', phone)
            formData.append('email', email)
            // 提交登陆信息
            $.ajax({
                type: 'POST',
                url: '/user/register/',
                data: formData,
                datatype: "json",
                processData: false,
                contentType: false,
                success: function (data) {
                    if (data.msg == '密码有误！！') {
                        alert('密码有误！！');
                        $("#reg_password").val('');
                        $("#reg_confirm").val('');
                    } else if (data.msg == '用户名已存在或有误！') {
                        alert('用户名已存在或有误！');
                        $("#reg_password").val('');
                        $("#reg_confirm").val('');
                    } else if (data.msg == '手机号已被绑定或有误！') {
                        alert('手机号已被绑定！');
                        $("#reg_password").val('');
                        $("#reg_confirm").val('');
                    } else if (data.msg == '邮箱已被绑定或有误！') {
                        alert('邮箱已被绑定！');
                        $("#reg_password").val('');
                        $("#reg_confirm").val('');
                    } else {
                        window.location.href = '/user/login/';
                    }
                }
            })
        } else {
            alert("请完善信息");
        }
    })
})
