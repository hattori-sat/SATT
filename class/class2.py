# MyProductクラスを定義
class MyProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.sales = 0
    # 概要メソッド
    # 文字列と「自分自身のメソッド」や「自分自身のメンバ」を連結して出力します
    def summary(self):
        message = "called summary()."  + \
        "\n name: "  + self.get_name() + \
        "\n price: " + str(self.price) + \
        "\n stock: " + str(self.stock) + \
        "\n sales: " + str(self.sales)
        print(message)
    # nameを返すget_name()を作成して下さい
    def get_name(self):
        return self.name
    # 引数のぶんだけpriceを減らすdiscount()を作成して下さい
    def discount(self, n):
        self.price -= n

product_2 = MyProduct("phone", 30000, 100)
# 5000だけdiscountして下さい
product_2.discount(5000)
# product_2のsummaryを出力して下さい
product_2.summary()
