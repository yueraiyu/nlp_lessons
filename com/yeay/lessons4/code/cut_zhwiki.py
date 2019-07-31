from pathlib import Path
import re
import json
import opencc
import jieba

zhwiki_path = "./extracted_xml"
zhwiki_out = "./zhwiki_word"

def cut_word(in_str):
    return list(jieba.cut("".join(re.findall('\w+', in_str))))

def cut_file(in_file):
    cuts = []
    cc = opencc.OpenCC('t2s')
    with open(in_file) as file:
        for i, line in enumerate(file.readlines()):
            content = json.loads(line)
            [cuts.append(w) for w in cut_word(cc.convert(content["text"]))]
    return cuts

def load_zhwiki_dump_files(path):
    zhwiki_files = []

    for entry in Path(path).iterdir():
        file_path = path + "/" + entry.name
        if not entry.name.startswith("."):
            if entry.is_file():
                zhwiki_files.append(file_path)
            elif entry.is_dir():
                zhwiki_files = zhwiki_files + load_zhwiki_dump_files(file_path)

    return zhwiki_files

def cuts():
    zhwiki_files = load_zhwiki_dump_files(zhwiki_path)
    with open(zhwiki_out, 'w') as f:
        for index, zhwiki_file in enumerate(zhwiki_files):
            print("start cut zhwiki %d file : %s" %(index, zhwiki_file))
            words = cut_file(zhwiki_file)
            f.write(" ".join('%s' %w for w in words))
            print("end cut zhwiki %d file : %s" % (index, zhwiki_file))

if __name__== '__main__':
    cuts()

