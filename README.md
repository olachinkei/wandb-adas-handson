# Basic WandB Handson
こちらのハンズオンコードは、[こちら](https://www.wandb.courses/courses/effective-mlops-model-development-jp)のコースを短縮したものになっています。
Experiment tracking, Artifacts, Tables, Sweepsの基礎をみていきます。
詳細はハンズオンの中で解説しますが、以下事前の動作確認をお願いします。

## preparation
pyenv, conda, Dockerなどを用いて環境構築を行ってください。以下は例です。
```
pip install -r requirements.txt
```
API keyを設定してください。API keyはUser Settingsにあります。
```
export WANDB_API_KEY=""
```

Dedicated cloudやVPC、on-premをお使いの方は、環境変数を以下のように設定して下さい。subdomainにあたる"XXX"は、担当者に確認をしてください。
Multinant cloud(SaaS)をご利用の場合は、必要ありません。
```
export WANDB_BASE_URL="https://XXX.wandb.io"
```


## Execution
### param.pyのupdate
WANDB_ENTITY = "" をupdateしてください。
はじめての方は、User settingsの元のdefaultのentity nameを入力してください。
なお、WANDB_ENTITYは上記のようにパラメータとして設定していますが、環境変数として設定することも可能です。

### Data preparation & Visualization & Base model creation
`0_ADAS_handson_basic.ipynb`を最後まで実行し、表示されるwandbのURLをご確認ください。

### Sweepの実行
`sweep.yaml`の`entity`を上記と同じ値に変更してください。その後、以下のコードを実行してください。
```
wandb sweep config.yaml
```
その後表示されるsweep_idを用いて、以下のコードを実行してください。
```
wandb agent sweep_id
```