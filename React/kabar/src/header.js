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
            {/* <Filter arrNoticias={this.props.arrNoticias}></Filter> */}
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


function Filter({arrNoticias}){
  console.log(arrNoticias)
  const showModal = ()=>{
    
    const modal = document.getElementById("modal");
    const modalWrap = document.getElementById("modal-wrap");

    // modal.style.animationPlayState = "running";
    // modalWrap.style.animationPlayState = "running";



    // modal.classList.remove("delay");
    document.body.style.overflow = "hidden"
    modal.classList.add("modal-active");
    // modalWrap.classList.add("modal-wrap-active");
    // modal.classList.add("delay");
    // modalWrap.classList.remove("modal-wrap-inactive");

  }

  const closeModal = (e)=>{
    
    if(e.target.id === "modal" || e.target.id ==="close"){
      console.log(e.target.id )
      const modal = document.getElementById("modal");
      const modalWrap = document.getElementById("modal-wrap");
      
      // modal.style.animationDirection = "reverse";
      // modalWrap.style.animationDirection = "reverse";
      // modal.style.animationFillMode = "none"
      // modalWrap.style.animationFillMode = "none"
      
      // setTimeout(()=>{
        //   modal.style.animationPlayState = "running";
        //   modalWrap.style.animationPlayState = "running";
        
        // }, 2000)

        
        
        // modalWrap.classList.remove("delay")
        document.body.style.overflow = "visible"
        modal.classList.remove("modal-active")
        // modalWrap.classList.remove("modal-wrap-active")
        // modalWrap.classList.add("delay")
        // document.getElementById("modal-wrap").classList.add("modal-wrap-inactive")
        
      }


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
        <span class="close" onClick={closeModal} id="close">&times;</span>
          <form>

            <h2>Filtro por Categorias:</h2>
            {/* <h3>Categorias</h3> */}
            <div>
              <input type="checkbox" name="categories[]" id="deportes"></input><label for="deportes"> Deportes</label><br></br>
            </div>

            <div>
              <input type="checkbox" name="categories[]" id="judicial"></input><label for="judicial"> Judicial</label ><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="politica"></input><label for="politica"> Política</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="uInvestigativa"></input><label for="uInvestigativa"> Unidad investigativa</label><br></br>
            </div>
            
            <div>

            <input type="checkbox" name="categories[]" id="economia"></input><label for="economia"> Economía</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="technologia"></input><label for="technologia"> Technología</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="ciencia"></input><label for="ciencia"> Ciencia</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="salud"></input><label for="salud"> Salud</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="educacion"></input><label for="educacion"> Educacíon</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="entreteniento"></input><label for="entreteniento"> Entretenimeinto</label><br></br>
            </div>
            
            <div>

            <input type="checkbox" name="categories[]" id="colombia"></input><label for="colombia"> Colombia</label><br></br>
            </div>

            <div>

            <input type="checkbox" name="categories[]" id="otros"></input><label for="otros"> Otros</label><br></br>
            </div>

            
            {/* <h3>Portales de noticias</h3> */}
            <button type="submit" className="filter-submit">Filtrar</button>
          </form>
        </div>
      </div>
    </>
  )
}


export default Header;
