# Pure demo, total crap code
# this is just my notes really 
# needs 5mins for gas sensor to stable

import bme680
from i2c import I2CAdapter
import time
from time import sleep
import machine

sleep(10)
i2c_dev = I2CAdapter(scl=machine.Pin(22), sda=machine.Pin(21))
sensor = bme680.BME680(i2c_device=i2c_dev)

sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

sensor.set_gas_status(bme680.ENABLE_GAS_MEAS)
sensor.set_gas_heater_temperature(320)
sensor.set_gas_heater_duration(150)
sensor.select_gas_heater_profile(0)

print(sensor.get_sensor_data())
print(sensor.data.heat_stable)
print(sensor.data.temperature)
print(sensor.data.pressure)
print(sensor.data.humidity)
print(sensor.data.gas_resistance)
