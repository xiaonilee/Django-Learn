$(function () {
    $('img').click(function () {
        console.log('clicked it');
        $(this).attr('src', '/app/getcode/?t=' + Math.random());

    })
})