import React from "react"

function Post(props){

    const url = `https://reddit.com${props.post}`


    return(
        <div>
            {/* //https://stackoverflow.com/questions/42914666/react-router-external-link */}
            <a target="_blank" rel="noreferrer" href={url}>
                <button>
                    {props.post}
                </button>
            </a>
        </div>
        
    )
}

export default Post
