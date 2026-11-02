#IoT sensor data analysis using Numpy
import numpy as np
sensor_data=np.array([24.5,25.1,26.3,27.0,28.2,29.,27.8,26.5,25.7,30.2])
print("sensor data:",sensor_data)
print("mean:",round(np.mean(sensor_data),2))
print("median:",round(np.median(sensor_data),2))
print("minimum:",np.min(sensor_data))
print("maximum:",np.max(sensor_data))
print("std.Dev.:",round(np.std(sensor_data),2))
threshold=28.0
high_values=sensor_data[sensor_data>threshold]
print("values above",threshold,":",high_values)
