document.getElementById('loginForm')?.addEventListener('submit', function(e) {
    e.preventDefault();
    
    const email = e.target.querySelectorAll('input')[0].value;
    const senha = e.target.querySelectorAll('input')[1].value;

    // Defina aqui o e-mail e a senha que você deseja usar:
    if (email === "admin@jastech.com" && senha === "123456") {
        alert("Login realizado com sucesso!");
        window.location.href = "/admin/dashboard.html";
    } else {
        alert("E-mail ou senha incorretos!");
    }
});
