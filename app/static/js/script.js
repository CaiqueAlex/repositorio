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
                //alert("A palavra digitada não é válida.");
                return;
            }

            // Processa a tentativa se a palavra for válida
            var palavra_aleatoria = $('#board').data('palavra');
            var feedback = '';

            if (tentativa === palavra_aleatoria) {
                $('#answer').html('<span class="green">' + tentativa + '</span>');
                exibirConfetes();
                exibirResultadoPopup(true);
                $('#success-popup .close').on('click', function() {
                    window.location.href = "../termo/";
                });
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
                exibirResultadoPopup(false);
                $('#error-popup .close').on('click', function() {
                    window.location.href = "../termo/";
                });
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
                    //alert("A palavra digitada não é válida.");
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

        // Fechar o pop-up ao clicar fora dele
        $(document).on('click', function(event) {
            if (!$(event.target).closest('#success-popup').length) {
                $('#success-popup').hide();
            }
        });
    });
});

function exibirResultadoPopup(venceu) {
    if (venceu) {
        $('#success-popup').show();
    } else {
        $('#error-popup').show();
    }
}

function exibirConfetes() {
    var confettiColors = ['#f00', '#0f0', '#00f', '#ff0', '#0ff', '#f0f']; // Cores dos confetes
    var confettiCount = 200; // Quantidade de confetes
    var confettiElements = '';

    // Criar elementos de confete
    for (var i = 0; i < confettiCount; i++) {
        var color = confettiColors[Math.floor(Math.random() * confettiColors.length)];
        confettiElements += '<div class="confetti" style="background-color: ' + color + ';"></div>';
    }

    // Adicionar confetes ao corpo da página
    $('#success-popup').append(confettiElements);

    // Configurar a animação dos confetes
    $('.confetti').each(function() {
        var angle = Math.random() * 360; // Ângulo aleatório entre 0 e 360 graus
        var distance = Math.random() * 400; // Distância aleatória do centro
        var duration = Math.random() * 4 + 2; // Duração da animação
        var delay = Math.random() * 2; // Atraso para iniciar a animação
        $(this).css({
            'left': 'calc(50% + ' + Math.cos(angle * Math.PI / 180) * distance + 'px)',
            'top': 'calc(50% + ' + Math.sin(angle * Math.PI / 180) * distance + 'px)',
            'animation-duration': duration + 's',
            'animation-delay': delay + 's'
        });
    });

    // Remover confetes após um período de tempo
    setTimeout(function() {
        $('.confetti').fadeOut(1000, function() {
            $(this).remove();
        });
    }, 3000);
}
