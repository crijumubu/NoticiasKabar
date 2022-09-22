const express = require('express');
const app = express();
const morgan = require('morgan');
const path = require('path');
require("dotenv").config();
const mongoose = require('mongoose');

// /////////////////////////////////////////////configuraciones////////////////////////////////////////////////////////////////////////

app.set('port',process.env.PORT || 3000); //tome el perto asignado por el sistema operativo o use el 3000

mongoose.connect(process.env.MONGODB_URI).then(()=>console.log("Conectado KABARDB")).catch((error)=>console.error(error));

////////////////////////midlewares Funciones que se ejecutan antes de llegar a las rutas/////////////////////////////////////////////////

app.use(morgan('dev'));
app.use(express.json());

////////////////////////////////////////////////rutas/////////////////////////////////////////////////////////////////////////////////

app.use('/api',require('./routes/rutas'))

//////////////////////////////////////////Archivos Estaticos/////////////////////////////////////////////////////////////////////////

app.use(express.static(path.join(__dirname+'/public')));
console.log(path.join(__dirname + '/public'));
/////////////////////////////////////////////iniciacion server///////////////////////////////////////////////////////////////////////
app.listen(app.get('port'), () => { 
    console.log('server en puerto: '+app.get('port')); 
});