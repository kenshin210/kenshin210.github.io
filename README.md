# Titanic's Overview 🚀

Titanic's Overview is a lightweight, real-time hardware telemetry dashboard. It features a responsive, glassmorphic frontend UI powered by **Chart.js** and an asynchronous **Flask** backend engine utilizing **psutil** to extract deep system metrics (CPU core splits, thermals, virtual memory footprints, and network interface velocities).Well also linking all subwebpages into one. 





## 🛠️ System Architecture

The application is split into two primary layers operating over a localized network loop:
* **Telemetry Engine (Backend):** A Python Flask API that samples OS kernel hardware states, handles multi-platform sensor fallbacks, and calculates network delta speeds.
* **Visualizer Frame (Frontend):** A modular CSS Grid and HTML5 Canvas layout that handles real-time First-In, First-Out (FIFO) chart streaming data at a continuous 2-second heartbeat cadence.



---

## ⚡ Features
TBD:
- **Granular CPU Tracking:** Multi-series real-time line charts tracking individual logical thread loads dynamically.
- **Cross-Platform Thermals:** Automatic hardware driver translation layers supporting Intel (`coretemp`), AMD Ryzen (`k10temp`), and Raspberry Pi (`cpu_thermal`).
- **Memory Analytics:** Deep binary-scale byte conversions showing active system allocations versus total physical thresholds.
- **Bandwidth Metering:** Server-side delta tracking processing network velocities into high-level throughput readouts ($\text{Mbps} \uparrow / \downarrow$).
- **Glassmorphic Responsive Design:** A dark-mode user interface built around CSS visual effects, scaling effortlessly down to mobile viewports.
- **Includes Quick Access to all essentials for a home lab and media server

---

## 🚀 Getting Started
WIP


### Prerequisites

Will Write this out once i have finished adding everything:

Installed :
Python
Python Addons:
Flask 
Flask-conv

Cockpit
Dockge
Pterodactyl Panel With Wing


Wireguard using Wsg-Easy

Plex Media Server
Prowlarr (Was easier than automating a script for jackett but will revist jacket in the future)
Radarr
Seerr
Sonarr
QBitTorrent

Unifi



To be added:
-Alerts (will be on critical and errors just to reduce overhead)
-Harddrive monitoring
-Design of the whole lab using Visio( Will include CPU core pinning)
-Pre-requisites
-Remove AI writting

To Adjust:
Overview Page
Reduce clutter , change CPU load by core to bar graph (isolating this from being spagetthi)
change the timing increments to 1 minute increments (Remove the x axis have seconds)
Add logging it self as a back end instead of being instantly in your face




 

Specs On Homelab currently:
This is deployed on Arch with Endevouros currently with LTS
2 x Intel Xeon E5-2680v4 
32Gb (2x16Gb) HPE 16GB PC4-2133 Load Reduced DIMMs
2 x 800W PSU
Everything alse is irrelevant for this Currently will add the remainder once i have added other monitoring




📜 LicenseThis project is open-source and available under the MIT License.



Warning: Comments were created by AI
