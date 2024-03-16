# MyProductクラスを定義
class MyProduct:
    # イニシャライザを修正してください
    def __init__(self,name,price,stock):
        # 引数をメンバに格納してください
        self.name=name
        self.price=price
        self.stock=stock


        self.sales = 0

# MyProductを呼び出し、オブジェクトproduct_1を作成
product_1 = MyProduct("cake", 500, 20)

# product_1のstockを出力してください
print(product_1.stock)
