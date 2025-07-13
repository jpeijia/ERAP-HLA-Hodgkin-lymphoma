import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

filepath = 'H://Peijia//graph//c2 ERAP//journal for ERAP paper.xlsx'
file = pd.read_excel(filepath, sheet_name='Sheet4')
print(file.head())
#print(file.dtypes)
#print(file.describe(include='all'))

#data_with_EBV = file.dropna(subset=['EBV'], axis=0)
#print(data_with_EBV.head())
#EBV_sex = data_with_EBV[['sex','EBV', 'Age at diagnosis', 'KIR_Haplotype', 'subtype']]
#print(EBV_sex.head())

ax = sns.countplot(x='journal for ERAP-SNP', hue='OA discount', data=file)
ax.tick_params(labelrotation=90)
ax.yaxis.set_ticks(np.arange(0,10.1,1))
ax.set_xlabel('')
ax.set_title('Journals published ERAP-SNP paper since 2010 (impact factor)')
plt.show()

