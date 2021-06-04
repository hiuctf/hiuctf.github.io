# todo:
# ユーザー設定ファイルを作る
# #author: のようなタグとマッチさせて置き換える
# 既存記事のアップデート日時の挿入も可能にする
# コマンドプロンプトから入力した時の文字コード変換が必要

import os
import sys
import datetime
import shutil as sh


# デフォルトのテンプレートファイル

template_filename = "_templates/default.markdown"


# コマンドライン引数から記事名を取り出す
# もし無ければユーザーに入力を促す

title = ""
if len(sys.argv) < 2:
    print("新規記事名を入力してください：")
    title = input()
else:
    title = sys.argv[1]
    
#title = unicode()

# attr

attributes = {
    "title": title,
    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S +0900")
}


# このディレクトリの絶対パスの生成
# 日付と記事名を結合した新規マークダウン記事のファイル名の生成

directory = os.path.abspath(os.path.dirname(__file__))
article_dir = os.path.join(directory, "_posts")
filename = "{}-{}.markdown".format(datetime.datetime.now().strftime("%Y-%m-%d"), title)


# テンプレートファイルの絶対パスの生成
# 新規記事ファイルの絶対パスの生成

template_path = os.path.join(directory, template_filename)
new_article_path = os.path.join(article_dir, filename)


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

