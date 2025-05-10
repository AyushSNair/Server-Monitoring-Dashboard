from flask import Flask, jsonify
from flask_cors import CORS
import random
import time
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Mock data generation functions
def generate_server_metrics():
    return {
        'cpu_usage': random.uniform(0, 100),
        'ram_usage': random.uniform(0, 100),
        'disk_usage': random.uniform(0, 100),
        'app_usage': random.uniform(0, 100)
    }

def generate_network_traffic():
    return {
        'incoming': random.uniform(0, 1000),
        'outgoing': random.uniform(0, 1000),
        'timestamp': datetime.now().isoformat()
    }

def generate_alerts():
    return {
        'critical': random.randint(0, 5),
        'medium': random.randint(0, 10),
        'low': random.randint(0, 15)
    }

def generate_server_list():
    servers = []
    server_names = ['Web Server', 'Database Server', 'Application Server', 'File Server', 'Load Balancer']
    for name in server_names:
        servers.append({
            'id': random.randint(1000, 9999),
            'name': name,
            'status': random.choice(['Online', 'Offline', 'Maintenance']),
            'ip_address': f'192.168.1.{random.randint(1, 255)}',
            'last_updated': datetime.now().isoformat()
        })
    return servers

# API Routes
@app.route('/api/metrics')
def get_metrics():
    return jsonify(generate_server_metrics())

@app.route('/api/network')
def get_network():
    # Generate last 24 hours of network data
    data = []
    for i in range(24):
        timestamp = datetime.now() - timedelta(hours=i)
        data.append({
            'timestamp': timestamp.isoformat(),
            'incoming': random.uniform(0, 1000),
            'outgoing': random.uniform(0, 1000)
        })
    return jsonify(data)

@app.route('/api/alerts')
def get_alerts():
    return jsonify(generate_alerts())

@app.route('/api/servers')
def get_servers():
    return jsonify(generate_server_list())

if __name__ == '__main__':
    app.run(debug=True) 