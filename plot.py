import pandas as pd
import matplotlib.pyplot as plt

# print(df)
plt.figure(dpi=300)
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["NimbusRomNo9L"],
    'font.size': 12
})
Ctype = "Fading"
# Ctype = "AWGN"
# model = "JSCC"
# model = "JSCCF"
model = "GAN"



df = pd.read_csv('./test_results/test_results_0SNR_' + Ctype + '_' + model + '.csv')
plt.plot(df['SNR'],df['PSNR'],'-c',marker="o",label='SNR Train 0 dB')

df = pd.read_csv('./test_results/test_results_5SNR_' + Ctype + '_' + model + '.csv')
plt.plot(df['SNR'],df['PSNR'],'-r',marker="^",label='SNR Train 5 dB')

df = pd.read_csv('./test_results/test_results_10SNR_' + Ctype + '_' + model + '.csv')
plt.plot(df['SNR'],df['PSNR'],'-b',marker="s",label='SNR Train 10 dB')

df = pd.read_csv('./test_results/test_results_20SNR_' + Ctype + '_' + model + '.csv')
plt.plot(df['SNR'],df['PSNR'],'-g',marker="p",label='SNR Train 20 dB')

# plt.xlim(0,25)
plt.grid()
plt.tick_params(direction='in')
plt.title(Ctype + " channel " + model + " model")   
plt.legend(loc='lower right')
plt.ylabel('PSNR (dB)')
plt.xlabel('SNR Test (dB)')
plt.savefig('Fig6.pdf', format="pdf", dpi=300)
plt.show()

# plt.close()
