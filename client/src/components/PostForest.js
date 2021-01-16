import React from "react"
import Post from './Post'

// function PostForest(props: any){
//     // console.log(props)
//     // const access_token = props.access_token

//     // fetch(`http://127.0.0.1:65010/homepage/${ props.access_token }`).then((result)=>{
//     //     result.json().then((resp) => {
//     //         data = resp
//     //     })
//     // })
//     console.log(props)
//     const url = `http://127.0.0.1:65010/homepage/${ props.access_token }`

    
//     async function getPosts(url: string){
//         let val 
//         const response = await fetch(url);
//         const resp = await response.json().then((data) => val = data)


//         // const posts = await resp.map((x:string) => <Post post = {x}/> )
//         // console.log(posts)
//         return val
//     }

//     const test = (async function(){
//         var result = await getPosts(url)
//         return result
//     })()

//     console.log(test)
    


//     return(
//         <div>
//             <Post post = "1"/>
//             <Post post = "2"/>
//             <Post post = "3"/>
//             <Post post = "4"/>
//             <Post post = "5"/>
//         </div>
        
//     )
// }

// export default PostForest

class PostForest extends React.Component{
    // https://stackoverflow.com/questions/47561848/property-value-does-not-exist-on-type-readonly
    constructor(props){
        super(props)

        this.state = {
            posts: []
        }
    }

    componentDidMount(){
//https://www.robinwieruch.de/react-fetching-data
        const token = Object.values(this.props)[0]
        const url = `http://reddit-saved.us-east-2.elasticbeanstalk.com/homepage/${ token }`

        
        fetch(url).then(resp => resp.json())
        .then(data => this.setState({ posts: data }))

    }

    render(){
        
        const { posts } = this.state

        const posts_ = Object.entries(posts).slice(0,5).map(post => <Post key = {post[0]} post = {post[1]}/>)


        return(
            <div>
            {posts_}
        </div>
        )
    }
}

export default PostForest