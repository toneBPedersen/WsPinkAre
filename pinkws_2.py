#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read data

tot_master_df = pd.read_excel('output_from_15001.xlsx')

#Slice data set

rev_songs = tot_master_df.iloc[:,4:24]
tot_rev= rev_songs.sum(axis=1)


#Quantile

q10 = tot_rev.quantile(0.1)
q90 = tot_rev.quantile(0.9)

mean_tot_rev = tot_rev.mean()
median_tot_rev = tot_rev.median()
max_tot_rev = tot_rev.max()

tot_rev_10 = tot_rev[tot_rev<q10]
tot_rev_90 = tot_rev[tot_rev>q90]

print 'low quantile:',q10
print 'high quantile:',q90
print 'max:', max_tot_rev
print 'mean:', mean_tot_rev
print 'median:', median_tot_rev


#Run script

#plot
rev_songs_low = rev_songs.iloc[tot_rev_10]
rev_songs_high = rev_songs.iloc[tot_rev_90]


rev_songs_low.plot()

plt.show()





