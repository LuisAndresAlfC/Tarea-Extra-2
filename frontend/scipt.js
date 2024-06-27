document.getElementById('questionnaire-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const mensaje1 = document.getElementById('mensaje1').value;
    const mensaje2 = document.getElementById('mensaje2').value;
    const mensaje3 = document.getElementById('mensaje3').value;

    fetch('http://localhost:5000/user/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, mensaje1, mensaje2,mensaje3})
    })
    .then(response => response.json())
    .then(data => {
        if (data.user_id) {
            alert(`Formulario Enviado Correctamente: ${data.name} (${data.email})`);
            document.getElementById('name').value = '';
            document.getElementById('email').value = '';
            document.getElementById('mensaje1').value = '';
            document.getElementById('mensaje2').value = '';
            document.getElementById('mensaje3').value = '';
        } else {
            alert('Error al enviar el formulario');
        }
    })
    .catch(error => console.error('Error:', error));
});

function getUser() {
    const userId = document.getElementById('userId').value;
    if (userId) {
        fetch(`http://localhost:5000/user/${userId}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert('Usuario no encontrado');
            } else {
                alert(`Detalles del usuario:\nID: ${data.user_id}\nNombre: ${data.name}\nEmail: ${data.email}\nmensaje1: ${data.mensaje1}\nmensaje2: ${data.mensaje2}\nmensaje3: ${data.mensaje3}`);
            }
        })
        .catch(error => console.error('Error:', error));
    } else {
        alert('Por favor, ingrese un ID de usuario válido.');
    }
}