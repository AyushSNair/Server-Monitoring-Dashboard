import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Line, Doughnut } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  ArcElement
} from 'chart.js';
import './App.css';

ChartJS.register(LineElement, CategoryScale, LinearScale, PointElement, ArcElement);

function App() {
  const [metrics, setMetrics] = useState(null);
  const [servers, setServers] = useState([]);
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    fetchMetrics();
    fetchServers();
  }, []);

  const fetchMetrics = async () => {
    try {
      const res = await axios.get('http://localhost:5000/api/metrics');
      setMetrics(res.data);
    } catch (err) {
      console.error('Failed to fetch metrics:', err);
    }
  };

  const fetchServers = async () => {
    try {
      const res = await axios.get('http://localhost:5000/api/servers');
      setServers(res.data);
    } catch (err) {
      console.error('Failed to fetch servers:', err);
    }
  };

  const gaugeOptions = {
    cutout: '80%',
    plugins: {
      legend: { display: false },
    }
  };

  const cpuGaugeData = {
    labels: ['CPU Usage', 'Free'],
    datasets: [{
      data: metrics ? [metrics.cpu_usage, 100 - metrics.cpu_usage] : [0, 100],
      backgroundColor: ['#42a5f5', '#e0e0e0'],
      borderWidth: 0,
      circumference: 180,
      rotation: 270,
    }]
  };

  const memoryGaugeData = {
    labels: ['Memory Usage', 'Free'],
    datasets: [{
      data: metrics ? [metrics.memory_usage, 100 - metrics.memory_usage] : [0, 100],
      backgroundColor: ['#748FFC', '#f0f0f0'],
      borderWidth: 0,
      circumference: 180,
      rotation: 270,
    }]
  };

  const trafficData = {
    labels: metrics ? metrics.traffic.map((_, i) => i) : [],
    datasets: [
      {
        label: 'Incoming',
        data: metrics ? metrics.traffic.map(t => t.incoming) : [],
        fill: false,
        borderColor: '#66bb6a',
        tension: 0.1
      },
      {
        label: 'Outgoing',
        data: metrics ? metrics.traffic.map(t => t.outgoing) : [],
        fill: false,
        borderColor: '#ef5350',
        tension: 0.1
      }
    ]
  };

  return (
    <div className={`app-container ${darkMode ? 'dark' : ''}`}>
      <header>
        <h1>Server Monitoring Dashboard</h1>
        <div>
          <button className="refresh-btn" onClick={fetchServers}>Refresh List</button>
          <button className="dark-mode-toggle" onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? '☀️ Light Mode' : '🌙 Dark Mode'}
          </button>
        </div>
      </header>

      <div className="grid">
        <div className="card cpu-gauge">
          <h2>CPU Usage</h2>
          <div className="gauge-container">
            <Doughnut data={cpuGaugeData} options={gaugeOptions} />
            <div className="gauge-value">
              <span className="value">{metrics ? Math.round(metrics.cpu_usage) : 0}%</span>
              <span className="label">Current Usage</span>
            </div>
          </div>
          <p className="status-text">
            {metrics && metrics.cpu_usage < 70 ? 'CPU load is normal' : 'High CPU load'}
          </p>
        </div>

        <div className="card cpu-gauge">
          <h2>Memory Usage</h2>
          <div className="gauge-container">
            <Doughnut data={memoryGaugeData} options={gaugeOptions} />
            <div className="gauge-value">
              <span className="value">{metrics ? Math.round(metrics.memory_usage) : 0}%</span>
              <span className="label">Current Usage</span>
            </div>
          </div>
          <p className="status-text">
            {metrics && metrics.memory_usage < 75 ? 'Memory usage normal' : 'High memory usage'}
          </p>
        </div>

        <div className="card traffic-graph">
          <h2>Network Traffic</h2>
          <Line data={trafficData} />
        </div>

        <div className="card server-list">
          <h2>Active Servers</h2>
          <ul>
            {servers.map((server, index) => (
              <li key={index}>
                <span>{server.name}</span>
                <span className={`status-badge ${server.status.toLowerCase()}`}>{server.status}</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default App;
