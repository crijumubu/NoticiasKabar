const mongoose  = require("mongoose");
const { Schema }= mongoose;

const noticiaSchema = new Schema ({

    title :{type :String, required:true},
    decripcion:{type :String, required:true},
    categoria:{type :String, required:true},
    imagen:{type :String, required:true},
    urlOrigen :{type :String, required:true},
    nombreOrigen:{type :String, required:true},
})

module.exports = mongoose.model("modelNoticia",noticiaSchema )