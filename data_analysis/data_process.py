import pandas as pd
import numpy as np

def gen_exp_weight(length, rate):
    weight = [1*rate**i for i in range(length)]
    return weight


def weighted_moving_average_imputation(df, column_name, weights):
    # データフレームのコピーを作成（オリジナルデータを変更しないため）
    df_copy = df.copy()

    # weights の長さ
    window = len(weights)

    # weights の合計（正規化のため）
    weights_sum = sum(weights)

    # 欠損値のインデックスを取得
    nan_indices = df_copy[df_copy[column_name].isna()].index

    for idx in nan_indices:
        # idx より前のデータを取得
        past_data = df_copy.loc[:idx].iloc[-window-1:-1][column_name]

        # 過去のwindowが全てNaNであればスキップ
        if len(past_data) == past_data.isna().sum():
            continue

        # 取得したwindow幅が足りなかった場合(補完する日より前に、データが十分に無い時)
        if len(past_data) < window:
            sub_window = len(past_data)

            # 過去のwindowに一部NaNがあれば、そこを除いて加重平均を計算する
            # 例えば、weight = [0.1, 0.2, 0.3, 0.4], past_data = [NaN, NaN, 1, 2]の時
            # 加重平均 = (0.3*1 + 0.4*2) / (0.3 + 0.4) = 1.57...
            sub_weights_sum = np.dot((~past_data.isna()).astype(int), weights[-sub_window:]).sum()

            # 加重平均を計算
            past_data = past_data.fillna(0)
            weighted_avg = np.dot(past_data.values, weights[-sub_window:]) / sub_weights_sum

            # 欠損値を加重平均で埋める
            df_copy.at[idx, column_name] = weighted_avg

        # 取得できたwindow幅がweightの幅と同じであった場合
        else:
            # 過去のwindowに一部NaNがあれば、そこを除いて加重平均を計算する
            # 例えば、weight = [0.1, 0.2, 0.3, 0.4], past_data = [NaN, NaN, 1, 2]の時
            # 加重平均 = (0.3*1 + 0.4*2) / (0.3 + 0.4) = 1.57...
            weights_sum = np.dot((~past_data.isna()).astype(int), weights).sum()

            # 加重平均を計算
            past_data = past_data.fillna(0)
            weighted_avg = np.dot(past_data.values, weights) / weights_sum

            # 欠損値を加重平均で埋める
            df_copy.at[idx, column_name] = weighted_avg

    return df_copy

# 使用例
weight = gen_exp_weight(3, 2)
print(weight)


# 使用例
df = pd.DataFrame({
    'test': [np.nan, np.nan, np.nan, np.nan, 1.0, 2.0, np.nan, 4.0, 5.0, np.nan, 7.0],
    'date': pd.date_range(start='2021-01-01', periods=11)
})
df.set_index('date', inplace=True)

weights = [0.1, 0.2, 0.3, 0.4]  # 合計が1である必要はない
result_df = weighted_moving_average_imputation(df, 'test', weights)
print(result_df)

