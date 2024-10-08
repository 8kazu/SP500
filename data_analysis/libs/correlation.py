import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import os

USER_ID = os.environ.get('USER_ID')
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 109)

def calc_correlation(df: pd.DataFrame):
    df = df.astype('float64')
    df_corr = df.corr()
    return df_corr

def plot_correlation(df_corr: pd.DataFrame, filename: str) -> None:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df_corr.iloc[1:, 1:], annot=False, fmt='.2f', cmap='coolwarm', square=True, vmax=1, vmin=-1, center=0, xticklabels=df_corr.columns, yticklabels=df_corr.columns)
    plt.title(f'Correlation Matrix Heatmap of {filename}')
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.savefig(f'/home/{USER_ID}/mizuho24s/images/heatmap_{filename}.png')