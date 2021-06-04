---
# template tags (but you can change these)

layout: post
category: article


# tags user defined

tags: uncategorized
lang: ja_JP
author: 3y
title: Pythonことはじめ
date: 2021-06-04 10:36:16 +0900
last-update: 2021-06-04 14:29:44 +0900
---

はじめまして、3yです。
この記事ではPython超入門として一番単純なPythonの命令を説明していきたいと思います。

## Hello, world!

まずはコンソール上にHello, world!と表示するプログラムを作りましょう。

{% highlight py %}
print("Hello, world!")
# => Hello, world!
{% endhighlight %}

`print()`は()内の引数をコンソール上に表示する関数です。
上の例では文字列"Hello, world!"をコンソール上に表示しています。

{% highlight py %}
number = 123

print(number)
# => 123
{% endhighlight %}

`変数名 = 〇〇`で変数に代入できます。
上の例では 整数値 123 を 変数 number に代入しています。
`print(変数名)`とすることで、変数の中身を表示することができます。
プログラムが期待通りに動かなかったり、エラーを吐くときはとにかく`print()`を使って変数の中身を把握する癖を付けましょう。

## まとめ

・プログラムが動かなかったらとにかく`print()`で変数の状態を把握しましょう