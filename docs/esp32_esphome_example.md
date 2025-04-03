# 🔌 ESPHome Example Configuration

Here is a basic example of an ESPHome config that listens to timer settings:

```yaml
substitutions:
  devicename: timer_display

esphome:
  name: ${devicename}

esp32:
  board: esp32dev

mqtt:
  broker: !secret mqtt_broker

logger:

ota:

api:

display:
  - platform: max7219
    cs_pin: GPIO5
    num_chips: 4
    rotate_chip: 180
    intensity: 3
    lambda: |-
      it.print("READY");

buzzer:
  - platform: gpio
    pin: GPIO18
    id: buzzer

mqtt_subscribe:
  - topic: "bearstorm/timer/settings"
    id: settings_sub
    on_message:
      then:
        - lambda: |-
            // Parse and use values
  - topic: "bearstorm/timer/command"
    on_message:
      then:
        - if:
            condition:
              lambda: 'return x == "start";'
            then:
              - logger.log: "Timer started"
