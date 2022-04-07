import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import cv2

data = pd.read_excel('code_week3/datasets/final_dataset.xlsx')
print(data.info())

# data.plot(kind='scatter', y = "Value", x = "Gls (20/21)")
# plt.show()

from pandas.plotting import scatter_matrix
features_to_draw = ["Age", "Value", "Gls (20/21)", "Ast (20/21)", "Penalties Scored (20/21)"]
    
scatter_matrix(data[features_to_draw], figsize=(12, 8))
plt.savefig('code_week3/figures/chart.png',format='png')
plt.show()
