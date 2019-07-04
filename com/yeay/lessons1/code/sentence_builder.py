import random

waiter = """
waiter => ""
waiter => 问候 迎接 询问 需求 物品 结尾
问候 => 称呼 打招呼 | 打招呼
称呼 => 先生 | 女生 | 老人家 | 小朋友
打招呼 => 下午好 | 晚上好 | 早上好 | 你好 | 您好
迎接 => 欢迎光临
询问 => 请问您需要
需求 => 吃 | 喝 | 玩 | 看 | 听
物品 => 点什么
结尾 => 吗？
"""

sporter = """
sporter => ""
sporter => 运动 头衔 姓名 时间 动作 赛事 等级 谓语 头衔
运动 => 著名 羽毛球
头衔 => 运动员 世界冠军 | 伟大的运动员 | 四大天王
姓名 => 李宗伟 | 林丹 | 陶菲克 | 盖德
时间 => 曾经 | 过去 | 以前 | 很早就
动作 => 获得 | 失去 | 卫冕 | 夺得 
赛事 => 世锦赛 | 马来西亚公开赛 | 奥运会 | 苏迪曼杯 | 汤姆斯杯 | 亚运会 | 全英公开赛
等级 => 冠军 | 亚军 | 季军 
谓语 => 是
"""

simple_grammar = """
sentence => noun_phrase verb_phrase 
noun_phrase => Article Adj* noun
Adj* => null | Adj Adj*
verb_phrase => verb noun_phrase
Article => 一个 | 这个
noun => 女人| 篮球|桌子|小猫
verb => 看着 | 听着 | 看见
Adj=> 蓝色的| 好看的|小小的|年轻的 
"""

human = """
human = 自己 寻找  活动
自己 = 我 | 俺 | 我们 
寻找 = 看看 | 找找 | 想找点
活动 = 乐子 | 玩的
"""

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字  号
数字 = 单个数字 | 数字 | 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 | 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？"""

# step 1 解析语法
def analytical_gram(gramStr, sp):
    grammer = {}
    for line in gramStr.split('\n'):
        if not line.strip(): continue
        exp, stmt = line.split(sp)
        grammer[exp.strip()] = [s.split() for s in stmt.split('|')]

    return grammer


# step 2 根据语法生成
def generate(gram, target):
    if target not in gram: return target
    new_expanded = random.choice(gram[target])
    return ''.join(generate(gram, t) for t in new_expanded if t != 'null')


def generate_n(n):
    # you code here
    grams = {"waiter": analytical_gram(waiter, '=>'),
             "sporter": analytical_gram(sporter, '=>'),
             #                  "human":analytical_gram(human, '='),
             "host": analytical_gram(host, '=')}
    keys = [key for key in grams.keys()]

    stmts = []
    for i in range(0, n):
        key = random.choice(keys)
        stmts.append(generate(grams[key], key))

    return stmts