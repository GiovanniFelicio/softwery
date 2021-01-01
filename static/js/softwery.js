$(function () {
    'use strict'

    $('.modal-dialog').draggable({
        handle: ".modal-header"
    });

    $('.checkIfExists').on('change', function(){
        let url = `${$(this).attr('data-url')}?value=${$(this).val()}&field=${$(this).prop('name')}`;
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'json',
            contentType: 'application/json',
            success: function (data) {
                console.log(data);
            },
            error: function(data) {
                console.log(data)
            }
        });
    });
})
