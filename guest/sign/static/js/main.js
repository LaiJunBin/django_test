$(function () {
    $(".nav-item>a").each(function () {
        if ($(this).attr('href') == location.pathname) {
            $(this).parent().addClass('active')
        }
    })
})