import React from "react";

export default function index(props) {
  console.log("props", props);
  return <div onClick={()=>alert()}>ind</div>;
}

export function getServerSideProps(ctx) {
    console.log('ctx', ctx)
  return {
    props: {
      hiii: "hiii",
    },
  };
}
