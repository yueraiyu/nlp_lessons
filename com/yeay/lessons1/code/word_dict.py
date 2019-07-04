# 文本清理
import os
import re
import jieba
import json
import pandas as pd
import time
from collections import Counter
import com.yeay.lessons1.code.sentence_builder as sentence_builder

# 新闻数据
news_file = '/Users/yeah/Downloads/sqlResult_1558435.csv'
# 电影评论数据
movies_file =  '/Users/yeah/Downloads/movie_comments.csv'
# 保险评论数据
insurance_file = '/Users/yeah/Downloads/train.txt'
# 分词字典
dicts_file = './dict.json'


# 获取文本内容
def token(string):
    return re.findall('\w+', string)


# jieba分词
def cut(string):
    return list(jieba.cut(string))


# 分词处理文本文件
def cut_all(file):
    cuts = []
    for i, line in enumerate(open(file).readline()):
        # print("cut line num %d" % i)
        # if i == 100:
        #     break
        cuts.append(cut(line))
    return cuts


# 读取分词字典
def load_dict(file):
    word_dicts = {}
    if os.path.exists(file):
        with open(file, 'r') as f:
            word_dicts = json.loads(f.read())
    return word_dicts


# 读取csv
def load_csv(file, key, encode):
    content = pd.read_csv(file, encoding=encode)
    return content[key].tolist()


# 读取txt
# def load_txt(file) :
#     with open(file, 'r') as f :
#         word_dicts = json.loads(f.read())

# 清洗数据  去除无效字符 生成分词字典
def build_dicts(contents, key):
    cache_file = './cache.txt'
    now = time.time()
    #  清理数据写入缓存文件
    for a in contents:
        with open(cache_file, 'a') as f:
            f.write(''.join(token(str(a))))
    end = time.time()
    print("cache file spent %d" % (end - now))

    #  分词
    now = time.time()
    dicts = load_dict(dicts_file)
    if key in dicts:
        print("before cut, dicts[%s] length : %d" % (key, len(dicts[key])))
    else:
        print("before cut, dicts[%s] length : %d" % (key, 0))

    cuts = cut_all(cache_file)
    end = time.time()
    print("cut spent %d, cuts length : %d" % (end - now, len(cuts)))

    # dicts[key] = reduce(add, cuts) reduce 太慢了，先写到文件，后面用正则替换掉'[]'
    dicts[key] = re.findall('[^\[\],\s\"\']', str(cuts))
    print("after cut, dicts[%s] length : %d" % (key, len(dicts[key])))

    # 保存文件
    with open(dicts_file, 'w') as f:
        f.write(json.dumps(dicts))

    # 文本处理完后删除缓存文件
    os.remove(cache_file)


def init_dicts():
    dicts = load_dict(dicts_file)
    print(dicts.keys())
    TOKENS = dicts['news'] + dicts['movies']
    TOKENS_COUNT = Counter(TOKENS)

    TOKENS2 = [
        ''.join(TOKENS[i:i + 2]) for i in range(len(TOKENS[:-2]))
    ]
    TOKENS_COUNT2 = Counter(TOKENS2)

    return TOKENS, TOKENS_COUNT, TOKENS2, TOKENS_COUNT2


def prob_1(w):
    return TOKENS_COUNT[w] / len(TOKENS)


def prob_2(w1, w2):
    if w1 + w2 in TOKENS_COUNT2:
        return TOKENS_COUNT2[w1 + w2] / len(TOKENS2)
    else:
        return 1 / len(TOKENS2)


def get_probablity(sentence):
    words = cut(sentence)
    sen_pro = 1
    for i, word in enumerate(sentence[:-1]):
        next_ = sentence[i + 1]
        pro = prob_2(word, next_)
        sen_pro *= pro
    #     print('pro(%s) : %g' % (sentence, sen_pro))
    return sen_pro

if __name__== '__main__':
    # build_dicts(load_csv(news_file, 'content', 'gb18030'), 'news')
    # build_dicts(load_csv(movies_file, 'comment', 'utf8'), 'movies')
    TOKENS, TOKENS_COUNT, TOKENS2, TOKENS_COUNT2 = init_dicts()
    waiter_gram = sentence_builder.analytical_gram(sentence_builder.waiter, '=>')
    s1 = sentence_builder.generate(waiter_gram, 'waiter')
    print('pro(%s) : %f' % (s1, get_probablity(s1)))

    sproter_gram = sentence_builder.analytical_gram(sentence_builder.sporter, '=>')
    s2 = sentence_builder.generate(sproter_gram, 'sporter')
    print('pro(%s) : %f' % (s2, get_probablity(s2)))

    human_gram = sentence_builder.analytical_gram(sentence_builder.human, '=')
    s3 = sentence_builder.generate(human_gram, 'human')
    print('pro(%s) : %f' % (s3, get_probablity(s3)))

    host_gram = sentence_builder.analytical_gram(sentence_builder.host, '=')
    s4 = sentence_builder.generate(host_gram, 'host')
    print('pro(%s) : %f' % (s4, get_probablity(s4)))

