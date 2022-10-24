import React from "react";
// import ReactDOM from "react-dom/client";
import "./header.css";

class Header extends React.Component{
  constructor(props){
    super(props);
    this.state = {value:''}

    this.resetPage = this.resetPage.bind(this);
  }

  resetPage(){
    this.props.changeNews("reset");
  }

  render(){
    return (
      <header>
        <div className="header-container" onClick={this.resetPage}>
          <h1>Kabar</h1>
        </div>
        
        <div className="search">
            <Filter changeNews={this.props.changeNews}></Filter>
          <form onSubmit={this.props.submitEvent}>
            <SearchBar holdTxt="¿Qué desea buscar?" change={this.props.submitEvent} />
            <SubmitBtn />
          </form>
        </div>

      </header>
    );  
  }
}

function SearchBar({holdTxt, valueS,change}) {
  return <input type="search" className="search-inp" placeholder={holdTxt} value={valueS} onChange={change} id="searchInput"></input>;
}

function SubmitBtn(){
    return(
        <button type="submit" className="search-btn button">
            <i className="bi bi-search icon-search"></i>
        </button>
    )
}


function Filter({changeNews}){
  // console.log(arrNoticias)
  const showModal = ()=>{
    
    const modal = document.getElementById("modal");

    document.body.style.overflow = "hidden"
    modal.classList.add("modal-active");
  }

  const closeModal = (e)=>{
    
    if(e.target.id === "modal" || e.target.id ==="close"){
      // console.log(e.target.id )
      const modal = document.getElementById("modal");

        document.body.style.overflow = "visible"
        modal.classList.remove("modal-active")
      }
  }

  const filterCategories = (e)=>{
    // e.preventDefault();

    const categorias = [];
    document.getElementsByName("categories[]").forEach((elem)=>{
      if(elem.checked){
        categorias.push(elem.id)
      }
    })

    if(categorias.length ===0){
      changeNews("resetC");
      return
    }

    const categoriasValue = [];
    categorias.forEach((elem)=>{
      switch (elem) {
        case "deportes":
          categoriasValue.push("Deportes")

          break;
        
        case "judicial":
          categoriasValue.push("Judicial")

          break;

        case "politica":
          categoriasValue.push("Política")

          break;

        case "uInvestigativa":
          categoriasValue.push("Unidad investigativa")

          break;

        case "economia":
          categoriasValue.push("Economía")

          break;

        case "tecnologia":
          categoriasValue.push("Tecnología")

          break;
          
        case "ciencia":
          categoriasValue.push("Ciencia")

          break;

        case "salud":
          categoriasValue.push("Salud")

          break;

        case "educacion":
          categoriasValue.push("Educacíon")

          break;

        case "entretenimiento":
          categoriasValue.push("Entretenimiento")

          break;

        case "colombia":
          categoriasValue.push("Colombia")

          break;
      
        default:
          categoriasValue.push("Otros")
          break;


      }
    })

    // console.log(categoriasValue)
    changeNews(categoriasValue, "categories");
  }

  const filterSoures = ()=>{
    const categorias = [];
    document.getElementsByName("sources[]").forEach((elem)=>{
      if(elem.checked){
        categorias.push(elem.id)
      }
    })

    if(categorias.length ===0){
      changeNews("resetS");
      return
    }

    const categoriasValue = [];
    categorias.forEach((elem)=>{
      switch (elem) {
        case "tiempo":
          categoriasValue.push("El tiempo")
  
          break;

        case "espectador":
          categoriasValue.push("El espectador")

          break;

        case "portafolio":
          categoriasValue.push("Portafolio")
  
          break;
        
        case "nuevoSiglo":
          categoriasValue.push("El nuevo siglo")
    
          break;
        
        case "publimetro":
          categoriasValue.push("Publimetro")

          break;

        default:
          categoriasValue.push("ADN")
  
          break;
      }
    })

    // console.log(categoriasValue)
    changeNews(categoriasValue, "sources");
  }

  const clickCategories = ()=>{
    document.getElementById("form-categories").classList.remove("inactive");
    document.getElementById("btn-categories").classList.remove("no-border");
    document.getElementById("form-sources").classList.add("inactive");
    document.getElementById("btn-sources").classList.add("no-border");
  }

  const clickSources = ()=>{
    document.getElementById("form-categories").classList.add("inactive");
    document.getElementById("btn-categories").classList.add("no-border");
    document.getElementById("form-sources").classList.remove("inactive");
    document.getElementById("btn-sources").classList.remove("no-border");
  }

  return (
    <>
      <button type="checkbox" className="filter-btn button" onClick={showModal} >
        {/* <i className="bi bi-funnel"></i> */}
        {/* <i className="bi bi-filter-circle"></i> */}
        <i className="bi bi-sort-down"></i>
      </button>
      <div className="modal open-bg" id="modal" onClick={closeModal}>
        <div className="modal-wrap open-wrap" id="modal-wrap">
        <span className="close" onClick={closeModal} id="close">&times;</span>

          <div className="filters">
            <button className="filter-type"onClick={clickCategories} id="btn-categories">Categorias</button>
            <button className="filter-type no-border"onClick={clickSources} id="btn-sources">Fuente</button>

          </div>
          <form  id="form-categories" onChange={filterCategories} className="" >

          {/* <div >  */}

            <div>
              <input type="checkbox" name="categories[]" id="deportes"></input><label htmlFor="deportes"> Deportes</label>
            </div>

            <div>
              <input type="checkbox" name="categories[]" id="judicial"></input><label htmlFor="judicial"> Judicial</label >
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="politica"></input><label htmlFor="politica"> Política</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="uInvestigativa"></input><label htmlFor="uInvestigativa"> Unidad investigativa</label>
            </div>
            
            <div>

            <input type="checkbox" name="categories[]" id="economia"></input><label htmlFor="economia"> Economía</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="tecnologia"></input><label htmlFor="tecnologia"> Tecnología</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="ciencia"></input><label htmlFor="ciencia"> Ciencia</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="salud"></input><label htmlFor="salud"> Salud</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="educacion"></input><label htmlFor="educacion"> Educacíon</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="entretenimiento"></input><label htmlFor="entretenimiento"> Entretenimiento</label>
            </div>
            
            <div>

            <input type="checkbox" name="categories[]" id="colombia"></input><label htmlFor="colombia"> Colombia</label>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="otros"></input><label htmlFor="otros"> Otros</label>
            </div>
          {/* </div> */}
          </form>


          {/* ------------- Fuentes ------------- */}
          <form   id="form-sources" className="inactive" onChange={filterSoures}>
          {/* <div > */}

            <div>
              <input type="checkbox" name="sources[]" id="tiempo"></input><label htmlFor="tiempo"> El tiempo</label>
            </div>

            <div>
              <input type="checkbox" name="sources[]" id="espectador"></input><label htmlFor="espectador"> El espectador</label >
            </div>

            <div>

            <input type="checkbox" name="sources[]" id="portafolio"></input><label htmlFor="portafolio"> Portafolio</label>
            </div>

            <div>

            <input type="checkbox" name="sources[]" id="nuevoSiglo"></input><label htmlFor="nuevoSiglo"> El nuevo siglo</label>
            </div>
            
            <div>

            <input type="checkbox" name="sources[]" id="publimetro"></input><label htmlFor="publimetro"> Publimetro</label>
            </div>

            <div>

            <input type="checkbox" name="sources[]" id="adn"></input><label htmlFor="adn"> ADN</label>
            </div>
          {/* </div> */}

            {/* <button type="submit" className="filter-submit" >Filtrar</button> */}
          </form>

          

        </div>
      </div>
    </>
  )
}


export default Header;
