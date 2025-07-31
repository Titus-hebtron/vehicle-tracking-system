import React from 'react';
import VehicleList from '../components/VehicleList';
import PatrolLogList from '../components/PatrolLogList';

const Dashboard: React.FC = () => {
    return (
        <div>
            <h1>Dashboard</h1>
            <VehicleList />
            <PatrolLogList />
        </div>
    );
};

export default Dashboard;