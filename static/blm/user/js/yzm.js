$().ready(function () {
    code_draw();
    // 点击后刷新验证码
    $("#canvas").on('click', function () {
        code_draw();
    })
})
