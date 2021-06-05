---
layout: post
title:  "マークダウンの書き方"
date:   2021-05-30 04:51:00 +0900
last-update: 2021-06-05 00:51:51 +0900
category: article
tags: guide
lang: ja_JP
author: 3y
---
マークダウンの書き方サンプル

## 見出しサイズ

# \# h1 見出し

## \#\# h2 見出し

### #\#\# h3 見出し

#### \#\#\#\# h4 見出し

##### \#\#\#\#\# h5 見出し

###### \#\#\#\#\#\# h6 見出し


## テキスト

#### 原文

{% highlight html linenos %}
{% raw %}
見出し以外のテキストは改行しても連続します。
改行するには、空白の行を挟むか、\<br\>タグを使用します。

空白行を挟むと\<p\>タグが分割されます。

\<br\>タグはHTMLでは改行を意味します。<br>
また、バックスラッシュを使うことでタグや強調構文のエスケープができます。
{% endhighlight %}
{% endraw %}

#### 整形後

見出し以外のテキストは改行しても連続します。
改行するには、空白の行を挟むか、\<br\>タグを使用します。

空白行を挟むと\<p\>タグが分割されます。

\<br\>タグはHTMLでは改行を意味します。<br>
また、バックスラッシュを使うことでタグや強調構文のエスケープができます。


## ハイパーリンク


#### 原文

{% raw %}
[リンク][hiuctf-home]を表示 [リンク](https://hiuctf.club)を表示
{% endraw %}

#### 整形後

[QiitaのMarkdown記法の参考ページ](https://qiita.com/Qiita/items/c686397e4a0f4f11683d)を表示
[LiquidのMarkdown記法の参考ページ](https://qiita.com/mt_west/items/7a4f41c749ed582330e9)を表示

シンタックスハイライトの[対応言語][jekyll-support-languages]と[オプション][jekyll-linenos]


## コードのハイライト

#### 原文

{% highlight md %}
{% raw %}
`myfunction()`の引数に`res_string.__dict__`を代入してみましょう。

{% highlight py %}
def nothing_to_do():
  pass # nothing happens
{% endhighlight %}
{% endraw %}
{% endhighlight %}

#### 整形後

`myfunction()`の引数に`res_string.__dict__`を代入してみましょう。

{% highlight py %}
def nothing_to_do():
  pass # nothing happens
{% endhighlight %}


## ページ・サイト変数読み込み


#### 原文

{% highlight md %}
{% raw %}
サイトのタイトル({{ site.title }})を表示したり、サイトの[URL]({{ site.url }})を表示したり、ページのタイトル({{ page.title }})を表示したりできます。
{% endraw %}
{% endhighlight %}

#### 整形後

サイトのタイトル({{ site.title }})を表示したり、サイトの[URL]({{ site.url }})を表示したり、ページのタイトル({{ page.title }})を表示したりできます。


## 画像挿入


#### 原文

{% highlight md %}
{% raw %}
![aaaa777 avatar](https://user-images.githubusercontent.com/27488794/120819563-ab021380-c58e-11eb-94f6-a0ea6dfeee76.jpg)
{% raw %}
{% endhighlight %}

#### 整形後

![aaaa777 avatar](https://user-images.githubusercontent.com/27488794/120819563-ab021380-c58e-11eb-94f6-a0ea6dfeee76.jpg)


## 文字装飾


#### 原文

{% highlight md %}
{% raw %}
例えば\*\*太字にしたり\*\*、\~\~取り消し線を引いたり\~\~、\*斜体にしたり\*、\~\~\*\*\*全部合わせたり\*\*\*\~\~、できます。
{% raw %}
{% endhighlight %}

#### 整形後

例えば**太字にしたり**、~~取り消し線を引いたり~~、*斜体にしたり*、~~***全部合わせたり***~~、できます。


Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

Jekyllが使用しているマークダウンHTML変換ライブラリ[Lquid][liquid-home]の[記法ドキュメント][liquid-syntax]。

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
[jekyll-support-languages]: https://github.com/rouge-ruby/rouge/wiki/List-of-supported-languages-and-lexers
[jekyll-linenos]: https://jekyllrb.com/docs/liquid/tags/#line-numbers
[hiuctf-home]: https://hiuctf.club
[liquid-syntax]: https://github.com/Shopify/liquid/wiki/Liquid-for-Designers
[liquid-doc]: https://github.com/Shopify/liquid/wiki
[liquid-home]: https://shopify.github.io/liquid/