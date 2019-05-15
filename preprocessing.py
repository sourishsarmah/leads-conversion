import numpy as np

def replace(df):
    # Replace Select with NaN
    df = df.replace(to_replace='Select', value=np.nan)

    # Merge Similar Labels
    df['Lead Source'] = df['Lead Source'].replace('google', 'Google')
    df['Lead Source'] = df['Lead Source'].replace(['blog', 'WeLearn', 'welearnblog_Home'], 'Blog')
    df['Country'] = df['Country'].replace(['unknown'], np.nan)

    return df
