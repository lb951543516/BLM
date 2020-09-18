$(function () {

    var user_Boolean = false;
    var password_Boolean = false;

    $('#log_user').blur(function () {
        if ($("#log_user").val().length > 0) {
            user_Boolean = true
        } else {
            user_Boolean = false
        }
    })

    $('#log_password').blur(function () {
        if ($("#log_password").val().length > 0) {
            password_Boolean = true
        } else {
            password_Boolean = false
        }
    })

    $('form').submit(function () {
        var result = user_Boolean & password_Boolean

        if (result == 1) {
            var pwd = $('#log_password').val()

            //md5加密
            new_pwd = md5(pwd)
            $("#log_password").val(new_pwd);


            // //base64加密
            // var bas = new Base64();
            // var hash = bas.encode(pwd);
            // // $("#log_password").val(hash);
            // //base64解密
            // //var str = bas.decode(hash);
            // //$("#password").val(str);
            return true
        } else {
            alert("请完善信息")
            $("#log_password").val('');
            password_Boolean = false
            return false
        }
    })

})