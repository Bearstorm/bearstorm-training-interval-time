# Bearstorm Training Interval Timer

**Bearstorm Training Interval Timer** is a multifunctional Home Assistant addon that controls an ESP32-based workout interval timer over MQTT. It offers a lightweight web UI integrated directly into the Home Assistant sidebar.

## 🔧 Features

- Web-based timer control panel accessible from the HA sidebar
- Customizable intervals: Work time, Rest time, Rounds
- Live training status display
- MQTT communication with ESP32 (ESPHome)
- Simple Flask backend with HTML/JS frontend
- Ready for mobile/tablet control
- Lightweight and open to contributions

## 📡 MQTT Topics

| Topic                         | Payload Example                          |
|------------------------------|-------------------------------------------|
| `bearstorm/timer/settings`   | `{ "work": 45, "rest": 15, "rounds": 8 }` |
| `bearstorm/timer/command`    | `"start"` / `"stop"`                      |
| `bearstorm/timer/status`     | `{ "mode": "WORK", "round": 3, "time_left": 28 }` |

## 🚀 Quick Start

1. Copy or clone this repo into:  
   `/addons/local/bearstorm_timer/`
2. In Home Assistant:  
   Settings → Add-ons → Add-on Store → ⋮ → Repositories → select your local addon
3. Start the addon
4. Access the "Interval Timer" from the HA sidebar
5. Set your training preferences and go!

## 🤝 Contributing

We welcome contributions from the community!

You can:
- Open [Issues](https://github.com/bearstorm/bearstorm-training-interval-timer/issues)
- Submit [Pull Requests](https://github.com/bearstorm/bearstorm-training-interval-timer/pulls)

Please see our [Contributing Guide](CONTRIBUTING.md) for more information.

## ⚖️ License

This project is licensed under the **Apache License 2.0**.  
If you modify or redistribute this project, **you must credit the original author (Bearstorm)** in your documentation or interface.

See [`LICENSE`](LICENSE) for full details.
