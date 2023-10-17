import tensorflow as tf
from tensorflow import keras
data = [
    ([1, 2], 3),
    ([2, 3], 5),
    ([5, 10], 15),]
inputs = [pair[0] for pair in data]
outputs = [pair[1] for pair in data]

model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(2,), activation='relu'),  # Input layer with 2 input nodes
    keras.layers.Dense(1)])  # Output layer with 1 output node
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(inputs, outputs, epochs=1000)  # You can adjust the number of epochs as needed
result = model.predict([[3, 4]])
print("Result:", result[0][0])  # Output: Result: 7.00123 (the exact value might vary)
