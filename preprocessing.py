
def replace_yn(df):
    df = df.replace(to_replace='Yes', value=1)
    df = df.replace(to_replace='No', value=0)
    return df
