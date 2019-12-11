# Tulips tools

## How to use

## Install

```
pip install tulips
```

### CLIとして使う

ユーザ名とパスワードの保存。この操作を行うと以下のコマンドでユーザとパスワードを入力する必要がなくなります。

```
python tulips-tools/cli.py config set -u <ユーザ名> -p <パスワード>
```

図書館から借りている資料の一覧

```
python tulips-tools/cli.py view borrow -u <ユーザ名> -p <パスワード>
```

借りた資料の履歴

```
python tulips-tools/cli.py view history -u <ユーザ名> -p <パスワード>
```


### APIラッパーとして使う

詳しくはtulips.pyを見て下さい。

```
import Tulips

tulips = Tulips(os.environ["LIB_USER"], os.environ["LIB_PASSWD"])
tulips.login() # ログイン
```

### Contributing

Tulips toolsに関するバグレポートやリクエストは、Issueの作成による報告をお願いします。

