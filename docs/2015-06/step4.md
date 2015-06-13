Step4. 自作したコマンドラインをpipでインストールして使えるようにする
--------------------------------------------------------------

せっかくコマンドラインツールが作れたのならば

```console
$ /path/to/workspace/hogehoge.py
```

のような感じではなく

```console
$ myutils
-- -- snip -- --
$ which myutils
/usr/local/bin/myutils
```

のような形で使いたいだろうし、

```console
$ pip install myutils
```

みたいにインストールができるのであればもっと便利なはず。
そのために必要になるパッケージ作成作業に必要な `setup.py` を作成し、githubで公開するところまでやってみる。  
(あくまで最低限の書き方を紹介。)


パッケージ作成
----------------

パッケージ作成の際にキモになるのが `setup.py` ファイルの作成。  
これを作成しパッケージとするファイル群のトップディレクトリ設置することで、

* モジュールとしてインストール
* tar玉やgit経由で配布
* PyPIへのアップロードが可能になる。

ができる。

### setup.py を置くとできるようになること

#### モジュールインストール

ローカルにすでにソースはある場合は以下でインストール可能

```console
$ python setup.py install
```

また、pipで以下のようにするのもあり

```console
$ pip install .
```

開発中の場合は、pipで `-e` オプションをつけてインストールすると  
ソースを直接編集するとすぐさま反映されるのでデバッグをする際にも便利


#### git経由でインストール

例えばgithubで公開してあるのであれば、以下の用にしてインストールすることができる

```console
$ pip install git+https://github.com/laughk/kite-string.git
```

### setup.py の例

#### 最小限な書き方

一番シンプルな書き方は以下

```python
from setuptools import setup, find_packages

setup(
    name="Package Name",
    packages=find_packages()
)
```

* `find_packages()` は setup.py 配下のパッケージをいい感じに見つけてくれる関数


#### コマンドラインツール作成の場合 

* `entry_points` : ここでインストールされるコマンド名とそれに紐づくメソッドを関連付ける。
* `install_requires` : 他のpypiパッケージに依存する場合はここに記載するとinstallの際に同時にインストールされる。

```python
from setuptools import setup, find_packages

setup(
    name="Package Name",
    packages=find_packages()
    entry_points='''
        [console_scripts]
        myutils=cli:main
    ''',
    install_requires=[
        'Click',
    ],
)
```
