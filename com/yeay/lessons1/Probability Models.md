# Probability Models

```概率模型```

A *probability model* is a mathematical representation of a random phenomenon. It is defined by its *sample space*, *events* within the sample space, and *probabilities* associated with each event.

```概率模型是随机现象的数学表示。它由样本空间，样本空间内的事件以及与每个事件相关的概率定义。```

The **sample space S** for a probability model is the set of all possible outcomes.

```概率模型的样本空间S是所有可能结果的集合。```

For example, suppose there are 5 marbles in a bowl. One is red, one is blue, one is yellow, one is green, and one is purple. If one marble is to be picked at random from the bowl, the sample space possible outcomes *S* = {red, blue, yellow, green, purple}. If 3 of the marbles are red and 2 are blue, then the sample space *S* = {red, blue}, since only two possible color outcomes be possible. If, instead, two marbles are picked from a bowl with 3 red marbles and 2 blue marbles, then the sample space *S* = {(2 red), (2 blue), (1 red and 1 blue)}, the set of all possible outcomes.

```例如，假设碗中有5个弹珠。一个是红色，一个是蓝色，一个是黄色，一个是绿色，一个是紫色。如果要从碗中随机挑选一颗弹珠，样品空间的可能结果 S = {红色，蓝色，黄色，绿色，紫色}。如果3个弹珠是红色而2个是蓝色，那么样本空间S = {红色，蓝色}，因为只有两种可能的结果在可能的颜色集合中。相反，如果从带有3个红色弹珠和2个蓝色弹珠的碗中挑选出两个弹珠，则样本空间 S = {（2个红色），（2个蓝色），（1个红色和1个蓝色）}，所有这些可能的结果```

An **event A** is a subset of the sample space S. 

```事件A是样本空间S的子集。```

Suppose there are 3 red marbles and 2 blue marbles in a bowl. If an individual picks three marbles, one at a time, from the bowl, the event "pick 2 red marbles" can be achieved in 3 ways, so the set of outcomes *A* = {(red,red, blue),(red, blue,red), (blue, red,red)}. The sample space for picking three marbles, one at a time, is all of the possible ordered combinations of three marbles, *S* = {(red, red, red), (red, red, blue), (red, blue, red), (blue, red, red), (blue, blue, red), (blue, red, blue), (red, blue, blue)}. Since there are only 2 blue marbles, it is impossible to achieve the event {blue, blue,blue}.

```假设一个碗里有3个红色弹珠和2个蓝色弹珠。如果一个人从碗中一次一个地挑选三颗弹珠，则可以通过三种方式实现“挑选2个红色弹珠”的事件，因此结果集 A = {（红色，红色，蓝色），（红色，蓝色，红色），（蓝色，红色，红色）}。用于挑选三颗弹珠的样本空间，一次一个，是三颗弹珠的所有可能的有序组合，S = {（红色，红色，红色），（红色，红色，蓝色），（红色，蓝色，红色） ，（蓝色，红色，红色），（蓝色，蓝色，红色），（蓝色，红色，蓝色），（红色，蓝色，蓝色）}。由于只有2个蓝色弹珠，因此无法实现{蓝色，蓝色，蓝色}事件。```

A **probability** is a numerical value assigned to a given event *A*. The probability of an event is written *P(A)*, and describes the long-run relative frequency of the event. The first two basic rules of probability are the following:

```概率是分配给给定事件A的数值。事件的概率写为P（A），并描述事件的长期相对频率。概率的前两个基本规则如下：```

`Rule 1` : *Any probability P(A) is a number between 0 and 1 (0 < P(A) < 1).*

```任何概率P（A）是0和1之间的数字(0 < p(A) < 1)```

`Rule 2` : *The probability of the sample space S is equal to 1 (P(S) = 1).*

```样本空间S的概率等于1（P（S）= 1）。```

