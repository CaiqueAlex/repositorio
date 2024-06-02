document.addEventListener('DOMContentLoaded', function() {
    const popupContainer = document.getElementById('popup-container');
    const closePopup = document.getElementById('close-popup');

    // Exibir o pop-up quando necessário
    function showPopup() {
        popupContainer.style.display = 'block';
    }

    // Fechar o pop-up quando clicar no botão de fechar
    closePopup.addEventListener('click', function() {
        popupContainer.style.display = 'none';
    });

    // Fechar o pop-up quando clicar fora dele
    window.addEventListener('click', function(event) {
        if (event.target == popupContainer) {
            popupContainer.style.display = 'none';
        }
    });

    // Exemplo de quando exibir o pop-up (pode ser adaptado para o seu caso específico)
    // Aqui estou usando um botão como exemplo, você pode chamar a função `showPopup()` quando o usuário ganhar o jogo
    const botaoExemplo = document.getElementById('botao-exemplo');
    botaoExemplo.addEventListener('click', function() {
        showPopup();
    });
});
