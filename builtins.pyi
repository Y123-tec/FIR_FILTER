import numpy as np
import matplotlib.pyplot as plt

def to_decimal(binary_str, bit_width):
    assert len(binary_str) <= bit_width
    value = int(binary_str, 2)
    sign_bit = 1 << (bit_width - 1)
    return (value & (sign_bit - 1)) - (value & sign_bit)

# Filter coefficients and bit widths
taps = 8
coef_bit_width = 8
input_bit_width = 16
output_bit_width = 32

real_coefficient = 1 / taps
binary_coefficient = np.binary_repr(int(real_coefficient * (2 ** (coef_bit_width - 1))), coef_bit_width)

# Check coefficient value
##coef_value_check = to_decimal(binary_coefficient, coef_bit_width) / (2 ** (coef_bit_width - 1))

# Generate test signal
time_vector = np.linspace(0, 2 * np.pi, 100)
signal_output = np.sin(2 * time_vector) + np.cos(3 * time_vector) + 0.3 * np.random.randn(len(time_vector))

plt.plot(signal_output)
plt.show()

# Convert signal to N2-bit signed representation
binary_signal = [np.binary_repr(int(val * (2 ** (coef_bit_width - 1))), input_bit_width) for val in signal_output]

# Save the converted signal to a data file
with open('input.data', 'w') as file:
    for binary_val in binary_signal:
        file.write(binary_val + '\n')

# after this line, you need to run the Vivado code

# from here, we read the filtered values, convert them to decimal representation
# and plot the filtered results

read_b=[]

# read data
with open("save.data") as file:
    for line in file:
        read_b.append(line.rstrip('\n'))

# this list contains the converted values
n_l=[]
for by in read_b:
    n_l.append(to_decimal(by, output_bit_width) / (2 ** (2 * (coef_bit_width - 1))))

plt.plot(signal_output, color='blue', linewidth=3, label='Original signal')
plt.plot(n_l, color='red', linewidth=3, label='Filtered signal')
plt.legend()
plt.savefig('results.png', dpi=600)
plt.show()
