# todo:
# ユーザー設定ファイルを作る
# #author: のようなタグとマッチさせて置き換える
# 既存記事のアップデート日時の挿入も可能にする
# 文字コードのせいでコマンドプロンプト非対応
# 可読性無視して書いたコードにコメント付けただけなので書き直せるなら書き直したい

import os
import sys
import datetime
import shutil as sh

#import blogtools


# デフォルトのテンプレートファイル

template_filename = "_templates/default.markdown"


# このディレクトリの親ディレクトリの絶対パスの生成
# 日付と記事名を結合した新規マークダウン記事のファイル名の生成

directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
lib_path = os.path.join(directory, "script/blogtools")
article_dir = os.path.join(directory, "_posts")



# テンプレートファイルの絶対パスの生成
# 新規記事ファイルの絶対パスの生成

template_path = os.path.join(directory, template_filename)


# コマンドライン引数から記事名を取り出す
# もし無ければユーザーに入力を促す

title = ""
if len(sys.argv) < 2:
    print("新規記事名（記事のトップに表示されます）を入力してください(日本語を推奨、無記入Enterで自動入力)：")
    title = input()
    if title == "":
        title = datetime.datetime.now().strftime("article%Y-%m-%d-%H-%M-%S")
else:
    title = sys.argv[1]
    
filetitle = ""
if len(sys.argv) < 3:
    print("ファイル名（URLに使われます）を入力してください(英語を推奨、無記入Enterで自動入力)：")
    filetitle = input()
    if filetitle == "":
        filetitle = datetime.datetime.now().strftime("article%Y-%m-%d-%H-%M-%S")
else:
    filetitle = sys.argv[2]


filename = "{}-{}.markdown".format(datetime.datetime.now().strftime("%Y-%m-%d"), filetitle)
new_article_path = os.path.join(article_dir, filename)

print("記事の作成者のニックネームを教えて下さい")
author = input()

# attr

attributes = {
    "title": title,
    "author": author,
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S +0900")
}



# 新規記事ファイルをテンプレートを基に作成

#sh.copyfile(template_path, new_article_path)
template_file_read = open(template_path, "r")
article_file_write = open(new_article_path, "w")

tags_area_flag = False
for line in template_file_read.readlines():
    line = line.rstrip()

    if line == "---":

        if tags_area_flag is True:
            for k, v in attributes.items():
                s = "{}: {}\n".format(k, v)
                article_file_write.write(s)
    
        else:
            tags_area_flag = True

    article_file_write.write(line + "\n")
    

# a

