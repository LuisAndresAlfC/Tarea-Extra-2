const express = require('express');
const app = express();
const path = require('path');

// Servir archivos estáticos
app.use(express.static(path.join(__dirname)));

// Ruta para la página principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Iniciar el servidor
const port = 3000;
app.listen(port, () => {
    console.log(`Servidor escuchando en el puerto ${port}`);
});
