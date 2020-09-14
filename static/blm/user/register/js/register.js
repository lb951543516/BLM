var user_Boolean = false;
var password_Boolean = false;
var varconfirm_Boolean = false;
// var emaile_Boolean = false;
var yzm_Boolean = false;
var Mobile_Boolean = false;


$('#reg_user').blur(function () {
    if ((/^[a-zA-Z0-9_-]{6,12}$/).test($("#reg_user").val())) {
        $('.user_hint').html("✔").css("color", "green");
        user_Boolean = true;
    } else {
        $('.user_hint').html("×").css("color", "red");
        user_Boolean = false;
    }
});
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

//
// // Email
// $('.reg_email').blur(function(){
//   if ((/^[a-z\d]+(\.[a-z\d]+)*@([\da-z](-[\da-z])?)+(\.{1,2}[a-z]+)+$/).test($(".reg_email").val())){
//     $('.email_hint').html("✔").css("color","green");
//     emaile_Boolean = true;
//   }else {
//     $('.email_hint').html("×").css("color","red");
//     emaile_Boolean = false;
//   }
// });

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


// phone
$('#reg_phone').blur(function () {
    if ((/^1[34578]\d{9}$/).test($("#reg_phone").val())) {
        $('.phone_hint').html("✔").css("color", "green");
        Mobile_Boolean = true;
    } else {
        $('.phone_hint').html("×").css("color", "red");
        Mobile_Boolean = false;
    }
});


// click
$('.red_button').click(function () {
    if (user_Boolean && password_Boolea && varconfirm_Boolean && emaile_Boolean && Mobile_Boolean == true) {
        alert("注册成功");
    } else {
        alert("请完善信息");
    }
});
