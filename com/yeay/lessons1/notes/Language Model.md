#### Language Model

##### [Learning NLP Language Models with Real Data](https://towardsdatascience.com/learning-nlp-language-models-with-real-data-cdff04c51c25)

##### Part 1: Defining Language Models

* 概率计算公式

  `P(W) = P(w1,w2,w3,...,Wn)`

  `P(w5|w1,w2,w3,w4)`

* 条件概率

  `P(A|B) = P(AB)/P(B)`

* 自然语言概率计算

  `P(x1,x2,…,xn)=P(x1)P(x2|x1)P(x3|x2,x1)P(x4|x3,x2,x1)…P(xn|x1xn-1,xn-2,…,x1)`

  `sentence => its water is so transparent`

  `P('its water is so transparen')` = `P(its)` * 

  ​																	`P(water|its)` * 

  ​																	`P(is|its water)` * 

  ​																	`P(so|its water is)` * 

  ​																	`P(transparent|its water is so)`

* [马尔可夫链](https://baike.baidu.com/item/马尔可夫链)

  马尔可夫链是一组具有`马尔可夫性质`的离散随机变量的集合。

* 马尔可夫性质



##### [N-gram Language Models](https://web.stanford.edu/~jurafsky/slp3/3.pdf)

##### [Language Modeling](https://web.stanford.edu/class/cs124/lec/languagemodeling.pdf)