Suppose five marbles, each of a different color, are placed in a bowl. The sample space for choosing one marble, from above, is *S* = {red, blue, yellow, green, purple}. Since one of these must be selected, the probability of choosing *any* marble is equal to the probability of the sample space *S* = 1. Suppose the event of interest is choosing the purple marble, *A* = {purple}. If it is equally likely that any one marble will be selected, then the probability of choosing the purple marble, *P(A)* = 1/5. In general, the following formula describes the calculation of probabilities for equally likely outcomes:

```假设五个不同颜色的弹珠放在一个碗里。从上面选择一个弹珠的样本空间是S = {红色，蓝色，黄色，绿色，紫色}。由于必须选择其中一个，因此选择任何弹珠的概率等于样本空间S = 1的概率。假设感兴趣的事件是选择紫色弹珠，A = {紫色}。如果同样可能选择任何一颗弹珠，则选择紫色弹珠的概率为P（A）= 1/5。通常，以下公式描述了同等可能结果的概率计算：```

**If there are k possible outcomes for a phenomenon and each is equally likely, then each individual outcome has probability 1/k.** **The probability of any event A is**

```如果某种现象存在k个可能的结果，并且每个结果的可能性相同，那么每个单独的结果的概率为1 / k。 任何事件A的概率是:```

`P(A)` = `count of outcomes in A` `/`  `count of outcomes in S`

​		   = `count of outcomes in A`  `/`  `k`

If two events have no outcomes in common, then they are called **disjoint**. For example, the possible outcomes of picking a single marble are disjoint: only one color is possible on each pick. The addition of probabilities for disjoint events is the third basic rule of probability:

```如果两个事件没有共同的结果，那么它们被称为不相交。例如，挑选单个弹珠的可能结果是不相交的：每次选择只能有一种颜色。增加不相交事件的概率是概率的第三个基本规则```

`Rule 3` : *If two events A and B are disjoint, then the probability of either event is the sum of the probabilities of the two events:P(A or B) = P(A) + P(B).*

```如果事件A和B不相交，那么任一事件的概率都是两个事件概率的总和： P（A或B）= P（A）+ P（B）。```

The chance of *any* (one or more) of two or more events occurring is called the **union** of the events. The probability of the union of disjoint events is the sum of their individual probabilities. 

```发生两个或多个事件中的任何（一个或多个）事件的可能性称为事件的并集。不相交事件结合的概率是它们各自概率的总和。```

For example, the probability of drawing either a purple, red, or green marble from a bowl of five differently colored marbles is the sum of the probabilities of drawing any of these marbles: 1/5 + 1/5 + 1/5 = 3/5. 

```例如，从一个放有五个不同颜色弹珠的碗中取出紫色，红色或绿色弹珠的概率，是去除这些弹珠中的任何一个的可能性的总和：1/5 + 1/5 + 1/5 = 3 / 5。```

If there are three red marbles and two blue marbles, then the probability of drawing any red marble is the number of outcomes in the event " red," which is equal to three, divided by the total number of outcomes, 5, or 3/5 = 0.6. The sample space is this case is {red, blue}, which must have total probability equal to 1, so the probability of drawing a blue marble is equal to 2/5 = 0.4. The event of drawing a blue marble does not occur if a red marble is chosen, so the event *A* = "blue" is called the ***complement** Ac* of the event "red." Since an event and its complement together form the entire sample space *S*, the probability of an event *A* is equal to the probability of the sample space *S*, minus the probability of *Ac*, as follows:

