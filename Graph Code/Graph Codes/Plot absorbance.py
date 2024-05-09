import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sampleanew.csv')

plt.plot(df['Position(mm)'], df["Absorbance"])

plt.annotate('40S', xy=(0,0), xytext=(20.3, 0.29))
plt.annotate('60S', xy=(0,0), xytext=(27.7, 0.46))
plt.annotate('80S', xy=(0,0), xytext=(34.7, 0.83))

plt.title("Sample A")
plt.xlabel("Position")
plt.ylabel("Absorbance")

plt.show()
