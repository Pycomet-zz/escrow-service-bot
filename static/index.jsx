
// const Dashboard = () => { 
//     return (
//         <section>
//             <p>React Is Active 🤯</p>
//         </section>
//     );
// }
class Dashboard extends React.Component {

    render() { 
        return (
            <section>
                <p>React Component Is Active 🤯</p>
            </section>
        );
    }

};
 



ReactDOM.render(
    <Dashboard />,
    document.getElementById('root')
);