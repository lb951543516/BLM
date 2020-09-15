function ImgUpload(node, width, height, linHeight) {
    var _this = this;
    this._node = node;
    this.width = width + 'px';
    this.height = height + 'px';
    this.linHeight = linHeight + 'px';
    this.setCss();
    this.createFile();
}

ImgUpload.prototype.createFile = function () {
    $(this._node).append('<input type="file" name="header"/>')
}

ImgUpload.prototype.setCss = function () {
    $(this._node).css({
        "width": this.width,
        "height": this.height,
        "line-height": this.linHeight,
    })
}

ImgUpload.prototype.setSpan = function (_this) {
    $(_this).siblings().css("opacity", 0);
}


$(function () {
    var img2 = new ImgUpload('.imgLog2', 100, 100, 100);

    $(document).on('change', ".imgLog2 input", function (e) {
        //模拟后台返回url
        var url = window.URL.createObjectURL(e.target.files[0]);
        $(this).parent().css('background', 'url(' + url + ')0% 0% / cover')
        img2.setSpan(this)
    })

})
