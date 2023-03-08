
import geopandas as gpd
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geoplot as gplt

vietnam_map = gpd.read_file("C:/Users/quyen/Downloads/diaphantinh.geojson")

# Load the "mat-do-dan-so.csv" file
pop_data = pd.read_csv("C:/Users/quyen/Downloads/mat-do-dan-so.csv")


pop_data = pop_data[pop_data.province != 'CẢ NƯỚC']
pop_data = pop_data[pop_data.province != 'Đồng bằng sông Hồng']
pop_data = pop_data[pop_data.province != 'Trung du và miền núi phía Bắc']

pop_data = pop_data[pop_data.province != 'Bắc Trung Bộ và Duyên hải miền Trung']
pop_data = pop_data[pop_data.province != 'Đồng bằng sông Cửu Long']
pop_data = pop_data[pop_data.province != 'Đông Nam Bộ']
pop_data = pop_data[pop_data.province != 'Tây Nguyên']




pop_data = pop_data.sort_values(by=['province'])
pop_data = pop_data.reset_index()
del pop_data['index']



province = vietnam_map['ten_tinh']
province = province.sort_values()
province = pd.DataFrame(province)
province = province.reset_index()
del province['index']

pop_data = pop_data.join(province)

del pop_data['province']



merged_data = vietnam_map.merge(pop_data, left_on = ['ten_tinh'], right_on=['ten_tinh'])

merged_data["log_population"] = np.log(merged_data["density"])

fig, ax = plt.subplots(figsize=(12, 8))
merged_data.plot(column="log_population", ax=ax, cmap="Oranges", edgecolor="black")
ax.set_title("the population of Vietnam", fontsize=16)
ax.axis("off")
plt.show()


sorted_data = pop_data.sort_values("density", ascending=False)

df_10 = sorted_data[:10]

x = df_10['ten_tinh']
y = df_10['density']

plt.bar(x, y, width=0.9)
plt.xticks(rotation = 80)
plt.show()

plt.hlines(x, xmin = 0, xmax = y, color = "b")

plt.plot(y,x, 'o')





