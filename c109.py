import pandas as pd
import plotly.figure_factory as ff
import statistics
import csv

df = pd.read_csv("heiwei.csv")

hlist =df["Height(Inches)"].to_list()
wlist =df["Weight(Pounds)"].to_list()

hmean =statistics.mean(hlist)
wmean =statistics.mean(wlist)

hmedian =statistics.median(hlist)
wmedian =statistics.median(wlist)

hmode =statistics.mode(hlist)
wmode =statistics.mode(wlist)

hstdev =statistics.stdev(hlist)
wstdev =statistics.stdev(wlist)

print(f"mean, median, mode of height is {hmean}, {hmedian}, {hmode}")
print(f"mean, median, mode of height is {wmean}, {wmedian}, {wmode}")

hstdev_1_start =hmean-hstdev
hstdev_1_end =hmean+hstdev

hstdev_2_start =hmean-(2*hstdev)
hstdev_2_end =hmean+(2*hstdev)

hstdev_3_start =hmean-(3*hstdev)
hstdev_3_end =hmean+(3*hstdev)

wstdev_1_start =wmean-wstdev
wstdev_1_end =wmean+wstdev

wstdev_2_start =wmean-(2*wstdev)
wstdev_2_end =wmean+(2*wstdev)

wstdev_3_start =wmean-(3*wstdev)
wstdev_3_end =wmean+(3*wstdev)

data_1_h =[i for i in hlist if i>hstdev_1_start and i<hstdev_1_end]
data_2_h =[i for i in hlist if i>hstdev_2_start and i<hstdev_2_end]
data_3_h =[i for i in hlist if i>hstdev_3_start and i<hstdev_3_end]

data_1_w =[i for i in wlist if i>wstdev_1_start and i<wstdev_1_end]
data_2_w =[i for i in wlist if i>wstdev_2_start and i<wstdev_2_end]
data_3_w =[i for i in wlist if i>wstdev_3_start and i<wstdev_3_end]

percentage_1_h =len(data_1_h)*100/len(hlist)
percentage_2_h =len(data_2_h)*100/len(hlist)
percentage_3_h =len(data_3_h)*100/len(hlist)

percentage_1_w =len(data_1_w)*100/len(wlist)
percentage_2_w =len(data_2_w)*100/len(wlist)
percentage_3_w =len(data_3_w)*100/len(wlist)

print(f"{percentage_1_h}, of data for height lies 1 deviation")
print(f"{percentage_2_h}, of data for height lies 2 deviation")
print(f"{percentage_3_h}, of data for height lies 3 deviation")

print(f"{percentage_1_w}, of data for weight lies 1 deviation")
print(f"{percentage_2_w}, of data for weight lies 2 deviation")
print(f"{percentage_3_w}, of data for weight lies 3 deviation")

fig= ff.create_distplot([hlist], ["height"])
fig.show()
