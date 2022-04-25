import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.sin(2*x + 90)
dataframe = {
    "Nilai x ": x,
    "f(x)": y
}
df_fungsi = pd.DataFrame(dataframe)

df_fungsi
