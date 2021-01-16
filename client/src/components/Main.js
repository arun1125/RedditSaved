import React from 'react'
import PostForest from './PostForest'
import Reload from './Reload'
// import AddEmail from './AddEmail'
import {useParams} from "react-router-dom"


function Main(){
    // https://stackoverflow.com/questions/63660520/typescript-error-after-upgrading-version-4-useparams-from-react-router-dom-pr
    const  access_token = useParams()
    
    // console.log(access_token)
    return(
        
        <div>
            <PostForest {... access_token}/>
            <Reload />
            {/* <AddEmail {... access_token}/> */}
        </div>
    ) 
}


export default Main

// class Main extends React.Component{
//     constructor(){
//         super()
//     }

//     render(){
//         const { access_token } = useParams<{ access_token : string}>()

//         return(
//             <div>
//                 <PostForest access_token = {access_token} />
//                 <Reload />
//                 <AddEmail />
//             </div>
//         ) 
//     }
// }

// export default Main
