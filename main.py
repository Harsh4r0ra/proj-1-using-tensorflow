import warnings 
warnings.simplefilter(action='ignore', category=FutureWarning)
import tensorflow as tf 
import numpy as np 
from tensorflow import keras 
from tensorflow.python.util import deprecation 
deprecation._PRINT_DEPRECATION_WARNINGS = False 

# Define the neural network
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])]) 

# Compile the neural network
model.compile(optimizer='sgd', loss='mean_squared_error') 

# Provide the data
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float) 
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float) 

# Train the neural network
model.fit(xs, ys, epochs=500)

# Use the trained model to make predictions
print(model.predict([10.0]))
