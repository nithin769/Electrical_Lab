import numpy as np
import matplotlib.pyplot as plt

# Define extended time axis for better visualization (20 clock cycles)
extended_time = np.arange(0, 31, 1)

# Define clock signal (toggling every cycle)
clk_extended = [1 if i % 2 == 0 else 0 for i in extended_time]

# Initialize Q0, Q1, Q2 for MOD-7 counter
Q0_extended = [0] * len(extended_time)  # LSB
Q1_extended = [0] * len(extended_time)
Q2_extended = [0] * len(extended_time)  # MSB

count = 0  # 3-bit counter

for i in range(len(extended_time)):
    # Update flip-flop states on falling edge (clk goes from 1 to 0)
    if clk_extended[i] == 0 and clk_extended[i - 1] == 1 if i > 0 else False:
        count = (count + 1) % 7  # Increment counter (mod-7 behavior)

    # Assign binary values to Q0, Q1, Q2
    Q0_extended[i] = (count >> 0) & 1
    Q1_extended[i] = (count >> 1) & 1
    Q2_extended[i] = (count >> 2) & 1

# Plot the MOD-7 counter timing diagram with proper spacing
plt.figure(figsize=(12, 7))  # Increased width for better spacing
plt.title("MOD-7 Counter Timing Diagram (T Flip-Flops, Falling Edge)")

# Offset each waveform for better visibility
plt.step(extended_time, np.array(clk_extended) + 6, where='post', label="Clock", linewidth=2, color='k')
plt.step(extended_time, np.array(Q2_extended) + 4, where='post', label="Q3", linewidth=2, color='r')
plt.step(extended_time, np.array(Q1_extended) + 2, where='post', label="Q2", linewidth=2, color='g')
plt.step(extended_time, np.array(Q0_extended), where='post', label="Q1", linewidth=2, color='b')

# Formatting plot
plt.xlabel("Clock Pulses")
plt.ylabel("State Levels")
plt.xticks(np.arange(0, 31, 1))
plt.yticks([0, 2, 4, 6], labels=["Q1", "Q2", "Q3", "Clock"])
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.show()

