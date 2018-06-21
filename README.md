# Micropython library for the BME680 sensor

# Overview
This code base was taken from a few different upstream sources.   
Modified only slightly to work with the DF-Robot ESP32 and the DF-Robot BME680 sensor.   

# Usage
See my [micropython wrapper library](https://gitlab.com/brendanhoran/esp32_modules/tree/master/bme680), it will handle all the common functions.
In addition I added an IAQ scoring function.   
Has better exception handling built in as well.   

# Upstream sources :
[Python BME680 library](https://github.com/pimoroni/bme680)  
[Micropython changes above](https://github.com/robmarkcole/bme680-mqtt-micropython)
[Custom I2C Libary](https://github.com/gkluoe/bme680/blob/master/library/bme680/i2c.py)

