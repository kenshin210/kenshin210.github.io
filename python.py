from flask import Flask, render_template, jsonify
from flask_cors import CORS
import psutil
import time

app = Flask(__name__, template_folder='.', static_folder='.')
CORS(app)

# =========================
# HOME PAGE
# =========================
@app.route('/')
def index():
    return render_template('overview.html')


# =========================
# TEMPERATURE
# =========================
@app.route('/api/temp')
def get_temp():
    try:
        temps = psutil.sensors_temperatures()

        target_keys = ['coretemp', 'k10temp', 'acpitz', 'cpu_thermal']
        found_key = next((key for key in target_keys if key in temps), None)

        if found_key and temps[found_key]:
            sensor = temps[found_key][0]
        elif temps:
            first_key = list(temps.keys())[0]
            sensor = temps[first_key][0]
        else:
            return jsonify({
                'status': 'error',
                'error': 'No temperature sensors detected'
            }), 500

        return jsonify({
            'status': 'success',
            'temperature': sensor.current,
            'label': sensor.label or found_key
        })

    except Exception as e:
        return jsonify({'status': 'error', 'error': str(e)}), 500


# =========================
# CPU (FIXED: PER CORE SUPPORT)
# =========================
@app.route('/api/cpu')
def cpu_usage():
    per_core = psutil.cpu_percent(interval=0.5, percpu=True)

    overall = sum(per_core) / len(per_core)

    return jsonify({
        'status': 'success',
        'overall': round(overall, 1),
        'per_core': per_core
    })
# =========================
# MEMORY
# =========================
@app.route('/api/memory')
def memory_usage():
    memory = psutil.virtual_memory()

    return jsonify({
        'status': 'success',
        'total': memory.total,
        'used': memory.used,
        'available': memory.available,
        'percent': memory.percent
    })


# =========================
# NETWORK (RAW TOTALS)
# =========================
@app.route('/api/network')
def network_usage():
    network = psutil.net_io_counters()

    return jsonify({
        'status': 'success',
        'bytes_sent': network.bytes_sent,
        'bytes_recv': network.bytes_recv
    })


# =========================
# NETWORK (OPTIONAL - BETTER FOR CHARTS)
# =========================
_last_net = psutil.net_io_counters()
_last_time = time.time()

@app.route('/api/network_rate')
def network_rate():
    global _last_net, _last_time

    now_net = psutil.net_io_counters()
    now_time = time.time()

    dt = now_time - _last_time
    if dt == 0:
        dt = 0.001

    upload_bps = (now_net.bytes_sent - _last_net.bytes_sent) / dt
    download_bps = (now_net.bytes_recv - _last_net.bytes_recv) / dt

    _last_net = now_net
    _last_time = now_time

    return jsonify({
        'status': 'success',
        'upload_bps': upload_bps,
        'download_bps': download_bps
    })


# =========================
# RUN SERVER
# =========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
