import React from "react";
// import ReactDOM from "react-dom/client";
import Scroll from "./scroll";
import "./container.css";
import Header from "./header";

class Content extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      news: [],
      newsRender: [],
      newQuantity: 20,
      
    }

    this.fetchApi = this.fetchApi.bind(this);
    this.handleClick = this.handleClick.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }


  async fetchApi(){
    const response = await fetch('https://raw.githubusercontent.com/crijumubu/NoticiasKabar/artificial-intelligence/news/news.json');
    const data = await response.json();
    this.setState({news: data})

    
    this.setState({newsRender:data.slice(0,this.state.newQuantity)})

    return data;
  }    

  componentDidMount(){
    this.fetchApi(this.renderGrid);

  }
  
  handleClick(){


    this.setState({newsRender:this.state.news.slice(0,this.state.newsRender.length +20)})
    // console.log(this.state.newsRender.length)
    if((this.state.newsRender.length+20) >= this.state.news.length){
      document.getElementById("btnMore").style.display = "none";
    }

  }

  handleSubmit(e){
    
    const input = document.getElementById("searchInput");
    this.search(input.value);


    e.preventDefault()

    // console.log(input.value)
  }

  search(text){

    const textLower = text.toLowerCase();
    let titleLower;


    const arrSearch = this.state.news.filter((elem)=>{
      titleLower = elem.Title.toLowerCase();

      return titleLower.includes(textLower)
      // 
      // if(){
        // return elem;
      // }
    })

    console.log(arrSearch);
  }

  render(){

    // this.state.newsRender = ;
    // console.log(this.state.newsRender)
    let temp = [];

    // console.log(data);
    return(
    <>
      <Header submitEvent={this.handleSubmit}></Header>
      <div className="content">
      {
        this.state.newsRender.map((e,ind)=>{
	        temp = this.state.newsRender.slice(ind*5,(ind+1)*5)
          try {
            return Grid(temp);
          } catch (error) {
            // console.log(error)
            return <></>;
          }
      })
      }
        <button onClick={this.handleClick} id="btnMore" className="btnMore">Ver más noticias</button>
        <Scroll></Scroll>
      </div>
    </>
    )
  }
}

// TODO Trabajar en RenderContent, para pasarle la funcion OnScroll

// function RenderContent(){
//   const listInnerRef = useRef();

//   const onScroll = () => {
//     if (listInnerRef.current) {
//       const { scrollTop, scrollHeight, clientHeight } = listInnerRef.current;
//       if (scrollTop + clientHeight === scrollHeight) {
//         console.log("reached bottom");
//       }
//     }
//   };

//   return(
//     <>
//       <Content onScroll={onScroll} ></Content>
//     </>)
// }




function New({Url, Image, Title, Descripcion , Category, Source, Date, Id, Bigger = ""}){
  return(
  <a href={Url} className={`news ${Bigger}`} key={Id} target="_blank" rel="noreferrer">
    <img src={Image} alt="No img"></img>
    <div id="news-info" className="news-info">

      <h2>{Title}</h2>
      <h4><b>Fuente:</b> {Source}</h4>
      <h3><span className="category">{Category} <i className="bi  bi-tag-fill catIcon"></i></span></h3>
      {/* <p>{Descripcion}</p> */}
      <h4 className="date"><b> Fecha de extraccion:</b> {Date}</h4>
      <div className="info"></div>
    </div>
  </a>
  );
}


function Grid(arr){
  return(
	<>
	  <div className="grid-2">

      
      <New Url={arr[0].Url} Image={arr[0].Image} Title={arr[0].Title} Descripcion={arr[0].Descripcion} Category={arr[0].Category} Source={arr[0].Source} Date={arr[0].Date} Id="0"></New>

      <New Url={arr[1].Url} Image={arr[1].Image} Title={arr[1].Title} Descripcion={arr[1].Descripcion} Category={arr[1].Category} Source={arr[1].Source} Date={arr[1].Date} Id="1"></New>
  </div>

  <div className="grid-3">
      <New Url={arr[2].Url} Image={arr[2].Image} Title={arr[2].Title} Descripcion={arr[2].Descripcion} Category={arr[2].Category} Source={arr[2].Source} Date={arr[2].Date} Id="2"></New>

      <New Url={arr[3].Url} Image={arr[3].Image} Title={arr[3].Title} Descripcion={arr[3].Descripcion} Category={arr[3].Category} Source={arr[3].Source} Date={arr[3].Date} Id="3"></New>

      <New Url={arr[4].Url} Image={arr[4].Image} Title={arr[4].Title} Descripcion={arr[4].Descripcion} Category={arr[4].Category} Source={arr[4].Source} Date={arr[4].Date} Id="4" Bigger="big"></New>

  </div>

	</>
  )
}

// function BtnTop(){
  
// }

export default Content;