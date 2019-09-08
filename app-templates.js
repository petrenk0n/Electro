const express = require('express')
const app = express()
var exphbs = require('express-handlebars')

app.use('/static', express.static('public'));

app.engine('handlebars', exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

app.get('/dashboard', function (req, res) {
	res.render('home');
});

app.get('/', function (req, res) {
	res.render('greet');
});

app.listen(3000, () => console.log('App is running'))