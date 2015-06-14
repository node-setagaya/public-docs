標準モジュールでコマンドラインツールを作ってみる
===================================================

python2.7以降でコマンドラインツールを作るとき、  
標準のモジュールで行う場合は argparse というモジュールを使います。

documentはこちら http://docs.python.jp/2/library/argparse.html


argparse を簡単に触ってみる
-------------------------------

該当サンプル

* [pure-prog1.py](sample/pure-prog1.py)
* [pure-prog2.py](sample/pure-prog2.py)

### argparse の使い方

argparse を import して parser インスタンスを定義

```python
import argparse 

parser = argparse.ArgumentParser(description='Process some integers.')
```

### オプションの定義

サンプルコード `sample/pure-prog1.py` より。

```python
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
```

### パラメタの受け取り方

サンプルコード `sample/pure-prog1.py` より。

```python
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
```

### サブコマンドを作ってみる

サンプルコード `sample/pure-prog2.py` より。

```python
    '''
    subパーサーを作成
    '''
    subparsers = parser.add_subparsers()
    sum_parser = subparsers.add_parser('sum')


    '''
    作成したsubパーサーにパラメタとデフォルト処理をする関数を指定する
    '''
    sum_parser.add_argument('integer', metavar='N', type=int, nargs='+', 
            help='an integer for the accumulator'
            )
    sum_parser.set_defaults(func=sum_command)
```

# 標準モジュールでのコマンドラインツールの作成の流れは異常
