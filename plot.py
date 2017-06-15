import numpy as np
import matplotlib.pyplot as plt
n_groups = 2
val=20
means_pos = (10,30)
means_neg = (83.33,20)
means_neut = (6.67,50)
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.20

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, means_pos, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=0,
                 error_kw=error_config,
                 label='Positive')
rects2 = plt.bar(index + bar_width, means_neg, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=0,
                 error_kw=error_config,
                 label='Negative')
rects3 = plt.bar(index + bar_width+bar_width, means_neut, bar_width,
                 alpha=opacity,
                 color='g',
                 yerr=0,
                 error_kw=error_config,
                 label='Neutral')
plt.xlabel('Sentiment')
plt.ylabel('Percentage')
plt.title('Sentiment Analysis')
plt.xticks(index + bar_width / 1,('bjp','congress'))
plt.legend()

plt.tight_layout()
plt.show()

