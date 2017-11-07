#!/usr/bin/env python

import time
import bme680
from beebotte import *

### Replace CHANNEL_TOKEN with that of your channel
bbt = BBT(token = 'CHANNEL_TOKEN')

### Define the wait period between readings (default is 5 minutes in seconds)
period = 300

### Change channel name as suits - in this instance, it is called BME_680
temp_resource = Resource(bbt, 'BME_680', 'temperature')
pressure_resource = Resource(bbt, 'BME_680', 'pressure')
humidity_resource = Resource(bbt, 'BME_680', 'humidity')
airqual_resource = Resource(bbt, 'BME_680', 'airqual')

### Define the BME6809 sensor
sensor = bme680.BME680()

### Oversample settings for the BME680 sensor
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)
sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

print("\n\nCollecting data...")
try:
    while True:
      if sensor.get_sensor_data():
        output_temp = (sensor.data.temperature)
        output_pressure = (sensor.data.pressure)
        output_humidity = (sensor.data.humidity)
        output_airqual = (sensor.data.gas_resistance)
        print(output_temp, output_pressure, output_humidity, output_airqual)
        temp_resource.write(output_temp)
        pressure_resource.write(output_pressure)
        humidity_resource.write(output_humidity)
        airqual_resource.write(output_airqual)

      time.sleep(period)

except KeyboardInterrupt:
    pass

