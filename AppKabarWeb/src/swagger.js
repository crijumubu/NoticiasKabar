const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUi =require("swagger-ui-express");

// metadatos informacion de la api

const options={
    definition:{
        openapi:"3.0.0",
        info:{
            title:"KabarWebBDApi",
            version:"1.0.0"
        },
    },
    apis:["src/routes/rutas.js", "src/model/ModelNoticias.js"],
};

//// documentos en formato json
const swaggerSpec = swaggerJSDoc(options);
const swaggerDocs =(app,port)=>{
    app.use('/api/v1/docs', swaggerUi.serve, swaggerUi.setup(swaggerSpec));
    app.get('/api/v1/docs.json',(req, res)=>{
        res.setHeader("Content-Type","application/json");
        res.send(swaggerSpec);
    });
    console.log(
        'version 1 docs are avaliable at http://localhost:'+port+'/api/v1/docs'
    );
}
module.exports={swaggerDocs};