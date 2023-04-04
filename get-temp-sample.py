from sense_hat import SenseHat

sense = SenseHat()
#sense.set_imu_config(False, False, True)

temp = round(sense.temp, 2)
print("Temperature: %s C" % temp)

humid = round(sense.humidity, 2)
print("Humidity: %s %%" % humid)

pressure = round(sense.pressure, 2)
print("Pressure: %s Millibars" % pressure)

t1 = sense.get_temperature_from_humidity()
t2 = sense.get_temperature_from_pressure()

print(t2)
print(t2)

#orientation = sense.orientation
#print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

#north = sense.compass
#print("North: %s" % north)

#accel_only = sense.accelerometer
#print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))
