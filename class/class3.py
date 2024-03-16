class MyProduct:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.sales = 0

    def summary(self):
        message = "called summary().\n name: " + self.get_name() + \
                    "\n price: " + str(self.price) + \
                    "\n stock: " + str(self.stock) + \
                    "\n sales: " + str(self.sales)
        print(message)

    def get_name(self):
        return self.name

    def discount(self, n):
        self.price -= n


class MyProductSalesTax(MyProduct):
    # MyProductSalesTaxでは第四引数に消費税率を受け取る事にします
    def __init__(self, name, price, stock, tax_rate):
        # super()を使うと親クラスのメソッドを呼び出す事ができます
        # ここでは、MyProductクラスのイニシャライザを呼び出しています
        super().__init__(name, price, stock)
        self.tax_rate = tax_rate

    # MyProductSalesTaxではMyProductのget_nameをオーバーライド(上書き)します
    def get_name(self):
        return self.name + "(税込)"

    # MyProductSalesTaxにget_price_with_taxを新規実装します
    def get_price_with_tax(self):
        return int(self.price * (1 + self.tax_rate))

    # MyProductのsummaryメソッドをオーバーライドしてsummaryのpriceが税込み価格を出力するようにしてください
    def summary(self):
        message = "called summary().\n name: " + self.get_name() + \
                    "\n price: " + str(self.get_price_with_tax()) + \
                    "\n stock: " + str(self.stock) + \
                    "\n sales: " + str(self.sales)
        print(message)

product_3 = MyProductSalesTax("phone", 30000, 100, 0.1)
print(product_3.get_name())
print(product_3.get_price_with_tax())
product_3.summary()
