$(document).ready(function() {
    let primeira_linha = document.getElementsByClassName("class_letra")[0];
    let linha_index = 0;
    let linhaAtual = primeira_linha;
    var tentativasRestantes = 6;
    var palavrasValidas = [];

    // Função para carregar palavras válidas de um arquivo de texto
    function carregarPalavrasValidas(arquivo, callback) {
        $.get(arquivo, function(data) {
            palavrasValidas = data.trim().toLowerCase().split('\n');
            callback();
        });
    }

    // Carrega as palavras válidas do arquivo texto
    carregarPalavrasValidas('/static/js/arquivo_palavras.txt', function() {
        // Impede a digitação de caracteres não alfabéticos nos campos de entrada
        $('.form-control').on('keypress', function(event) {
            var charCode = event.which;
            if (!((charCode >= 65 && charCode <= 90) || (charCode >= 97 && charCode <= 122))) {
                event.preventDefault();
            }
        });

        // Move o foco para o próximo campo ao preencher o atual
        $('.form-control').on('keyup', function(event) {
            if ($(this).val() && event.which !== 8) {
                $(this).next('.form-control').focus();
            } else if (event.which === 8 && $(this).val() === "") { // Detecta Backspace no campo vazio
                $(this).prev('.form-control').focus();
            }
        });

        $('#form1').on('submit', function(event) {
            event.preventDefault();

            var tentativa = $('.form-control').map(function() { return $(this).val(); }).get().join('').toLowerCase();
            if (tentativasRestantes > 0 && palavrasValidas.indexOf(tentativa) === -1) {
                alert("A palavra digitada não é válida.");
                return;
            }

            // Processa a tentativa se a palavra for válida
            var palavra_aleatoria = $('#board').data('palavra');
            var feedback = '';

            if (tentativa === palavra_aleatoria) {
                $('#answer').html('<span class="green">' + tentativa + '</span>');
                alert("Você ganhou!");
                window.location.href = "../termo/"; // Redireciona para a URL desejada
                return;
            }

            let filhos_linha = linhaAtual.children;
            for (var i = 0; i < tentativa.length; i++) {
                if (tentativa[i] === palavra_aleatoria.charAt(i)) {
                    filhos_linha[i].setAttribute("placeholder", tentativa[i]);
                    filhos_linha[i].classList.add("correta");
                } else if (palavra_aleatoria.indexOf(tentativa[i]) !== -1) {
                    filhos_linha[i].setAttribute("placeholder", tentativa[i]);
                    filhos_linha[i].classList.add("existe");
                } else {
                    filhos_linha[i].setAttribute("placeholder", tentativa[i]);
                    filhos_linha[i].classList.add("errado");
                }
            }

            $('#answer').html(feedback);

            $('.form-control').val('');
            $('.form-control:first').focus();

            tentativasRestantes--;

            // Torna os campos da linha atual readonly após a tentativa ser processada corretamente
            $(linhaAtual).addClass('readonly').find('.form-control').prop('disabled', true);
            linha_index++;
            linhaAtual = document.getElementsByClassName("class_letra")[linha_index];

            if (tentativasRestantes === 0) {
                alert("Game Over! Você atingiu o limite de tentativas.");
                window.location.href = "../termo/"; // Redireciona para a URL desejada
                return;
            }

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

        $('.form-control').on('keypress', function(event) {
            if (event.which === 13) {
                var tentativa = $('.form-control').map(function() { return $(this).val(); }).get().join('').toLowerCase();
                if (palavrasValidas.indexOf(tentativa) === -1) {
                    alert("A palavra digitada não é válida.");
                    return;
                }
                var linhaAtual = $(this).closest('.class_letra');
                event.preventDefault();
                $('#form1').submit();
                var proximaLinha = linhaAtual.next('.class_letra');
                if (proximaLinha.length) {
                    proximaLinha.find('.form-control:first').focus();
                }
            }
        });

        // Adiciona evento para limpar a palavra errada e voltar o foco para o início da linha atual
        $('.form-control').on('keydown', function(event) {
            if (event.which === 8 && $(this).val() === '') { // Detecta Backspace no campo vazio
                event.preventDefault();
                $(this).prev('.form-control').focus();
            }
        });
    });
});