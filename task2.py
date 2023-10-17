mport numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
X_train = np.random.rand(1000, 2, 3)  # 1000 samples of 2x3 matrices
Y_train = np.random.rand(1000, 3, 2)  # 1000 samples of 3x2 matrices
model = Sequential()
model.add(Dense(64, input_shape=(2 * 3,), activation='relu'))
model.add(Dense(6))
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train.reshape(-1, 2 * 3), Y_train.reshape(-1, 3 * 2), epochs=100, batch_size=32)
A = np.random.rand(2, 3)
B = np.random.rand(3, 2)
result = model.predict(A.reshape(1, -1)).reshape(3, 2)

print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Result of A * B:")
print(result)
