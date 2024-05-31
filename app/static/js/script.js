$(document).ready(function() {
    let primeira_linha = document.getElementsByClassName("class_letra")[0]
    let linha_index = 0
    let linhaAtual = primeira_linha


    var tentativasRestantes = 6;
    
    // Impede a digitação de caracteres não alfabéticos nos campos de entrada
    $('.form-control').on('keypress', function(event) {
        var charCode = event.which;
        if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122))) {
            event.preventDefault();
        }
    });

    // Move o foco para o próximo campo ao preencher o atual
    $('.form-control').on('keyup', function(event) {
        if ($(this).val()) {
            $(this).next().focus();
        }
        else if ($(this).val() === "" && event.which === 8) {
            $(this).prev('.form-control').focus();
        }
    });

    $('#form1').on('submit', function(event) {
        event.preventDefault(); 

        var tentativa = '';
        $('.form-control').each(function() {
            tentativa += $(this).val(); 
        });

        var palavra_aleatoria = $('#board').data('palavra');
        var feedback = '';

        
        if (tentativa === palavra_aleatoria) {
            $('#answer').html('<span class="green">' + tentativa + '</span>');
            alert("Você ganhou!");
            window.history.back();
            return;
        }
        
        let filhos_linha = linhaAtual.children
        linha_index++
        linhaAtual = document.getElementsByClassName("class_letra")[linha_index]



        for (var i = 0; i < tentativa.length; i++) {
            if (tentativa[i] === palavra_aleatoria.charAt(i)) {
                filhos_linha[i].setAttribute("placeholder", tentativa[i]);
                filhos_linha[i].classList.add("correta")
                // Letra correta e no lugar certo (verde)
            } else if (palavra_aleatoria.indexOf(tentativa[i]) !== -1) {
                filhos_linha[i].setAttribute("placeholder", tentativa[i])
                filhos_linha[i].classList.add("existe")
                //filhos_linha[i].innerHTML = '<span class="yellow">' + tentativa[i] + '</span>'; // Letra correta, mas no lugar errado (amarelo)
            } else {
                filhos_linha[i].setAttribute("placeholder", tentativa[i])
                filhos_linha[i].classList.add("errado")
                //filhos_linha[i].innerHTML = '<span class="black">' + tentativa[i] + '</span>'; // Letra errada (preto)
            }
        }

        $('#answer').html(feedback); // Exibe o feedback na página

        // Limpa os campos de tentativa e habilita o próximo campo
        $('.form-control').val('');
        $('.form-control:first').focus();
        
        tentativasRestantes--;

        // Verifica se o número de tentativas restantes é zero e exibe "Game Over"
        if (tentativasRestantes === 0) {
            alert("Game Over! Você atingiu o limite de tentativas.");
            window.history.back();
            return; // Sai da função após o fim do jogo
        }

        // Desabilita os campos de entrada na linha atual
        $('.class_letra').first().addClass('readonly').find('.form-control').prop('disabled', true);
        
        // Envie os dados do formulário
        $.ajax({
            type: "POST",
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(response) {
                console.log(response);
            },
            error: function(xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });

    // Envio do formulário quando o usuário pressiona Enter
    $('.form-control').on('keypress', function(event) {
        if (event.which === 13) {
            var linhaAtual = $(this).closest('.class_letra');
            event.preventDefault();
            $('#form1').submit();
            // Move para o próximo campo
            console.log(linhaAtual)
            var proximaLinha = linhaAtual.next('.class_letra');
            if (proximaLinha.length) {
                proximaLinha.find('.form-control:first').focus();
            } else {
                alert("Game Over! Você atingiu o limite de tentativas.");
            }
            // Desabilita os campos de entrada na linha atual
            linhaAtual.addClass('readonly').find('.form-control').prop('disabled', true);
        } else if ($(this).val().length === 1) {
            $(this).next().focus();
        }
    });
});
