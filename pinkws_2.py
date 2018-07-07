#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read data

tot_master_df = pd.read_excel('Song_rev.xlsx', header=1, index = )

#Slice data set

rev_songs = tot_master_df.iloc[:,3:22]
tot_rev= tot_master_df.iloc[:,23]

#Quantile

q10 = tot_rev.quantile(0.1)
q30 = tot_rev.quantile(0.3)
q90 = tot_rev.quantile(0.9)

mean_tot_rev = tot_rev.mean()
median_tot_rev = tot_rev.median()
max_tot_rev = tot_rev.max()

tot_rev_10 = tot_rev[tot_rev<q10]
tot_rev_10_30 = tot_rev[(q10<tot_rev) & (tot_rev<q30)]
tot_rev_90 = tot_rev[tot_rev>q90]

print 'low quantile:',q10
print 'high quantile:',q90
print 'max:', max_tot_rev
print 'mean:', mean_tot_rev
print 'median:', median_tot_rev

#Run script

#plot
rev_songs_low = rev_songs.loc[tot_rev_10.index]
rev_songs_mid = rev_songs.loc[tot_rev_10_30.index]
rev_songs_high = rev_songs.loc[tot_rev_90.index]

median_low = rev_songs_low.sum(axis=1).median()
median_mid = rev_songs_mid.sum(axis=1).median()
median_high = rev_songs_high.sum(axis=1).median()

song_low = rev_songs_low.iloc[-3,:]
song_mid = rev_songs_mid.iloc[-3,:]
song_high = rev_songs_high.iloc[-3,:]

song_low.plot()
song_mid.plot()
song_high.plot()

x_axis = rev_songs.columns
plt.plot(x_axis, song_low,x_axis, song_mid, x_axis, song_high)

plt.show()

#Cleaned data with revenue for all quarters
rev_songs_with20Q = rev_songs[tot_master_df.iloc[:,24]==20]
tot_rev_with20Q = rev_songs.loc[rev_songs_with20Q.index]

#Find the low, mid, high quantile
q10_with20Q = tot_rev_with20Q.quantile(0.1)
q30_with20Q = tot_rev_with20Q.quantile(0.3)
q90_with20Q = tot_rev_with20Q.quantile(0.9)

tot_rev_10_with20Q = tot_rev_with20Q[tot_rev_with20Q<q10_with20Q]
tot_rev_10_30_with20Q = tot_rev_with20Q[(q10_with20Q<tot_rev_with20Q) & (tot_rev_with20Q<q30_with20Q)]
tot_rev_90_with20Q = tot_rev_with20Q[tot_rev_with20Q>q90_with20Q]

#Get songs from each quantile
rev_songs_low_with20Q = rev_songs_with20Q.loc[tot_rev_10_with20Q.index]
rev_songs_mid_with20Q = rev_songs_with20Q.loc[tot_rev_10_30_with20Q.index]
rev_songs_high_with20Q = rev_songs_with20Q.loc[tot_rev_90_with20Q.index]

song_low_with20Q = rev_songs_low_with20Q.iloc[-3,:]
song_mid_with20Q = rev_songs_mid_with20Q.iloc[-3,:]
song_high_with20Q = rev_songs_high_with20Q.iloc[-3,:]

song_low.plot()
song_mid.plot()
song_high.plot()

x_axis = rev_songs.columns
plt.plot(x_axis, song_low_with20Q,x_axis, song_mid_with20Q, x_axis, song_high)

plt.show()

#Accumulated data
# acc_master_df = rev_songs/rev_songs.sum()

# acc_mid = acc_master_df.iloc[median_mid]

# rev_songs_low = rev_songs.loc[acc_master_df<q30_acc]
# rev_songs_high = rev_songs.loc[acc_master_df>q90_acc]

#PLot 2 accomulated songs




