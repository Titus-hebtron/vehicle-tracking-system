# Vehicle Tracker Frontend

## Overview
The Vehicle Tracker Frontend is a React application that interfaces with the Vehicle Tracker Backend. It provides a user-friendly interface for tracking vehicles and their activities.

## Project Structure
```
vehicle-tracker-frontend
├── public
│   └── index.html          # Main HTML file
├── src
│   ├── components          # Contains reusable components
│   │   └── VehicleList.tsx # Component to display a list of vehicles
│   ├── pages               # Contains page components
│   │   └── Dashboard.tsx    # Main application page
│   ├── App.tsx             # Main application component
│   ├── index.tsx           # Entry point for the React application
│   └── types               # TypeScript types and interfaces
│       └── index.ts        # Type definitions
├── package.json            # npm configuration file
├── tsconfig.json           # TypeScript configuration file
└── README.md               # Project documentation
```

## Setup Instructions
1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd vehicle-tracker-frontend
   ```

2. **Install dependencies:**
   ```
   npm install
   ```

3. **Run the application:**
   ```
   npm start
   ```

4. **Open your browser:**
   Navigate to `http://localhost:3000` to view the application.

## Usage
- The main page of the application is the Dashboard, which includes a list of vehicles and their details.
- The VehicleList component fetches data from the backend API and displays it in a user-friendly format.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.