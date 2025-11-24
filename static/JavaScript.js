const form = document.getElementById("cadastro-funcionario");
const tabela = document.getElementById("tabela-funcionarios");

form.addEventListener("submit", function (e) {
    e.preventDefault();

    const nome = document.getElementById("nome").value;
    const cargo = document.getElementById("cargo").value;
    const cultura = document.getElementById("cultura").value;
    const salario = document.getElementById("salario").value;
    const atribuicoes = document.getElementById("atribuicoes").value;

    
    const novaLinha = document.createElement("tr");

    novaLinha.innerHTML = `
        <td>${nome}</td>
        <td>${cargo}</td>
        <td>${cultura}</td>
        <td>44h/semana</td>
        <td>R$ ${Number(salario).toFixed(2)}</td>
        <td>${atribuicoes}</td>
        <td>${new Date().toLocaleDateString()}</td>
        <td>
            <button class="editar">Editar</button>
            <button class="excluir">Excluir</button>
        </td>
    `;

    tabela.appendChild(novaLinha);

    // Limpar formulário
    form.reset();
});
