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
        <button type="submit" className="search-btn">
            <i className="bi bi-search icon-search"></i>
        </button>
    )
}

// function Filter(){
//   return(
//   <>
//     <button>
//       <i class="bi bi-funnel"></i>
//     </button>
//   </>)
// }


export default Header;