```如果有三个红色弹珠和两个蓝色弹珠，则取出任何红色弹珠的概率是“红色”事件中的结果数，等于三，除以结果总数5（3 / 5 = 0.6）。此示例空间为{red，blue}，其总概率必须等于1，因此取出蓝色弹珠的概率等于2/5 = 0.4。如果选择红色弹珠，则不会出现取出蓝色弹珠的事件，因此事件A =“蓝色”被称为事件“红色”的补充Ac。由于事件及其补码一起形成整个样本空间S，因此事件A的概率等于样本空间S的概率减去Ac的概率，如下：``

`Rule 4` : The probability that any event A does not occur is P(Ac) = 1 - P(A).

```任何事件A不发生的概率是P（Ac）= 1-P（A）。```

### Venn Diagrams

```韦恩图```

A useful graphical tool for studying the complements, intersections, and unions of events within a sample space S is known as a *Venn diagram*. In such a diagram, events are drawn as regions that may or may not overlap. 

用于研究样本空间S内的事件的补集，交集和并集的图形工具被称为韦恩图。在这样的图中，事件被绘制为可能重叠或不重叠的区域。

![img](http://www.stat.yale.edu/Courses/1997-98/101/venn1.gif)

In the Venn diagram to the top, events *A* and *B* are disjoint. Suppose, for example, event *A* is drawing a red marble from a bowl of five differently colored marbles, and event *B* is drawing a blue marble. These events cannot both occur, so there is no overlapping area. 

在上边的韦恩图中，事件A和B是不相交的。例如，假设事件A是从一个有五个不同颜色弹珠的碗中取出一个红色弹珠，而事件B是取出一个蓝色弹珠。这些事件不会同时发生，因此没有重叠区域。

![img](http://www.stat.yale.edu/Courses/1997-98/101/venn2.gif)

In the Venn diagram on the top, events *A* and *B* are not disjoint. This means that it is possible for both events to occur, and the overlapping area represents this possibility. Suppose, for instance, there are 3 red marbles and two blue marbles in a bowl. Two marbles are to be drawn from the bowl, one after the other. After the first draw, the marble drawn is returned to the bowl. Define event *A* to be drawing a red marble from the bowl on the first draw, and define event *B* to be drawing a blue marble on the second draw. The occurence of event *A* is represented by the red area, the occurence of event *B* is represented by the bluearea, the occurence of *both* events is represented by the overlapping area (also known as the *intersection* of the two events), and the occurence of *either* event is represented by the entire colored area (also known as the *union* of the two events). 

```在上边的韦恩图中，事件A和B不是相交的。这意味着两个事件可能同时发生，重叠区域代表着这种可能性。例如，假设一个碗里有3个红色弹珠和两个蓝色弹珠。将从碗中取出两个弹珠，一个接一个。第一次取出后，将取出的弹珠放回到碗中。将事件A定义为在第一次取出的弹珠是红色，并将事件B定义为在第二次取出的弹珠是蓝色。事件A的出现由红色区域表示，事件B的出现由蓝色区域表示，两个事件的出现由重叠区域（也称为两个事件的交集）表示，并且出现任何一个事件都由整个彩色区域（也称为两个事件的联合）表示。 ```

### Independence

```独立事件```

Consider two events which might occur in succession, such as two flips of a coin. If the outcome of the first event has no effect on the probability of the second event, then the two events are called *independent*. For two coin flips, the probability of getting a "head" on either flip is 1/2, regardless of the result of the other flip. The fourth basic rule of probability is known as the *multiplication rule*, and applies only to independent events:

```考虑可能连续发生的两个事件，例如两次掷硬币。如果第一个事件的结果对第二个事件的概率没有影响，那么这两个事件被称为独立事件。对于两个硬币翻转，无论另一个翻转的结果如何，在任一翻转上获得“头部”的概率是1/2。概率的第四个基本规则称为乘法规则，仅适用于独立事件：```

`Rule 5` : If two events A and B are independent, then the probability of both events is the product of the probabilities for each event: P(A and B) = P(A)P(B).

```如果两个事件A和B是独立的，那么两个事件的概率都是每个事件概率的乘积： P（A和B）= P（A）P（B）。```

The chance of *all* of two or more events occurring is called the **intersection** of events. For independent events, the probability of the intersection of two or more events is the product of the probabilities. In the case of two coin flips, for example, the probability of observing two heads is 1/2*1/2 = 1/4. Similarly, the probability of observing four heads on four coin flips is 1/2*1/2*1/2*1/2 = 1/16. 

```发生所有两个或更多事件的可能性称为事件的交集。对于独立事件，两个或更多事件的交集的概率是概率的乘积。 例如，在两个硬币翻转的情况下，观察两个头的概率是1/2 * 1/2 = 1/4。类似地，在四个硬币翻转上观察四个头的概率是1/2 * 1/2 * 1/2 * 1/2 = 1/16。```

**If two events A and B are not disjoint, then the probability of their union (the event that A or B occurs) is equal to the sum of their probabilities minus the sum of their intersection.**

```如果事件A和B不是不相交的，那么它们结合的概率（发生A或B的事件）等于它们的概率加上它们的交点之和的总和。```

In the example corresponding to the second Venn diagram above, we know that the probability of drawing a red marble on the first draw (event *A*) is equal to 3/5, and the probability of drawing a blue marble on the second draw (event *B*) is equal to 2/5. Since events *A* and *B* are independent, the probability of the *intersection* of A and B, *P(A and B)*, equals the product *P(A)\*P(B)* = 3/5*2/5 = 6/25. The probability of the *union*of *A* and *B*, *P(A or B)*, is equal to P(A) + P(B) - P(A and B)* = 3/5 + 2/5 - 6/25 = 1 - 6/25 = 19/25 = 0.76. 

```在对应于上面第二个韦恩图的示例中，我们知道在第一次绘制（事件A）上取出红色弹珠的概率等于3/5，并且在第二次取出蓝色弹珠的概率（事件） P（B）等于2/5。由于事件A和B是独立的，因此A和B的交叉概率P（A和B）等于乘积P（A）* P（B）= 3/5 * 2/5 = 6/25。 A和B，P（A或B）结合的概率等于 P（A）+ P（B）-P（A和B）= 3/5 + 2/5 - 6/25 = 1 - 6/25 = 19/25 = 0.76。```

For another example, consider tossing two coins. The probability of a head on any toss is equal to 1/2. Since the tosses are independent, the probability of a head on both tosses (the intersection) is equal to 1/2*1/2 = 1/4. The probability of a head on either toss (the union) is equal to the sum of the probabilities of a head on each toss minus the probability of the intersection, 1/2 + 1/2 - 1/4 = 3/4. 

```再举一个例子，考虑扔两个硬币。任何投掷头的概率等于1/2。由于投掷是独立的，因此两个投掷（交叉点）上的头部的概率等于1/2 * 1/2 = 1/4。任意一个投掷（联合）上的头部的概率等于每个投掷上的头部概率减去交叉点概率的总和，即1/2 + 1/2 - 1/4 = 3/4。```

**Note:** Disjoint events are **not** independent. In the marble example, consider drawing one marble from the bowl of five, where each marble is a different color. Suppose the event of interest, event *A*, is drawing a bluemarble. The probability of drawing this marble is 1/5. Suppose event *B* is drawing a green marble. These events are disjoint, since event *B* cannot occur if event *A* occurs. Obviously, they are not independent, since the outcome of event *A* directly affects the outcome of event *B*. If, instead, two marbles were to be drawn from the bowl, with the first marble replaced before the second marble was drawn, then the event of drawing a blue marble on the first draw would not affect the outcome of the second draw. The event of drawing a green marble on the second draw would be independent of the event of drawing a blue marble on the first draw, so the probability of **both** events occurring would be the product of the probabilities of each event, 1/5*1/5 = 1/25. 

```不相交的事件不是独立的。在弹珠的例子中，考虑从五个碗中取出一个弹珠，其中每个弹珠是不同的颜色。假设感兴趣的事件A事件正在取出蓝色弹珠。取出这弹珠的概率是1/5。假设事件B正在取出一个绿色弹珠。这些事件是不相交的，因为如果事件A发生，事件B不会发生。显然，它们不是独立的，因为事件A的结果直接影响事件B的结果。相反，如果从碗中抽出两个弹珠，在第二个弹珠被取出之前更换第一个弹珠，那么事件在第一次抽出时为蓝色弹珠不会影响第二次的结果。在第二次中取出绿色弹珠的事件将与第一次取出蓝色弹珠的事件无关，因此两个事件发生的概率将是每个事件概率的乘积，1/5 * 1/5 = 1/25。```