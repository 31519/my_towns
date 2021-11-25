import React, { useState, useEffect } from "react";
import axios from "axios";
import { useSelector, useDispatch } from "react-redux";
import { createTechs } from "../actions/techActions";

import "../css_styles/TechCreate.css";

const TechCreateNewsApi = () => {
  // const [author, setAuthor] = useState("");
  // // const [title, setTitle] = useState("");
  // const [description, setDescription] = useState("");
  // const [url, setUrl] = useState("");
  // const [urlToImage, setUrlToImage] = useState("");
  // const [publishedAt, setPublishedAt] = useState("");
  // const [content, setContent] = useState("");

  const [techsx, setTechsx] = useState([]);
  const newsApiKey = "d049a308e4634c8b8a28ce3b4b3059be";
  const dispatch = useDispatch();

  // const submitHandler = (tech) => {
  //   dispatch(
  //     createTechs({
  //       "author":tech.author,
  //       "title": tech.title,
  //       "description":tech.description,
  //       "url":tech.url,
  //       "urlToImage":tech.urlToImage,
  //       "publishedAt":tech.publishedAt,
  //       "content":tech.content
  //     })
  //   )
  //   console.log("clicked", author);
  // };

  //   FETCH THE DATA
  const techNewsApi = () => async () => {
    console.log("Fetching api");

    const { data } = await axios.get(
      `https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=${newsApiKey}`
    );

    const techs = data.articles;

    console.log("datas", techs.length);
    // setTechs(datas);
    // console.log("techs1", techs.values());
    console.log("techs2", techs);

    for (let i = 0; i< techs.length; i++) {
      
    console.log("interval start", techs.length)
    const author = techs[i].author
    const title = techs[i].title
    const description = techs[i].description
    const url = techs[i].url
    const urlToImage = techs[i].urlToImage
    const publishedAt = techs[i].publishedAt
    const content = techs[i].content
    console.log("interval ended author", techs[i].author )

    dispatch(
          createTechs(
            author,
            title,
            description,
            url,
            urlToImage,
            publishedAt,
            content
          )
        )

      console.log("for loop ended dispatch", techs[i].author)
    }
    console.log("finished")




    techsx && techsx.map((tech) => {
      return (
        console.log("interval start", techs.length),
        console.log("hi", techs.author),
        // setAuthor(techs.author),
        // // setTitle(techs.title),
        // setDescription(techs.description),
        // setUrl(techs.url),
        // setUrlToImage(techs.urlToImage),
        // setPublishedAt(techs.publishedAt),
        // setContent(techs.content),
        console.log("interval ended author", techs.author ),
        // submitHandler(),

        console.log("inside map last line"),
        // dispatch(
        //   createTechs(
        //     author,
        //     title,
        //     description,
        //     url,
        //     urlToImage,
        //     publishedAt,
        //     content
        //   )
        // ),


        dispatch(createTechs({
           
            "author":techs.author,
            "title": techs.title,
            "description":techs.description,
            "url":techs.url,
            "urlToImage":techs.urlToImage,
            "publishedAt":techs.publishedAt,
            "content":techs.content
          })
        ),
        console.log("dispatch finished")
      )
    
      
    })
  };

  return (
    <>
      <div className="techcreate">
        <button onClick={techNewsApi()}>click</button>
        {/* <div>{techs && <h2>length {techs.length}</h2>}</div> */}
        {/* <div>Title -- {title && <h2>{title}</h2>}</div> */}
        {/* <div>Author -- {author && <h2>{author}</h2>}</div> */}
      </div>
    </>
  );
};

export default TechCreateNewsApi;
