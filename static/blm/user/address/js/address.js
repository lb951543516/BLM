var user_Boolean = false;
var Mobile_Boolean = false;
var address_Boolean = false;

$(function () {
// username
    $('#reg_consignee').blur(function () {
        if ((/^[\u4E00-\u9FA5A-Za-z0-9_]{2,10}$/).test($("#reg_consignee").val())) {
            $('.consignee_hint').html("✔").css("color", "green");
            user_Boolean = true;
        } else {
            $('.consignee_hint').html("×").css("color", "red");
            user_Boolean = false;
        }
    });
// address
    $('#reg_address').blur(function () {
        if ($("#reg_address").val()) {
            $('.address_hint').html("✔").css("color", "green");
            address_Boolean = true;
        } else {
            $('.address_hint').html("×").css("color", "red");
            address_Boolean = false;
        }
    });
// phone
    $('#reg_phone').blur(function () {
        if ((/^1[34578]\d{9}$/).test($("#reg_phone").val())) {
            $('.phone_hint').html("✔").css("color", "green");
            Mobile_Boolean = true;
        } else {
            $('.phone_hint').html("×").css("color", "red");
            Mobile_Boolean = false;
        }
    })

    $('.form-control').blur(function () {
        if (user_Boolean && address_Boolean && Mobile_Boolean == true) {
            $('#toast').attr("disabled", false);
        } else {
            $('#toast').attr("disabled", true);
        }
    });

    //
    // //前端密码加密(base64)并提交
    // $('#toast').click(function () {
    //     var un = $('#reg_user').val()
    //     var pwd = $('#reg_password').val()
    //     var cpwd = $('#reg_confirm').val()
    //     var phone = $('#reg_phone').val()
    //     var email = $('#reg_email').val()
    //
    //     if (user_Boolean && password_Boolean && varconfirm_Boolean && email_Boolean && Mobile_Boolean && yzm_Boolean == true) {
    //         //加密
    //         var bas = new Base64();
    //         var hash = bas.encode(pwd);
    //         var hash2 = bas.encode(cpwd);
    //         $("#reg_password").val(hash);
    //         $("#reg_confirm").val(hash2);
    //
    //         //解密
    //         //var str = bas.decode(hash);
    //         //$("#password").val(str);
    //
    //         //获取登陆信息
    //         var formData = new FormData()
    //         formData.append('username', un)
    //         formData.append('password', pwd)
    //         formData.append('c_password', cpwd)
    //         formData.append('phone', phone)
    //         formData.append('email', email)
    //         // 提交登陆信息
    //         $.ajax({
    //             type: 'POST',
    //             url: '/user/register/',
    //             data: formData,
    //             datatype: "json",
    //             processData: false,
    //             contentType: false,
    //             success: function (data) {
    //                 if (data.msg == '密码有误！！') {
    //                     alert('密码有误！！');
    //                     $("#reg_password").val('');
    //                     $("#reg_confirm").val('');
    //                 } else if (data.msg == '用户名已存在或有误！') {
    //                     alert('用户名已存在或有误！');
    //                     $("#reg_password").val('');
    //                     $("#reg_confirm").val('');
    //                 } else if (data.msg == '手机号已被绑定或有误！') {
    //                     alert('手机号已被绑定！');
    //                     $("#reg_password").val('');
    //                     $("#reg_confirm").val('');
    //                 } else if (data.msg == '邮箱已被绑定或有误！') {
    //                     alert('邮箱已被绑定！');
    //                     $("#reg_password").val('');
    //                     $("#reg_confirm").val('');
    //                 } else {
    //                     window.location.href = '/user/login/';
    //                 }
    //             }
    //         })
    //     } else {
    //         alert("请完善信息");
    //     }
    // })
})
