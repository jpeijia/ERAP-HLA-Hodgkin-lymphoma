import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss

#eQTL_filepath = '/home/peijia/course/seaborn/eQTL_in_LCL.xlsx'
eQTL_filepath = 'D:\\Peijia\\graph\\ERAP_HLA\\eQTL_in_LCL.xlsx'
eQTL_data = pd.read_excel(eQTL_filepath)
print(eQTL_data.head())

def SNP_eQTL_anova(SNP_col,gene_col):
    SNPcount={}
    for genotype in SNP_col:
        SNPcount.setdefault(genotype,0)
        SNPcount[genotype] = SNPcount[genotype]+ 1
    print(SNPcount)
    SNPgeno = list(SNPcount.keys())
    group1,group2,group3 = [],[],[]
    for num in range(len(SNP_col)):                
        if SNP_col[num] == SNPgeno[0]:
            group1.append(gene_col[num])
        elif SNP_col[num] == SNPgeno[1]:
            group2.append(gene_col[num])
        else:
            group3.append(gene_col[num])
    print(len(group1),len(group2),len(group3))
    anova = ss.f_oneway(group1, group2, group3)
    return anova

def anova_annotation(p,x,y):
#        if p<0.0001:
#            ax[i][j].text(x,y,'****', ha='center')
        if p<0.001:
           ax[i][j].text(x,y,'***', ha='center')
        elif p<0.01:
            ax[i][j].text(x,y,'**', ha='center')
        elif p <0.05:
            ax[i][j].text(x,y,'*', ha='center')
        else:
            ax[i][j].text(x,y+y/40,'ns', ha='center')

fig, ax = plt.subplots(nrows=3, ncols=6, figsize=(11,6))

#SNP = ['rs27524','rs13160562','rs27038','rs27044','rs10050860','rs30187']
SNP1 = ['rs2287987','rs27895','rs26618','rs26653','rs72773968','rs2549782']
ERAP = ['ERAP1','ERAP2','ERAP2']
boxprops = dict(linewidth=0, color='k')
for i in range(len(ERAP)):
    for j in range(len(SNP1)):
#        sns.swarmplot(x=SNP1[j], y=ERAP[i], data=eQTL_data, ax=ax[i][j],size=2)
        sns.boxplot(x=SNP1[j], y=ERAP[i], data=eQTL_data, ax=ax[i][j], showfliers=False, boxprops={'facecolor': 'None'})
        ax[i][j].spines['right'].set_visible(False)
        ax[i][j].spines['top'].set_visible(False)
        ax[i][j].xaxis.set_ticks_position('bottom')
        ax[i][j].yaxis.set_ticks_position('left')
        
#           sns.boxplot(x=SNP1[j], y=ERAP[i], data=eQTL_data, ax=ax[i][j], showfliers=False,
#                       showcaps=False, whiskerprops={'linewidth': 0}, boxprops=dict(alpha=0))  # only show median
        ax[i][j].set_ylim(0,13)

#        if i<2:
#            ax[i][j].set_xlabel('')

        ax[i][j].set_xlabel('')
        
        if j>0:
            ax[i][j].set_ylabel('')
            ax[i][j].set_yticklabels([])

        if i==0:
            ax[i][j].set_title(SNP1[j])
              

        if SNP1[j] != 'rs27895':
            ax[i][j].plot([0,2], [11,11], c='k')

            f, p = SNP_eQTL_anova(eQTL_data[SNP1[j]], eQTL_data[ERAP[i]])
            anova_annotation(p,1,11)
            print(SNP1[j],f, p)

plt.tight_layout()
plt.show()
