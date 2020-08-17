
// const Dashboard = require("./components/dashboard");

// const Table = required("./components/table")

import Dashboard from './components/dashboard'

class App extends React.Component {

    render() {
        return (
            <Dashboard />
            <Table />
        );
    }
};

ReactDOM.render(
    <App />,
    document.getElementById('root')
);;