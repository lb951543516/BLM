var user_Boolean = false;
var Mobile_Boolean = false;
var address_Boolean = false;

$(function () {
// username
    $('#reg_consignee').blur(function () {
        if ((/^[\u4E00-\u9FA5A-Za-z0-9_]{1,10}$/).test($("#reg_consignee").val())) {
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
    })
})
