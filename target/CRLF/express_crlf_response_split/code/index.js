const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/setcookie', (req, res) => {
    const userInput = req.query.name;
    res.setHeader('Set-Cookie', `user=${userInput}`);
    res.send('Cookie has been set');
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
