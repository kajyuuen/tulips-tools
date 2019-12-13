# Tulips tools

[klis Advent Calendar 2019](https://adventar.org/calendars/4206) 24日目のネタです。

## How to use

### Slack Botとして使う

![](https://user-images.githubusercontent.com/15792784/70805441-441df700-1dfc-11ea-8aaf-c5c55e516211.png)

```
python tulips-tools/slack-bot.py
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

