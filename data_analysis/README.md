# mizuho24s

## データについて
- `/home/u00232/dss/share24S/mizuho/work/processed_data`の中に提供データというディレクトリがあるので、この中のデータをいじりましょう。その上で、このフォルダをシンボリックリンクで自分のホームディレクトリに持ってきていただきたいです。
- `ln -s /home/u00232/dss/share24S/mizuho/work/processed_data mizuho_data`をを自分のホームディレクトリ(`/home/(ユーザー名)`)で実行すると、自分のホームからはmizuho_dataというディレクトリの中に`/home/u00232/dss/share24S/mizuho/work/processed_data`のデータがあるように見えます。

## vscodeでのconda環境への接続
1. istクラスタにssh接続する
2. 以下を実行
```
echo '
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/u00232/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/u00232/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/u00232/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/u00232/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
' >> ~/.bashrc
``` 
3. `source ~/.bashrc` 
3. `conda activate /home/u00232/anaconda3` を実行
4. `ipython kernel install --user --name=shared_anaconda --display-name=shared_anaconda`を実行
5. vscodeでipynbファイルを開き、"kernelを選択" > "別のカーネルを選択..." > "Python 環境..." から パスが `/home/u00232/anaconda3` と表示されているものを選ぶ
6. 5ができない時はvscodeの拡張機能を確認
