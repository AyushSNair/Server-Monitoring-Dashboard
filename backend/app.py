from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

class MockDataGenerator:
    """Class to encapsulate mock data generation logic."""

    @staticmethod
    def generate_server_metrics():
        return {
            'cpu_usage': round(random.uniform(0, 100), 2),
            'ram_usage': round(random.uniform(0, 100), 2),
            'disk_usage': round(random.uniform(0, 100), 2),
            'app_usage': round(random.uniform(0, 100), 2)
        }

    @staticmethod
    def generate_network_traffic():
        return {
            'incoming': round(random.uniform(0, 1000), 2),
            'outgoing': round(random.uniform(0, 1000), 2),
            'timestamp': datetime.now().isoformat()
        }

    @staticmethod
    def generate_alerts():
        return {
            'critical': random.randint(0, 5),
            'medium': random.randint(0, 10),
            'low': random.randint(0, 15)
        }

    @staticmethod
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

# --------------------
# API ROUTES
# --------------------

@app.route('/api/status')
def api_status():
    return jsonify({
        'status': 'success',
        'message': 'API is running',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/metrics')
def get_metrics():
    return jsonify({
        'status': 'success',
        'data': MockDataGenerator.generate_server_metrics()
    })

@app.route('/api/network')
def get_network():
    data = []
    for i in range(23, -1, -1):  # reverse to get chronological order
        timestamp = datetime.now() - timedelta(hours=i)
        data.append({
            'timestamp': timestamp.isoformat(),
            'incoming': round(random.uniform(0, 1000), 2),
            'outgoing': round(random.uniform(0, 1000), 2)
        })
    return jsonify({
        'status': 'success',
        'data': data
    })

@app.route('/api/alerts')
def get_alerts():
    return jsonify({
        'status': 'success',
        'data': MockDataGenerator.generate_alerts()
    })

@app.route('/api/servers')
def get_servers():
    return jsonify({
        'status': 'success',
        'data': MockDataGenerator.generate_server_list()
    })

if __name__ == '__main__':
    app.run(debug=True)
