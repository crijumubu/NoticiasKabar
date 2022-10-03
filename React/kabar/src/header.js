import React from "react";
// import ReactDOM from "react-dom/client";
import "./header.css";

function Header () {
    return (
      <header>
        <div className="header-container">
          <h1>Kabar</h1>
        </div>
        
        {/* <nav>
          <Link icon="bi bi-person-square"  linkText="Kabar"goTo=""></Link> 
          <Link icon="bi bi-search"   linkText="Kabar"goTo="#search"></Link> 
          <Link icon="bi bi-funnel" linkText="Kabar" ></Link>
        </nav> */}
        <div className="search">
          <form>
            <SearchBar holdTxt="¿Que desea buscar?" />
            <SubmitBtn />
          </form>
        </div>
      </header>
    );  
}

function SearchBar({holdTxt}) {
  return <input type="search" className="search-inp" placeholder={holdTxt}></input>;
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
// function Link({icon,linkText, goTo ="#"}){
//   return (
//     <a href={goTo} className="link-side">
//         <i className={`${icon} icon`}>
//             <p>{linkText}</p>
//         </i>
//     </a>
//   );
// }

export default Header;
