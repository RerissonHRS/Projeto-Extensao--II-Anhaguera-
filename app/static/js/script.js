
async function consultar() {
    const numero = document.getElementById("numero").value;
    const res = document.getElementById("resultado");

    const r = await fetch("/consultar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ numero })
    });

    const data = await r.json();

    if (data.erro) {
        res.innerHTML = data.erro;
        return;
    }

    res.innerHTML = `
        <h3>${data.nome}</h3>
        <p><b>Aspecto Positivo:</b> ${data.positivo}</p>
        <p><b>Aspecto Negativo:</b> ${data.negativo}</p>
        <p><b>Ebó de Positivação:</b> ${data.ebo_positivo}</p>
        <p><b>Principal Conselho:</b> ${data.Alerta}</p>
        <p><b>Orixás:</b> ${data.orixas.join(", ")}</p>
    `;
}
