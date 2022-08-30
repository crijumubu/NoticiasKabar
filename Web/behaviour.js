function createNew(news){
    return `
    <div class="news">
        <img src="${imagen}" alt="">
        <h3>${categoria}</h3>
        <div class="info">

            <h2>${titulo}</h2>
            <h4>${publicadora}</h4>
        </div>
    </div>`;
}

const new1 = {
    imagen:"",
    categoria:"",
    titulo:"",
    publicadora:"",
    descripcion:"",
    link:""
} 