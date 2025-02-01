import numpy as np
import matplotlib.pyplot as plt

def to_decimal(binary_str, bit_width):
    assert len(binary_str) <= bit_width
    value = int(binary_str, 2)
    sign_mask = 1 << (bit_width - 1)
    return (value & (sign_mask - 1)) - (value & sign_mask)

# Define filter parameters
taps = 8
coef_bit_width = 8
input_bit_width = 16
output_bit_width = 32

# Compute filter coefficient in binary format
real_coef = 1 / taps
binary_coef = np.binary_repr(int(real_coef * (2 ** (coef_bit_width - 1))), coef_bit_width)

# Generate test signal
time_vector = np.linspace(0, 2 * np.pi, 100)
signal_output = np.sin(2 * time_vector) + 2*np.cos(2 * time_vector)+ 0.3 * np.random.randn(len(time_vector))

# Plot original signal
plt.plot(signal_output)
plt.show()

# Convert signal to binary representation
binary_signal = [np.binary_repr(int(val * (2 ** (coef_bit_width - 1))), input_bit_width) for val in signal_output]

# Write converted signal to file
with open('input.data', 'w') as file:
    file.writelines(f"{b_val}\n" for b_val in binary_signal)

# Execute RTL simulation before proceeding

# Read filtered output from file
filtered_values = []
with open("save.data") as file:
    filtered_values = [line.strip() for line in file]

# Convert filtered values to decimal format
filtered_decimals = [to_decimal(b_val, output_bit_width) / (2 ** (2 * (coef_bit_width - 1))) for b_val in filtered_values]

# Plot original and filtered signals
plt.plot(signal_output, color='blue', linewidth=3, label='Original signal')
plt.plot(filtered_decimals, color='red', linewidth=3, label='Filtered signal')
plt.legend()
plt.savefig('results.png', dpi=600)
plt.show()
