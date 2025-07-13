import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#eQTL_filepath = '/home/peijia/course/seaborn/eQTL_in_LCL.xlsx'
SNP_HLA = pd.read_excel('H:\\Peijia\\graph\\presentation\\2019_3_22_ERAPSNP_HLAinteraction.xlsx',sheet_name='SNP_HLA_interaction')
hap_HLA = pd.read_excel('H:\\Peijia\\graph\\presentation\\2019_3_22_ERAPSNP_HLAinteraction.xlsx',sheet_name='hap_HLA_interaction')
print(hap_HLA.head())
ls=[SNP_HLA, hap_HLA]
xlab=['ERAP SNPs', 'ERAP1 haplotypes']
titles= ['ERAP SNP', 'ERAP1 haplotypes']
txtposition=[2.5, 4]
xorder=[['rs30187', 'rs2042381','rs27524','rs28129','rs26618', 'rs2549782'],['hap3', 'hap4', 'hap7','hap12','hap8','hap2','hap6','hap5','hap1']]
fig, ax = plt.subplots(nrows=1, ncols=2)

for i in range(2):
    sns.swarmplot(x='ERAP', y='-log10',data=ls[i], ax=ax[i], order=xorder[i],size=6) # Better way to make a good order for x-axis?
    ax[i].set_ylim(0,5)
#    ax[i].plot([-1,10],[3.6+i/5,3.6+i/5],c='k')
    ax[i].plot([-1,10],[2.3,2.3],c='k',linestyle='dashed')
#    ax[i].text(txtposition[i],3.7+i/5,'with correction',ha='center', fontsize=16)
    ax[i].text(txtposition[i],2.4,'p=0.005',ha='center', fontsize=16)
    ax[i].set_xlabel(xlab[i],fontsize=18,labelpad=40) # labelpad= space between xlabel and x-axis
    ax[i].set_ylabel('p value (-log10)',fontsize=18)
    ax[i].tick_params(labelsize=12)
    ax[i].set_title(titles[i],fontsize=18)
    ax[i].set_xlabel('')
    
plt.tight_layout()
plt.show()
