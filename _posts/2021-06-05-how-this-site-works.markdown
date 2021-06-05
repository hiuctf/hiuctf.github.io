---
# template tags (but you can change these)

layout: post
category: article


# tags user defined

tags: uncategorized
lang: ja_JP
author: 3y
title: Github PagesによるWebブログ制作の手引
date: 2021-06-05 23:45:33 +0900
---

このサイトはGithub PagesとJekyllという静的サイトビルダによって作られています。<br>
これを使えば、独自ドメイン利用、サイトのHTTPS化、マークダウンによる記事の出力、全て無料で利用できます。<br>
早速自分のサイトを作ってみましょう。

## 用意するもの

- githubアカウント
- gitコマンドが実行できる環境
- Ruby実行環境（任意）

アカウントの作成とgitコマンドの実行環境は省略します

## 1. Githubでリポジトリを作成する

Githubにログインした状態で、右上の＋▼を選びます。<br>
![new-repo](https://user-images.githubusercontent.com/27488794/120899058-c6d9e800-c668-11eb-951c-088d427a5c5b.png)<br>
すると、new repositoryという欄が出るので選択します。

作成するときはリポジトリ名を`[ユーザー名].github.io`とします。<br>
任意の名前にもできますが、その場合はページのルートパスが`https://[ユーザー名].github.io/[リポジトリ名]`となります。

リポジトリだけ作成した場合は、その後表示される手順に従って手元のPCから`git push`まで行います。
LICENSEやDescriptionなどを指定した場合は、`git clone [URL]`コマンドでリポジトリをクローンします。

## 2. テンプレートを作成する

jekyllではブログを簡単に作る仕組みが予め用意されています。<br>
以下の通りにファイルを配置すればWebサイトが作れます。

``` console
/
├─ /_posts # 記事を保存するディレクトリ
│  ├ YY-MM-DD-記事１.markdown # マークダウンで書かれた記事
│  └ YY-MM-DD-記事２.markdown
├─ _config.yml # Jekyllで使うテーマやプラグインを記述する
└─ index.markdown # サイトのindex.htmlとなるページ
```

まずは`_config.yml`を作成します。<br>
内容は以下のようにします。

```yaml:_config.yml
# _config.yml
title: まいブログ
email: example@example.com
description: >- # この記号は"baseurl:"の行まで続けることを意味します
説明！
説明終わり！
github_username:  hiuctf
theme: minima 
plugins:
  - jekyll-feed
  - jekyll-seo-tag
```

続けて`index.markdown`も作成します<br>
内容は以下のようにします。

``` coffescript:index.markdown
---
page: home
---
```

このページはここで終わっている…（書きかけ）