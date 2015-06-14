Step1. pythonの開発環境の作り方をざっくりと
==============================================

python のインストール
-----------------------

### Mac

Macの場合はシステムpythonではなく、別途インストールしたほうが無難。brewで入れる。

```
brew install python
brew install python3
```

### Ubuntu14.04以上

* デフォルトでインストールされている system python が古くないので、それをベースにvirtualenvで環境を作れば問題ないので割愛

### Windows

以下からインストーラーを取得してインストール
https://www.python.org/downloads/


独立した python 環境をつくる
--------------------------------

* 言語限らず、どんな小さな開発でも開発するなら独立した環境を使ったほうがよい。(モジュールがごちゃごちゃになる)
* python の場合はそれを実現するツールとして virtualenv が主流で、python3.4からそれが公式化した pyvenv として提供され始めたよ
* virtualenv, pyvenvの動きをざっくり言うと、すでにインストールされているpythonをコピー&シンボリックリンクを駆使して、仮想的に全く独立した新たなpython環境をつくる。そのため高速で容量も食わない。
* pyenv っていう rbenv っぽいツールがあるけど、ツールとしては非公式でトラブるケースも多いのでどうしても細かいバージョンごとに手元でコンパイルしたい人でなければあまりおすすめしない。(@laughk主観)


(pip + ) virtualenv のインストール (python2.7のみ)
------------------------------------------------

## Mac/Linux系

#### python が 2.7.8以下のバージョンの場合

pip が含まれていないのでインストールする。  
(system python に pip を追加する場合は sudo も忘れずに )

```
curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

#### virtualenv のインストール

```
## Mac (from brew)
pip install virtualenv

## それ以外
sudo pip install virtualenv

## 確認
which virtualenv
```

## Windows

2015-06-15 の時点で新規にインストールする場合は pip がデフォルトで同封されているので以下を実行すればOK

```
> C:\Python27\Script\pip install virtualenv
> dir C:\Python27\Script\virtualenv.exe
```

新規に何か開発するときの流れ
---------------------------------

ここまでできていればpythonで開発する最低限の環境の準備はOK
具体的には以下のような流れになる。

#### 適宜作業ディレクトリを作成する

```console
$ mkdir /path/to/workspace/my-apps
```

#### 開発するツール用に仮想python環境を作成

##### 2.7.x ( 〜 3.3.x )

`-p` オプションでベースとなるpythonのパスを指定する。  
また、仮想環境名は任意でよいが最近は `venv` とするケースが多い。

```console
$ cd /path/to/workspace/my-apps
$ virtualenv -p /path/to/base/python venv
$ ls -l venv
```

##### 3.4.x

pyvenv は 3.4 系以降なので、現状は特にベースにするpythonの意識はしなくてもOK

```
$ cd /path/to/workspace/my-apps
$ pyvenv venv
$ ls -l venv
```

#### 仮想python環境を有効にする

pythonを実行する際に `venv` 配下に作成された仮想環境のpythonを利用するようにする。

##### Mac/Linux

```
$ soure venv/bin/activate
(venv) $
```

##### Windows

```
C:\Users\laughk> venv/Scripts/activate.bat
(venv) C:\Users\laughk>
```


# python環境の準備は以上。
