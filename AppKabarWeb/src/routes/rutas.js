const express = require('express');
const router = express.Router();
const noticia = require('../model/ModelNoticias')


///consultar todos las noticias

/**
 * @openapi
 * /api:
 *   get:
 *     tags:
 *       - Noticias KABAR
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     $ref: "../model/ModelNoticicias.js"
 */
router.get('/', async(req, res)=>{
    const noticias =await noticia.find();
    console.log(noticias)
    res.json(noticias)
})
/////insrtar una noticia

/**
 * @openapi
 * /api:
 *   post:
 *     tags:
 *       - Noticias KABAR
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     $ref: "../model/ModelNoticicias.js"
 */

router.post('/', async(req, res)=>{
    
    
    const {title, decripcion, categoria, imagen, urlOrigen, nombreOrigen }= req.body
    const noti = new noticia({title, decripcion, categoria, imagen, urlOrigen, nombreOrigen});
    await noti.save();
    console.log(req.body)
    res.json('noticia insertada')
});
/// editar una noticia
/**
 * @openapi
 * /api:
 *   put:
 *     tags:
 *       - Noticias KABAR
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     $ref: "../model/ModelNoticicias.js"
 */
router.put('/:id', async(req, res)=>{
    
    
    const {title, decripcion, categoria, imagen, urlOrigen, nombreOrigen }= req.body
    const noti = new noticia({title, decripcion, categoria, imagen, urlOrigen, nombreOrigen});
    await noti.findByIdAndUPdate(req.params.id, newNoti);
    console.log(req.body)
    res.json('noticia actualizada')
});
///eliminar na noticia
/**
 * @openapi
 * /api:
 *   delete:
 *     tags:
 *       - Noticias KABAR
 *     responses:
 *       200:
 *         description: OK
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 status:
 *                   type: string
 *                   example: OK
 *                 data:
 *                   type: array 
 *                   items: 
 *                     $ref: "../model/ModelNoticicias.js"
 */
router.delete('/:id', async(req, res)=>{
    await noti.findByIdAndURemove(req.params.id);
    res.json('noticia eliminada')
});

module.exports = router;