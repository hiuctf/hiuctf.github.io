# 特に無し
# WIP
# 再利用考えずに書いているのでgenerate_post.pyとかぶる所多い
# 冗長

import os
import sys
import datetime
import shutil as sh


attribute_key = ""
if len(sys.argv) < 2:
    print("変更する属性を入力してください（無入力でtimestamp）")
    attribute_key = input()
    if attribute_key == "":
        attribute_key = datetime.datetime.now().strftime("article%Y-%m-%d-%H-%M-%S")
else:
    attribute_key = sys.argv[1]


print("last-update: 時間をアップデートしました")

