import React from "react"


function Reload(){
    return(
        <div>
            <h1>Feelin' Lucky?</h1>
            <button onClick = {() => window.location.reload(false)}> Refresh </button>
        </div>
        
    )
}

export default Reload