$('.form-control').keyup(function(e) {
    if (this.value.length === this.maxLength) {
        let next = $(this).data('next');
        $('#n' + next).focus();
    }
});