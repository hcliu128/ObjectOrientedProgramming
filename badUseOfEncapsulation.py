class Bank():
    def __init__(self, id, password, moneyAmount, address):
        self.id = id
        self.password = password
        self.moneyAmount = moneyAmount
        self.address = address

XiaoMingWang = Bank("A123456789", "0000", "100000", "Taipei XinYi District")

print(XiaoMingWang.id)
print(XiaoMingWang.password)
print(XiaoMingWang.moneyAmount)
print(XiaoMingWang.address)
    