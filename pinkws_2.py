#import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read data 

tot_master_df = pd.read_excel('Song_rev_no_name.xlsx', header=1)

#NR 1: Slice data set
#Get all songs that have more than 10 quarters 

#Get all songs per quarter
rev_songs = tot_master_df.iloc[:,1:20]
#Get all songs tot revenue
tot_rev= tot_master_df.iloc[:,21]
#Get all songs that have more than 10 quarters 
songs_above_10Q = tot_master_df.iloc[:,22][tot_master_df.iloc[:,22]>10]

#NR 2: Calculate mean median and max revenue

mean_tot_rev = tot_rev.mean()
median_tot_rev = tot_rev.median()
max_tot_rev = tot_rev.max()

print 'max:', max_tot_rev
print 'mean:', mean_tot_rev
print 'median:', median_tot_rev
#NR 3: Plot a histogram of total revenue  

tot_rev_hist = tot_rev.hist()
plt.title('Histogram of total revenue')
plt.show()

#NR 4: Calculate Quantile

Quantile = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
q_all = tot_rev.quantile(Quantile)

print 'quantiles:', q_all


#Nr 5 Plot the 5 best selling songs
q99 = tot_rev.quantile(0.99)
tot_rev_99 = tot_rev[tot_rev>q99]
rev_songs_high = rev_songs.loc[tot_rev_99.index]

x_axis = rev_songs.columns
plt.plot(x_axis, rev_songs_high.transpose())
plt.title('Songs from the 99 % quantile, songs with highest revenue')
plt.show()

#NR 6 Plot the accumulated song
hit_acc = rev_songs_high.transpose().cumsum()/rev_songs_high.transpose().sum()

plt.plot(x_axis, hit_acc)
plt.title('Revenue distributed from quarter 1 to quarter 20')

plt.show()

#NR 7 Plot one hit and one average swedish song
pop_hit = rev_songs.loc[23778758]
pop_soul = rev_songs.loc[19751504]

plt.bar(x_axis, pop_hit, color="blue")
plt.bar(x_axis, pop_soul,color="red")
plt.title('Blue: Hit, Red: average swedish song')

plt.show()

pop_hit_cum = pop_hit.cumsum()/pop_hit.sum()
pop_soul_cum = pop_soul.cumsum()/pop_soul.sum()

plt.plot(x_axis, pop_hit_cum,x_axis, pop_soul_cum)
plt.title('Revenue distributed from quarter 1 to 20')

plt.show()


