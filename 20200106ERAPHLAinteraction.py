import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#eQTL_filepath = '/home/peijia/course/seaborn/eQTL_in_LCL.xlsx'
bestGuessGeno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='best guess N=390 (HLA geno)')
bestGuessPheno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='best guess N=390 (HLA pheno)')
bestGuessWithCutoffGeno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='with cutoffs N=390 (HLA geno)')
bestGuessWithCutoffPheno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='with cutoffs N=390 (HLA pheno)')
realHLAtypeGeno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='real HLA type N=365 (HLA geno)')
realHLAtypePheno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='real HLA type N=365 (HLA pheno)')
realGenotypeGeno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='real genotype N=285 (HLA geno)')
realGenotypePheno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='real genotype N=285 (HLA pheno)')

ERAPhapGeno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='ERAP haplotype (HLA geno)')
ERAPhapPheno = pd.read_excel('H:\\Peijia\\graph\\presentation\\20191223ERAPHLAinteraction20190927.xlsx',sheet_name='ERAP haplotype (HLA pheno)')


ls = [bestGuessGeno, bestGuessPheno, bestGuessWithCutoffGeno, bestGuessWithCutoffPheno, realHLAtypeGeno, realHLAtypePheno, realGenotypeGeno, realGenotypePheno,
      ERAPhapGeno, ERAPhapPheno]
title = ['Best guess N=390 (HLA geno)', 'Best guess N=390 (HLA pheno)', 'With cutoffs N=390 (HLA geno)', 'ERAP SNP and HLA association',
         'Real HLA type N=365 (HLA geno)', 'Real HLA type N=365 (HLA pheno)', 'Real genotype N=285 (HLA geno)', 'Real genotype N=285 (HLA pheno)',
         'ERAP haplotype (HLA geno)', 'ERAP1 haplotype and HLA association']

#xlab=['ERAP SNPs', 'ERAP1 haplotypes']
#titles= ['ERAP SNP', 'ERAP1 haplotypes']

for i in range(len(ls)):
    xorder = list(ls[i]['ERAP'].unique())
    if i<8:
        xorder = ['rs72773968', 'rs26653', 'rs26618', 'rs27895', 'rs2287987', 'rs30187', 'rs10050860', 'rs27044', 'rs27038', 'rs13160562', 'rs27524', 'rs2549782']
        #sns.swarmplot(x='ERAP', y='-log10',data=ls[i], ax=ax[i], order=xorder[i],size=6) # Better way to make a good order for x-axis?
        fig, ax = plt.subplots(figsize=(15,8))
        ax = sns.swarmplot(x='ERAP', y='-log10',data=ls[i], order=xorder, color='black', size=6)
        ax.set_title(title[i], fontsize=22)
        ax.set_ylim(0,4)
        ax.plot([-1,12],[2.3,2.3],c='k',linestyle='dashed')
    #    ax[i].text(txtposition[i],3.7+i/5,'with correction',ha='center', fontsize=16)
        ax.text(5.5,2.4,'p=0.005',ha='center', fontsize=16)
        ax.set_xlabel('ERAP SNP',fontsize=18)#,labelpad=5) # labelpad= space between xlabel and x-axis
    # for subscript printing, we can use unicode's subscripts. (e.g H₂) Namely the subscripts are in the ranges: 0x208N for numbers, +, -, =, (, )
    # (N goes from 0 to F), 0x209N for letters. For example: In [6]: print(u'H\u2082O\u2082') -->  H₂O₂    

        ax.set_ylabel(u'P value (-Log\u2081\u2080)',fontsize=18)
        ax.yaxis.set_ticks(np.arange(0,4,0.5))
        ax.tick_params(labelsize=14)
        plt.subplots_adjust(left=0.06, bottom=0.13, right=0.99, top=0.5)

    else:
        xorder = ['hap3', 'hap4', 'hap7', 'hap2', 'hap6', 'hap5', 'hap1']
        fig, ax = plt.subplots(figsize=(15,8))
        ax = sns.swarmplot(x='ERAP', y='-log10',data=ls[i], order=xorder, color='black', size=6)
        ax.set_title(title[i], fontsize=22)
        ax.set_ylim(0,4)
        ax.plot([-1,12],[2.3,2.3],c='k',linestyle='dashed')
    #    ax[i].text(txtposition[i],3.7+i/5,'with correction',ha='center', fontsize=16)
        ax.text(3,2.4,'p=0.005',ha='center', fontsize=16)
        ax.set_xlabel('ERAP haplotype',fontsize=18)#,labelpad=5) # labelpad= space between xlabel and x-axis
    # for subscript printing, we can use unicode's subscripts. (e.g H₂) Namely the subscripts are in the ranges: 0x208N for numbers, +, -, =, (, )
    # (N goes from 0 to F), 0x209N for letters. For example: In [6]: print(u'H\u2082O\u2082') -->  H₂O₂    

        ax.set_ylabel(u'P value (-Log\u2081\u2080)',fontsize=18)
        ax.yaxis.set_ticks(np.arange(0,4,0.5))
        ax.tick_params(labelsize=14)
        plt.subplots_adjust(left=0.06, bottom=0.13, right=0.99, top=0.5)

#plt.tight_layout()
plt.show()
