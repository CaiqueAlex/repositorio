$('.form-control').on('keyup', function(k) {
    if ($(this).val()) {
        $(this).next().focus();
    }
    if ($(this).val() === "" && k.which === 8) {
        $(this).prev('.form-control').focus();
    }
});
