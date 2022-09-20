const express = require('express');
const router = express.Router();
const noticia = require('../model/ModelNoticias')


///consultar todos las noticias
router.get('/', async(req, res)=>{
    const noticias =await noticia.find();
    console.log(noticias)
    res.json(noticias)
})
/////insrtar una noticia

router.post('/', async(req, res)=>{
    
    
    const {title, decripcion, categoria, imagen, urlOrigen, nombreOrigen }= req.body
    const noti = new noticia({title, decripcion, categoria, imagen, urlOrigen, nombreOrigen});
    await noti.save();
    console.log(req.body)
    res.json('noticia insertada')
});
/// editar una noticia
router.put('/:id', async(req, res)=>{
    
    
    const {title, decripcion, categoria, imagen, urlOrigen, nombreOrigen }= req.body
    const noti = new noticia({title, decripcion, categoria, imagen, urlOrigen, nombreOrigen});
    await noti.findByIdAndUPdate(req.params.id, newNoti);
    console.log(req.body)
    res.json('noticia actualizada')
});
///eliminar na noticia
router.delete('/:id', async(req, res)=>{
    await noti.findByIdAndURemove(req.params.id);
    res.json('noticia eliminada')
});

module.exports = router;