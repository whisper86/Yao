import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


# 1、split()函数
# 语法：str.split(str="",num=string.count(str))[n]
# str:表示为分隔符，默认为空格，但是不能为空(’’)。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
# num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
# [n]:表示选取第n个分片
# 注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略
class FrenchDeck:
    # 列表解析，ranks的列表是扑克牌的数字
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # suits 的列表是扑克牌的花色
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck
beer_card = Card(3, "clubs")
print(beer_card)