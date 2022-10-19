import React from "react";
// import ReactDOM from "react-dom/client";
import "./header.css";

class Header extends React.Component{
  constructor(props){
    super(props);
    this.state = {value:''}

  }

  render(){
    return (
      <header>
        <div className="header-container">
          <h1>Kabar</h1>
        </div>
        
        <div className="search">
            <Filter changeNews={this.props.changeNews}></Filter>
          <form onSubmit={this.props.submitEvent}>
            <SearchBar holdTxt="¿Qué desea buscar?"  />
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
      console.log(e.target.id )
      const modal = document.getElementById("modal");

        document.body.style.overflow = "visible"
        modal.classList.remove("modal-active")
      }
  }

  const handleSubmit = (e)=>{
    e.preventDefault();
    // console.log(arrNoticias);
    // arrNoticias = [];
    changeNews([]);
    // console.log(arrNoticias);
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
          <form onSubmit={handleSubmit}>

            <h2>Filtro por Categorias:</h2>
            {/* <h3>Categorias</h3> */}
            <div>
              <input type="checkbox" name="categories[]" id="deportes"></input><label htmlFor="deportes"> Deportes</label><br></br>
            </div>

            <div>
              <input type="checkbox" name="categories[]" id="judicial"></input><label htmlFor="judicial"> Judicial</label ><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="politica"></input><label htmlFor="politica"> Política</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="uInvestigativa"></input><label htmlFor="uInvestigativa"> Unidad investigativa</label><br></br>
            </div>
            
            <div>

            <input type="checkbox" name="categories[]" id="economia"></input><label htmlFor="economia"> Economía</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="technologia"></input><label htmlFor="technologia"> Technología</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="ciencia"></input><label htmlFor="ciencia"> Ciencia</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="salud"></input><label htmlFor="salud"> Salud</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="educacion"></input><label htmlFor="educacion"> Educacíon</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="entreteniento"></input><label htmlFor="entreteniento"> Entretenimeinto</label><br></br>
            </div>
            
            <div>

            <input type="checkbox" name="categories[]" id="colombia"></input><label htmlFor="colombia"> Colombia</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="otros"></input><label htmlFor="otros"> Otros</label><br></br>
            </div>

            
            {/* <h3>Portales de noticias</h3> */}
            <button type="submit" className="filter-submit" >Filtrar</button>
          </form>
        </div>
      </div>
    </>
  )
}


export default Header;
