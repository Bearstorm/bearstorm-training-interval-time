# Bearstorm Training Interval Timer

Multifunkčný addon pre Home Assistant, ktorý ovláda ESP32 tréningový časovač cez MQTT. Nastavuješ work/rest intervaly, sleduješ stav tréningu priamo v UI, všetko z pohodlia Home Assistanta.

## Funkcie
- UI dostupné v bočnom paneli HA
- Ovládanie cez MQTT
- Frontend v HTML/JS, backend v Python Flask
- Kompatibilné s ESPHome

## MQTT Témy
- `bearstorm/timer/settings`
- `bearstorm/timer/command`
- `bearstorm/timer/status`

## Inštalácia
1. Nahraj do `addons/local/bearstorm_timer/`
2. Spusti addon v HA
3. Uži si tréning 😎
