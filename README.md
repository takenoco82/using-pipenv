# using-pipenv
## 概要
- pipenvの使い方を試す

## 使い方
``` sh
# アプリの実行（Docker）
make start
curl http://localhost:8080/v1/fizzbuzz/15

# 静的解析・テストの実行（Docker）
make test
```

## テストの small・medium について
- [結合テストと呼ぶのをやめた話 - asterisc](http://akito0107.hatenablog.com/entry/2018/08/27/190333)
- [Attrib: tag and select tests with attributes — nose 1.3.7 documentation](https://nose.readthedocs.io/en/latest/plugins/attrib.html)

## 参考
- [Python開発環境の構築](https://gist.github.com/takenoco82/22de2e7088304d7c6eb74535d6afbae8)
