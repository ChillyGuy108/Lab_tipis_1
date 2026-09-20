import numpy as np
import matplotlib.pyplot as plt


fs = 1000  
T = 2.0   
t = np.linspace(0, T, int(fs * T), endpoint=False)

frequencies = [1, 2, 4, 8]

fig, axs = plt.subplots(len(frequencies), 4, figsize=(16, 10))
fig.suptitle('Гармонические сигналы, меандры и их спектры (Линейный вид)', fontsize=16)

for i, f in enumerate(frequencies):
    sig_harm = np.sin(2 * np.pi * f * t)
    spec_harm = np.abs(np.fft.rfft(sig_harm)) / len(sig_harm)
    spec_harm[1:] = 2.0 * spec_harm[1:]
    freqs = np.fft.rfftfreq(len(sig_harm), 1/fs)

  
    sig_meander = 0.5 * (np.sign(np.sin(2 * np.pi * f * t)) + 1)
    spec_meander = np.abs(np.fft.rfft(sig_meander)) / len(sig_meander)
    spec_meander[1:] = 2.0 * spec_meander[1:]
    freq_mask = (freqs >= 0) & (freqs <= 35)


    num_samples_to_show = int(fs / f * 2)

  
    axs[i, 0].plot(t[:num_samples_to_show], sig_harm[:num_samples_to_show], color='blue')
    axs[i, 0].set_title(f'Гармоника {f} Гц')
    axs[i, 0].grid(True)
    axs[i, 0].set_ylim(-1.2, 1.2)
    
    axs[i, 1].plot(freqs[freq_mask], spec_harm[freq_mask], color='cyan')
    axs[i, 1].set_title(f'Спектр {f} Гц')
    axs[i, 1].grid(True)
    axs[i, 1].set_xlim(0, 35)
    axs[i, 1].set_ylim(0, 1.2)
    
    axs[i, 2].plot(t[:num_samples_to_show], sig_meander[:num_samples_to_show], color='orange')
    axs[i, 2].set_title(f'Меандр {f} Гц')
    axs[i, 2].grid(True)
    axs[i, 2].set_ylim(-0.2, 1.2)
    
    axs[i, 3].plot(freqs[freq_mask], spec_meander[freq_mask], color='red')
    axs[i, 3].set_title(f'Спектр меандра {f} Гц')
    axs[i, 3].grid(True)
    axs[i, 3].set_xlim(0, 35)
    axs[i, 3].set_ylim(0, 1.2)

plt.tight_layout()
plt.savefig('signals_and_spectra_fixed_lines.png', dpi=300)
plt.show()
plt.show()
