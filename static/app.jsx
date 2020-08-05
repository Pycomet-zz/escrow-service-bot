
var Dashboard = require("./components/dashboard");

class App extends React.Component {

    render() {
        return (
            <Dashboard />
        );
    }
};

ReactDOM.render(
    <App />,
    document.getElementById('root')
);