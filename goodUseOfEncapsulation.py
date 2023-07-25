class Bank():
    def __init__(self, id, password, moneyAmount, address):
        self.__id = id
        self.__password = password
        self.__moneyAmount = moneyAmount
        self.__address = address

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, newPassword):
        print("Setting new password ...")
        self.__password = newPassword

    def get_id(self):
        return self._id
    def get_moneyAmount(self):
        return self.__moneyAmount
    def get_address(self):
        return self.__address

XiaoMingWang = Bank("A123456789", "0000", "100000", "Taipei XinYi District")

try:
    print(XiaoMingWang.__moneyAmount)
except:
    print("AttributeError: 'Bank' object has no attribute '__moneyAmount'")
print(XiaoMingWang.get_moneyAmount())
try:
    print(f"XiaoMingWang's pwd is :{XiaoMingWang.__password}")
except:
    print("AttributeError: 'Bank' object has no attribute '__password'")

XiaoMingWang.password = "1234"
print(f"XiaoMingWang's pwd is :{XiaoMingWang.password}")
    
    