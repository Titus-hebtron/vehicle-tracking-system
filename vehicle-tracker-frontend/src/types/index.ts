export interface Vehicle {
    id: number;
    plate_number: string;
    model: string;
    driver_name: string;
}

export interface PatrolLog {
    id: number;
    vehicle_id: number;
    location: string;
    latitude?: number;
    longitude?: number;
    activity?: string;
    timestamp: string;
    vehicle: Vehicle;
}