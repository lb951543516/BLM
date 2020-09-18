var user_Boolean = true;
var password_Boolean = true;
var varconfirm_Boolean = true;
var email_Boolean = true;
var Mobile_Boolean = true;

//nickname
$('#reg_nick').blur(function () {
    if ((/^.{0,20}$/).test($("#reg_nick").val())) {
        $('.nick_hint').html("✔").css("color", "green");
        user_Boolean = true;
    } else {
        $('.nick_hint').html("×").css("color", "red");
        user_Boolean = false;
    }
});
// password
$('#reg_password').blur(function () {
    if ((/^[a-zA-Z0-9_-]{6,12}$/).test($("#reg_password").val()) || $("#reg_password").val().length == 0) {
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


// Email
$('#reg_email').blur(function () {
    if ((/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/).test($("#reg_email").val())) {
        var email = $("#reg_email").val()
        $.ajax({
            type: 'GET',
            url: '/user/updatecheck/',
            data: {'email': email},
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
});

// phone
$('#reg_phone').blur(function () {
    if ((/^1[34578]\d{9}$/).test($("#reg_phone").val())) {
        var phone = $('#reg_phone').val()
        //获取登陆信息
        $.ajax({
            type: 'GET',
            url: '/user/updatecheck/',
            data: {'phone': phone},
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
});

// 点击头像进行上传，可以预览图片
$(function () {
    $('#reg_img').click(function () {
        $('#img-upload').click()
    })
})

function reads(obj) {
    var file = obj.files[0];
    var reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function (ev) {
        $("#reg_img").attr("src", ev.target.result);
    }
}


// ,表单的submit事件的返回值 只有为true的时候 才可以提交表单
$('form').submit(function () {
    var result = user_Boolean & password_Boolean & varconfirm_Boolean & email_Boolean & Mobile_Boolean

    if (result == 1) {
        var pwd = $('#reg_password').val()
        var cpwd = $('#reg_confirm').val()

        if (pwd.length > 0) {
            //md5加密
            new_pwd = md5(pwd)
            new_cpwd = md5(cpwd)
            $("#reg_password").val(new_pwd);
            $("#reg_confirm").val(new_cpwd);
        }

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