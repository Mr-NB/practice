

import jieba
import jieba.posseg as psg

# s = u'我想和女朋友一起去北京故宫博物院参观和闲逛。'
#
# cut = jieba.cut(s)   #精确模式
# all_cut = jieba.cut(s,cut_all=True)   #全模式
# search_cut = jieba.cut_for_search(s)  #搜索引擎模式
# print('/'.join(cut))
# print('/'.join(all_cut))
# print('/'.join(search_cut))
#
#
# print([(x.word,x.flag) for x in psg.cut(s)])  #获取词性
#
# print( [(x.word,x.flag) for x in psg.cut(s) if x.flag.startswith('n')])  #获取名词


# 开启并行分词模式，参数为并发执行的进程数
# jieba.enable_parallel(5)

# 关闭并行分词模式
# jieba.disable_parallel()

# santi_text = open('./santi.txt').read()
# jieba.enable_parallel(100)
# santi_words = [x for x in jieba.cut(santi_text) if len(x) >= 2]
# jieba.disable_parallel()
#
#
# from collections import Counter
# c = Counter(santi_words).most_common(20)  #获取词频

#使用用户字典提高分词准确性

txt = u'欧阳建国是创新办主任也是欢聚时代公司云计算方面的专家'
jieba.load_userdict('user_dict.txt')
print(','.join(jieba.cut(txt)))