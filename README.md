Its called Titanic makes cool dashboard. For the rest I Ai generated it .. will actually make a readme later. 


# Titan's Overview 🚀

Titan's Overview is a lightweight, real-time hardware telemetry dashboard. It features a responsive, glassmorphic frontend UI powered by **Chart.js** and an asynchronous **Flask** backend engine utilizing **psutil** to extract deep system metrics (CPU core splits, thermals, virtual memory footprints, and network interface velocities).

---

## 🛠️ System Architecture

The application is split into two primary layers operating over a localized network loop:
* **Telemetry Engine (Backend):** A Python Flask API that samples OS kernel hardware states, handles multi-platform sensor fallbacks, and calculates network delta speeds.
* **Visualizer Frame (Frontend):** A modular CSS Grid and HTML5 Canvas layout that handles real-time First-In, First-Out (FIFO) chart streaming data at a continuous 2-second heartbeat cadence.

---

## ⚡ Features

- **Granular CPU Tracking:** Multi-series real-time line charts tracking individual logical thread loads dynamically.
- **Cross-Platform Thermals:** Automatic hardware driver translation layers supporting Intel (`coretemp`), AMD Ryzen (`k10temp`), and Raspberry Pi (`cpu_thermal`).
- **Memory Analytics:** Deep binary-scale byte conversions showing active system allocations versus total physical thresholds.
- **Bandwidth Metering:** Server-side delta tracking processing network velocities into high-level throughput readouts ($\text{Mbps} \uparrow / \downarrow$).
- **Glassmorphic Responsive Design:** A dark-mode user interface engineered with modern CSS visual effects, scaling effortlessly down to mobile viewports.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.8+ installed on your host system.

### 1. Backend Installation & Setup

Clone the repository to your host environment, navigate to the source directory, and follow these steps:

1. **Create a virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

   
   Install system dependencies:Bashpip install flask flask-cors psutil
Deploy the Telemetry Server:Bashpython app.py
The engine will initialize and bind globally to http://0.0.0.0:5000 to allow accessibility from any client machine on your local area network (LAN).
2. Frontend ConfigurationEnsure your static directory layout matches the structured routes:
Plaintext├── app.py                  # Flask Application Engine
├── overview.html           # Main Application UI Viewport
├── CSS/
│   └── styles.css          # Core Layout & Component Variables
└── SideNavigation/
    └── sidebar.html        # Modular Injected Navigation Fragment
Open your web browser and point to http://<your-host-ip>:5000/ to visualize the dashboard canvas.
📡 API Endpoints ReferenceRouteMethodDescriptionSample Payload Data/GETServes the core monolithic dashboard template.
HTML Source/api/tempGETFetches core motherboard packaging thermal data.{"status":"success", "temperature": 48.5, "label": "coretemp"}/api/cpuGETTracks overall usage and per-logical-core percentages.{"status":"success", "overall": 12.5, "per_core": [10.2, 14.8]}/api/memoryGETCaptures virtual memory bytes allocation states.{"status":"success", "total": 17179869184, "used": 8589934592, ...}/api/networkGETReturns raw lifetime I/O counter byte tallies.{"status":"success", "bytes_sent": 4829104, "bytes_recv": 9821044}/api/network_rateGETComputes live bandwidth velocity directly on the host.{"status":"success", "upload_bps": 124500.0, "download_bps": 854200.0}

This is deployed on Arch currently. 



📜 LicenseThis project is open-source and available under the MIT License.



Warning: Comments were created by AI
