# Envirotron
Logs temperature and humidity from DHT11, DHT22 or AM2302 sensors over the Raspberry Pi GPIO.

Now supports Pi Camera. Take regular snapshots of your garden and measure your growth!

HINT: use Envirotron in conjunction with Grafana, InfluxDB and Telegraf (or other reliable log processor) to provide live dashboards.


## Installation

1. Clone this repo:

```bash
git clone https://github.com/mike-t/dht22.git
```

2. Create cronjobs for the scripts you want to run:

  * ```run_sensor_local.py``` sensor data to local logfile
  * ```run_sensor_google.py``` sensor data to a Google Sheet (OAuth setup required)
  * ```run_camera.py``` to take a photo

HINT: if you want to use Grafana ensure the suite above is installed and runs at startup. Then, run ```run_sensor_logged.py``` for local logfile and set up Telegraf to process it.

## Roadmap

Evolve into a garden control system. 

* Visual dashboard with guages and live video or snahshots
* dynamic rules to control power based on sensor readings or camera movement. For example:
  * turn on sprinklers if humdity drops below ```50%```
  * engage cooling systems if temperature exceeds ```20C```
  * turn on lights if detect motion above ```20%``` (wildlife deterrent)

Not actively developed, currently in hobbyist mode.
