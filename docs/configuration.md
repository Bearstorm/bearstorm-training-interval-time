# ⚙️ Configuration & MQTT

The addon communicates with an ESP32 device using MQTT.

## Required:

- Home Assistant with Mosquitto MQTT broker
- ESPHome configured ESP32

## MQTT Topics:

| Topic                         | Payload Example                          |
|------------------------------|-------------------------------------------|
| `bearstorm/timer/settings`   | `{ "work": 45, "rest": 15, "rounds": 8 }` |
| `bearstorm/timer/command`    | `"start"` / `"stop"`                      |
| `bearstorm/timer/status`     | `{ "mode": "WORK", "round": 3, "time_left": 28 }` |

The addon also includes a REST API (see [API Reference](api.md)).
