import React, { useEffect, useState } from 'react';

type Vehicle = {
    id: number;
    plate_number: string;
    model: string;
    driver_name: string;
};

const VehicleList: React.FC = () => {
    const [vehicles, setVehicles] = useState<Vehicle[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('http://localhost:8000/vehicles/') // Adjust URL to match your backend
            .then(res => res.json())
            .then(data => {
                setVehicles(data);
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading vehicles...</div>;

    return (
        <div>
            <h2>Vehicles</h2>
            <ul>
                {vehicles.map(vehicle => (
                    <li key={vehicle.id}>
                        {vehicle.plate_number} - {vehicle.model} (Driver: {vehicle.driver_name})
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default VehicleList;