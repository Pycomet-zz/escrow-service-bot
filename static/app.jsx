
// const Dashboard = require("./components/dashboard");

// const Table = required("./components/table")

// import Dashboard from './components/dashboard'

// class App extends React.Component {

//     render() {
//         return (
//             <section>
//                 <p>React Component Is Active 🤯</p>
//             </section>
//         );
//     }
// };

function App() {
    const [errors, setErrors] = useState(true);
    const [users, setUsers] = useState({});
    const apiUrl = `https://0.0.0.0:5000/api/v1/users`;

    async function fetchData() {
        const res = await fetch(apiUrl);
        res
          .json()
          .then(res => setUsers(res))
          .catch(() => setErrors(false));
    };

    useEffect(() => {
        fetchData();
    });
    
    console.log(users);
    return (
        <section>
            {/* <h1>{users}</h1>
            <p>React Component Is Active 🤯</p> */}
            {
                errors ?
                <p>Big Error</p> :
                <p>React Component Is Active 🤯 {users}</p> 
            }
        </section>
    );
}

ReactDOM.render(
    <App />,
    document.getElementById('root')
);