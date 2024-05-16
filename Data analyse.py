import pandas as pd
import matplotlib.pyplot as plt
from distfit import distfit
from fitter import Fitter, get_common_distributions, get_distributions

import scipy.stats as st


# def get_best_distribution(data):
#     dist_names = ["norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme"]
#     dist_results = []
#     params = {}
#     for dist_name in dist_names:
#         dist = getattr(st, dist_name)
#         param = dist.fit(data)
#
#         params[dist_name] = param
#         # Applying the Kolmogorov-Smirnov test
#         D, p = st.kstest(data, dist_name, args=param)
#         print("p value for " + dist_name + " = " + str(p))
#         dist_results.append((dist_name, p))
#
#     # select the best fitted distribution
#     best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
#     # store the name of the best fit and its p value
#
#     print("Best fitting distribution: " + str(best_dist))
#     print("Best p value: "+ str(best_p))
#     print("Parameters for the best fit: " + str(params[best_dist]))
#
#     return best_dist, best_p, params[best_dist]


# dist = distfit()
# Lees het Excel-bestand
xlsx = pd.ExcelFile('Data/Extruder_Opvolging_Productie.xlsx')
df3 = pd.read_excel(xlsx, 'Extruder_3')
df4 = pd.read_excel(xlsx, 'Extruder_4')
df5 = pd.read_excel(xlsx, 'Extruder_5')

# print("Extruder 3")
# get_best_distribution(df3['Count OK'])
#
# print("Extruder 4")
# get_best_distribution(df4['Count OK'])
#
# print("Extruder 5")
# get_best_distribution(df5['Count OK'])

# dist.fit_transform(df3['Count OK'])

df3.hist(column='Count OK', bins=120)
# df4.hist(column='Count OK', bins=120)
# df5.hist(column='Count OK', bins=120)

plt.show()
# dist.plot()

# f = Fitter(df4['Count OK'])
# f.fit(get_common_distributions())
# best = f.get_best()
# for dist_name, dist_info in best.items():
#     print(f"{dist_name}: {dist_info}")

# print(f.summary())