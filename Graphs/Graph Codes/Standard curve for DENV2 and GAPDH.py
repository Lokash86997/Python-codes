import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sd.csv')

plt.plot(df['log(dilution)'], df['GAPDH'], label='GAPDH', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['DENV2_1'], label='DENV2_1', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['DENV2_2'], label='DENV2_2', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['DENV2_3'], label='DENV2_3', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['DENV2_revcomp_1'], label='DENV2_revcomp_1', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['DENV2_revcomp_2'], label='DENV2_revcomp_2', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['DENV2_revcomp_3'], label='DENV2_revcomp_3', marker='o', linestyle='dotted')
plt.plot(df['log(dilution)'], df['panDENV'], label='DENV2_panDENV', marker='o', linestyle='dotted')

plt.xlabel("Dilution")
plt.ylabel("CT Mean")
plt.title("20240327 Standard Curve DENV2 and GAPDH")

plt.legend()

plt.show()
