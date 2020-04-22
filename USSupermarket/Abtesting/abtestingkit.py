import pandas as pd
from scipy.stats import norm
from scipy.stats import ttest_ind


def abtesting(df,group,target,diff=0,alt='equal'):
    df_stats = df[[group, target]].groupby(group) \
                 .agg(['count','mean','var','std']).reset_index()

    # Sample Sizes
    n1 = df_stats[target]['count'][0]
    n2 = df_stats[target]['count'][1]

    # Sample means
    y1 = df_stats[target]['mean'][0]
    y2 = df_stats[target]['mean'][1]

    # Pooled variance and standard deviation
    sigma_2 = (n1*df_stats[target]['var'][0] + n2*df_stats[target]['var'][1]) \
               / (n1+n2)

    sigma = sigma_2**0.5

    # Sample mean difference
    delta = y1 - y2

    # Power (Probability not having Type II error)
    k = n2*1.0/n1
    power = norm.cdf(1.96-(delta/(sigma_2/n1+sigma_2/n2)**0.5))

    # Sample size needed to achieve 0.8 power
    n2_needed = (((k**-1+1)*(1.96-0.84)**2)*sigma_2)/delta**2
    n2_needed = int(round(n2_needed))
    n1_needed = int(round(k*n2_needed))

    # Find p-values for ab testing
    # alt is H0. If alt='equal', H0 is equal; if alt='less than', H0 is less
    pval = -1
    if alt=='equal':
        pval = ttest_ind(df[df[group]==df_stats[group][0]][target].tolist(),
                         df[df[group]==df_stats[group][1]][target].tolist())[1]

    elif alt=='less than':
        pval = 1-ttest_ind(df[df[group]==df_stats[group][0]][target].tolist(),
                           df[df[group]==df_stats[group][1]][target] \
                              .tolist())[1]/2

    elif alt=='greater than':
        pval = ttest_ind(df[df[group]==df_stats[group][0]][target].tolist(),
                         df[df[group]==df_stats[group][1]][target]
                            .tolist())[1]/2

    result = {'pval':pval, 'power':power, 'size_needed': (n1_needed, n2_needed)}

    return result

# Function to save results
def savefile(results, filepath):
    f = open(filepath,'w')
    f.write('-----Result-----\n')
    f.write('P-value: ')
    f.write(str(round(results['pval'], 4)))
    f.write('\n')
    f.write('Power: ')
    f.write(str(round(results['power'], 4)))
    if results['power'] < 0.80:
        f.write('\n')
        f.write('Sample Size needed to achieve 80%: ')
        f.write(str(results['size_needed'][0]))
        f.write(' ')
        f.write(str(results['size_needed'][1]))
    f.close()
