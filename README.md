**Important Note:**  
The files submitted in the previous version were incorrect. After reviewing the project, the correct files have been uploaded. This version (1.1) includes all the necessary updates and fixes.

### Changes Made:
- Replaced old files (only contained the frontend part) with the correct versions.
- Fixed: reuploaded the correct files

# Server Monitoring Dashboard
A web-based dashboard for monitoring server metrics including CPU, RAM, disk usage, and network traffic.
![image](https://github.com/user-attachments/assets/8bce773c-0023-4141-b783-b185f3bafb73)
![image](https://github.com/user-attachments/assets/c8d0386d-f972-4e47-8e8a-1f637e2b28bb)
![image](https://github.com/user-attachments/assets/1245a731-39aa-453f-b0fe-100d1b646519)

## Features

- Real-time server metrics monitoring
- Alert system with critical, medium, and low priority alerts
- Server resource usage visualization
- Network traffic monitoring
- Server list and information display

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the backend server:
```bash
python backend/app.py
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:5000 
