import React from 'react'


function Login(){
    // #want auth url to load as the login is created and username
    
    
    
    function LoginReddit(){
        fetch('http:/localhost:65010/login').then(res => res.json()).then(data => window.location.href = data.login_url)
    }



    return(
        <div>
            <h1>Connect Your Reddit Account</h1>
            <button onClick={LoginReddit}> Login </button>
        </div>
        
    )
}

export default Login


// class Login extends React.Component{
//     // #want auth url to load as the login is created and username
//     // const username = fetch('http://127.0.0.1:65010/getuser').then(res => res.json()).then(data => console.log(data))

//     constructor(){
//         super()
//         this.auth_url
//         fetch('http://127.0.0.1:65010/').then(res => res.json()).then(data => this.auth_url = data.login_url)
//     }

//     render(){
//         return(
//             <div>
//                 <h1>Connect Your Reddit Account</h1>
//                 <button onClick={GetLoginUrl}> Login </button>
//             </div>
            
//         )
//     }
    
// }

// export default Login