$(document).ready(function() {

    $('.form-control').on('keypress', function(event) {
        var charCode = event.which;
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122))) {
            event.preventDefault();
        }
    });
    
    $('.form-control').on('keyup', function(event) {
        if ($(this).val()) {
            $(this).next().focus();
        }
        else if ($(this).val() === "" && event.which === 8) {
            $(this).prev('.form-control').focus();
        }
    });

    $('.botao').on('click', function() {
        var dados = {};

        $('.form-control').each(function() {
            dados[$(this).attr('id')] = $(this).val();
        });

        $.ajax({
            type: 'POST',
            url: '/salvar_dados/',
            data: dados,
            success: function(response) {
                alert(response.mensagem);
            },
            error: function(xhr, status, error) {
                alert('Erro ao salvar os dados: ' + error);
            }
        });
    });

    
});
