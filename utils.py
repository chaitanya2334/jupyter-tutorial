import numpy as np
import matplotlib.pyplot as plt
    
def plot_sine():
    time = np.arange(0, 10, 0.1);
    amplitude = np.sin(time)
    plt.plot(time, amplitude)
    plt.title('Sine wave')
    plt.xlabel('Time')
    plt.ylabel('Amplitudeasdf')
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')