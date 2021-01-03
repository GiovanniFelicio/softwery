$(function () {
    'use strict'

    $('.modal-dialog').draggable({
        handle: ".modal-header"
    });

    $('.check-if-exists').on('change', function(){
        let field = $(this);
        let nameField = field.prop('name');
        let url = `${field.attr('data-url')}?value=${field.val()}&field=${nameField}`;
        let parent = field.parent();
        $.ajax({
            url: url,
            type: 'GET',
            success: function (data) {
                $(field).removeClass('is-invalid');
                $(parent).find('div.invalid-feedback').remove()
                $(field).addClass('is-valid')
            },
            error: function(e) {
                $(field).removeClass('is-valid');
                $(field).addClass('is-invalid');                
                parent.append(`<div class="invalid-feedback">${nameField.charAt(0).toUpperCase() + nameField.slice(1)} is already being used</div>`)
            }
        });
    });
})

function isValidChar(str) {
    return !/[~`!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g.test(str);
}