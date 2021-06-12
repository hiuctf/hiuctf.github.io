import datetime

class TTYnav:
    

    # init

    def __init__(self):
        
        # 項目パラメータはハードコード

        self.post_author = None
        self.post_type = None
        self.post_title = None
        self.post_filename = None
        self.post_timestamp = datetime.datetime.now()

    
    # run

    def execute_dialog(self):

        # 入力項目の追加もハードコード

        self.ask_post_type()
        self.ask_post_title()
        self.ask_post_filename()
        self.ask_post_author()


    # ask filename

    def ask_post_filename(self):
        self.post_filename = self.ask_something("URLに表示するファイル名を英語で入力してください\n無記入Enterで自動入力になります")
        return self.post_filename


    # ask title

    def ask_post_title(self):
        self.post_title = self.ask_something("記事のタイトルを入力してください\n無記入Enterで自動入力になります")
        return self.post_title


    # ask author

    def ask_post_author(self):
        self.post_author = self.ask_someting("記事の執筆者名を入力してください\n")
        return self.post_author


    # ask post type

    def ask_post_type(self):
        self.post_type = self.ask_something("記事の種類を入力してください\n1: 技術解説, 2: 定例会議, 3: 日記, それ以外: \n")
        return self.post_type


    # ask something

    def ask_something(self, guide_text = ""):
        self.p(guide_text)
        stdin = input() 
        return None if stdin == "" else stdin


    # output

    def p(self, s):
        print(s)