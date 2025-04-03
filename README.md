# Bearstorm Training Interval Timer

**Bearstorm Training Interval Timer** is a multifunctional Home Assistant addon that controls an ESP32-based workout interval timer over MQTT. It offers an intuitive web UI integrated into Home Assistant's sidebar.

## 🔧 Features

- Web-based timer control panel accessible in the HA sidebar
- Custom interval settings: Work, Rest, Rounds
- Presets (Tabata, HIIT, EMOM – coming soon)
- Live training status display
- MQTT communication with ESP32 via ESPHome
- Lightweight Python Flask backend and HTML/JS frontend

## 🔌 MQTT Topics

| Topic                         | Payload                                 |
|------------------------------|------------------------------------------|
| `bearstorm/timer/settings`   | `{ "work": 45, "rest": 15, "rounds": 8 }` |
| `bearstorm/timer/command`    | `"start"` / `"stop"`                     |
| `bearstorm/timer/status`     | `{ "mode": "WORK", "round": 3, "time_left": 28 }` |

## 🧪 Quick Start

1. Clone or copy this repo into:  
   `/addons/local/bearstorm_timer/`
2. In Home Assistant, go to **Settings → Add-ons → Add-on Store → ⋮ → Repositories**
3. Start the addon
4. Open the sidebar panel “Interval Timer”
5. Set your training parameters and start your workout!

## 📦 Architecture

- ESP32 listens for timer commands via MQTT
- Addon hosts a Flask server with REST API
- Frontend fetches and sends commands via the API
- Optional: extend to play sounds via HA media players

## 📄 License

MIT – feel free to remix and improve.
