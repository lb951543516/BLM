var user_Boolean = false;
var password_Boolean = false;
var varconfirm_Boolean = false;
// var emaile_Boolean = false;
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


// // click
// $('.red_button').click(function () {
//     if (user_Boolean && password_Boolea && varconfirm_Boolean && emaile_Boolean && Mobile_Boolean == true) {
//         alert("注册成功");
//     } else {
//         alert("请完善信息");
//     }
// });
