import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#hapQTL_filepath = '/home/peijia/course/seaborn/ERAP1_haplotype_QTL.xlsx'
hapQTL_filepath = 'H:\\Peijia\\graph\\ERAP_HLA\\ERAP1_haplotype_QTL.xlsx'
#hapQTL_filepath = 'D:\\Peijia\\graph\\ERAP_HLA\\ERAP1_haplotype_QTL_total.xlsx'
hapQTL_data = pd.read_excel(hapQTL_filepath)
print(hapQTL_data.head())

hapcomb=hapQTL_data['hap_comb']
hapcount={}
hapcombmorethan5=[]

for a in hapcomb:
    hapcount.setdefault(a,0)
    hapcount[a] = hapcount[a] +1
print(hapcount)

hapcount1=list(hapcount.keys())

for b in hapcount1:
    if hapcount[b]>4:
        hapcombmorethan5.append(b)
print(hapcombmorethan5)                         

fig, ax = plt.subplots(figsize=(12,6))

#    sns.violinplot(x='hap_comb1', y='ERAP1', data=hapQTL_data,
#                   order=['3+4','4+4','2+3','2+2','2+4','1+4','1+3','2+5','1+6','1+2','1+1','1+5'])
#sns.swarmplot(x='hap_comb1', y='ERAP1', data=hapQTL_data,
#                  order=['3+4','4+4','2+3','2+2','2+4','1+4','1+3','2+5','1+6','1+2','1+1','1+5'])
sns.boxplot(x='hap_comb1', y='ERAP1', data=hapQTL_data, showfliers=False,boxprops={'facecolor': 'None'},
                order=['3+4','4+4','2+3','2+2','2+4','1+4','1+3','2+5','1+6','1+2','1+1','1+5'])
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
y_pos = np.arange(1,11)

plt.ylim(0,15)
plt.xlabel('ERAP1 haplotype combinations',fontsize=26)
plt.ylabel('ERAP1', fontsize=26)
plt.plot([0,0,10,10],[12.5,13,13,12.5], c='k')
plt.text(5,13,'***', size=26, ha= 'center')
plt.plot([9,9,11,11],[12,12.5,12.5,12], c='k')
plt.tick_params(labelsize=20)             # labelsize

plt.plot([1,1,10.5,10.5],[11,11.5,11.5,11], c='k')
plt.text((1+10.5)*0.5,11.5,'**', size=26, ha= 'center')
plt.plot([10,10,11,11],[10.5,11,11,10.5], c='k')
plt.subplots_adjust(left=0.07, bottom=0.14, right=0.99, top=0.69)

plt.show()
