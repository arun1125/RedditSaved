import React from "react"


// function AddEmail(props:any){
//     console.log(props)
//     return(
//         <div>
//             <h1>Enter Your Email Here</h1>
//             <input></input>
//             <button> Submit </button>
//         </div>
        
//     )
// }

class AddEmail extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            Email: "",
            got_email: false
        }
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
    }

    handleChange(event){
        //https://stackoverflow.com/questions/61265736/parameter-e-implicitly-has-an-any-type-react-typescript
        const { name, value } = event.target
        this.setState({
            [name]: value
        })
        //https://stackoverflow.com/questions/46361905/property-is-missing-in-type-x-string-string
    }

    handleSubmit(event){
        event.preventDefault()
        //https://stackoverflow.com/questions/50193227/basic-react-form-submit-refreshes-entire-page
        const Email = this.state.Email
        const token = Object.values(this.props)[0]
        fetch(`http://192.168.99.100:65010/AddEmail/${ token }`, {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              }, 
            method: 'POST',
            body: JSON.stringify(Email)
        }).then(resp => resp.json())
        .then(data => this.setState({got_email:data.got_email}))
    }



    render(){
        console.log(this.state.got_email)
        return(
            <div>
                <h1>Want to get an email instead?</h1>
                <form onSubmit={this.handleSubmit}>
                    <input 
                    type="email"
                    value={this.state.Email}
                    name = "Email"
                    placeholder = "Your Email"
                    onChange = {this.handleChange}>
                    </input>
                    <button>Send</button>
                </form>
            </div>
        )
    }
}

export default AddEmail