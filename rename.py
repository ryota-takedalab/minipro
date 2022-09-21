import os
import glob

#ファイル名に含まれる変更したい単語と変更後の単語
before_word = "yusaku_THUMBOPEN"
after_word = "C"

#カレントディレクトリに含まれるファイルを取得する
files = glob.glob('*'+ before_word +'*')
#print(files)

#before_wordの単語をafter_wordに変更
for before_file_name in files:
    after_file_name = before_file_name.replace(before_word,after_word)
    os.rename(before_file_name,after_file_name)