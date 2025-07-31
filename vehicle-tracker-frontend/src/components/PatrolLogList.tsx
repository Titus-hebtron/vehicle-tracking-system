import React, { useEffect, useState } from 'react';
import './PatrolLogList.css';

type Vehicle = {
    id: number;
    plate_number: string;
    model: string;
    driver_name: string;
};

type PatrolLog = {
    id: number;
    vehicle_id: number;
    location: string;
    latitude?: number;
    longitude?: number;
    activity?: string;
    timestamp: string;
    vehicle?: Vehicle;
};

type NewPatrolLog = {
    vehicle_id: number;
    location: string;
    latitude?: number;
    longitude?: number;
    activity?: string;
};

const PatrolLogList: React.FC = () => {
    const [logs, setLogs] = useState<PatrolLog[]>([]);
    const [loading, setLoading] = useState(true);
    const [search, setSearch] = useState('');
    const [newLog, setNewLog] = useState<NewPatrolLog>({
        vehicle_id: 0,
        location: '',
        latitude: undefined,
        longitude: undefined,
        activity: '',
    });

    // Fetch patrol logs
    const fetchLogs = () => {
        fetch('http://localhost:8000/patrol-logs/')
            .then(res => res.json())
            .then(data => {
                setLogs(data);
                setLoading(false);
            });
    };

    useEffect(() => {
        fetchLogs();
    }, []);

    // Create patrol log
    const handleCreate = (e: React.FormEvent) => {
        e.preventDefault();
        fetch('http://localhost:8000/patrol-logs/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(newLog),
        })
            .then(res => res.json())
            .then(() => {
                setNewLog({
                    vehicle_id: 0,
                    location: '',
                    latitude: undefined,
                    longitude: undefined,
                    activity: '',
                });
                fetchLogs();
            });
    };

    // Delete patrol log
    const handleDelete = (id: number) => {
        fetch(`http://localhost:8000/patrol-logs/${id}`, {
            method: 'DELETE',
        })
            .then(res => res.json())
            .then(() => fetchLogs());
    };

    // Filter logs by location or activity
    const filteredLogs = logs.filter(
        log =>
            log.location.toLowerCase().includes(search.toLowerCase()) ||
            (log.activity ?? '').toLowerCase().includes(search.toLowerCase())
    );

    if (loading) return <div style={{ padding: 24 }}>Loading patrol logs...</div>;

    return (
        <div className="patrol-dashboard-bg">
            <div className="patrol-dashboard-card">
                <h2 className="patrol-dashboard-title">🚓 Patrol Logs Dashboard</h2>

                {/* Search/filter */}
                <input
                    type="text"
                    placeholder="Search by location or activity"
                    value={search}
                    onChange={e => setSearch(e.target.value)}
                    className="patrol-dashboard-search"
                />

                {/* Create form */}
                <form onSubmit={handleCreate} className="patrol-dashboard-form">
                    <input
                        type="number"
                        placeholder="Vehicle ID"
                        value={newLog.vehicle_id || ''}
                        onChange={e => setNewLog({ ...newLog, vehicle_id: Number(e.target.value) })}
                        required
                    />
                    <input
                        type="text"
                        placeholder="Location"
                        value={newLog.location}
                        onChange={e => setNewLog({ ...newLog, location: e.target.value })}
                        required
                    />
                    <input
                        type="number"
                        step="any"
                        placeholder="Latitude"
                        value={newLog.latitude ?? ''}
                        onChange={e => setNewLog({ ...newLog, latitude: e.target.value ? Number(e.target.value) : undefined })}
                    />
                    <input
                        type="number"
                        step="any"
                        placeholder="Longitude"
                        value={newLog.longitude ?? ''}
                        onChange={e => setNewLog({ ...newLog, longitude: e.target.value ? Number(e.target.value) : undefined })}
                    />
                    <input
                        type="text"
                        placeholder="Activity"
                        value={newLog.activity}
                        onChange={e => setNewLog({ ...newLog, activity: e.target.value })}
                    />
                    <button type="submit">
                        Add Patrol Log
                    </button>
                </form>

                {/* Table */}
                <div className="patrol-dashboard-table-container">
                    <table className="patrol-dashboard-table">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Vehicle</th>
                                <th>Location</th>
                                <th>Latitude</th>
                                <th>Longitude</th>
                                <th>Activity</th>
                                <th>Timestamp</th>
                                <th>Delete</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredLogs.map(log => (
                                <tr key={log.id}>
                                    <td>{log.id}</td>
                                    <td>
                                        {log.vehicle
                                            ? `${log.vehicle.plate_number} (${log.vehicle.model})`
                                            : log.vehicle_id}
                                    </td>
                                    <td>{log.location}</td>
                                    <td>{log.latitude ?? '-'}</td>
                                    <td>{log.longitude ?? '-'}</td>
                                    <td>{log.activity ?? '-'}</td>
                                    <td>{new Date(log.timestamp).toLocaleString()}</td>
                                    <td>
                                        <button
                                            className="patrol-dashboard-delete-btn"
                                            onClick={() => handleDelete(log.id)}
                                        >
                                            Delete
                                        </button>
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    );
};

export default PatrolLogList;