# in the_bank.py

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


# in the_bank.py

class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin: Account, dest: Account, amount: float) -> bool:
        """
        @origin:  int(id) or str(name) of the first account
        @dest:    int(id) or str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return         True if success, False if an error occurred
        """

        if not self.is_corrupted(origin) and not self.is_corrupted(
                dest) and origin in self.account and dest in self.account:
            index_origin = self.account.index(origin)
            index_dest = self.account.index(dest)
            value = self.account[index_origin].value
            if value >= amount and value > 0:
                self.account[index_origin].value -= amount
                self.account[index_dest].value += amount
                return True
        return False

    @staticmethod
    def is_corrupted(account):
        ok = False
        count = 0
        attributes = list(filter(lambda att: not att.startswith("__"), dir(account)))
        if len(attributes) % 2 == 0:
            return True
        for attr in attributes:
            if attr[0] == "b":
                return True
            if attr.startswith("zip") or attr.startswith("addr"):
                ok = True
            if attr == "id" or attr == "value" or attr == "name":
                count += 1
        return True if count != 3 or not ok else False

    def fix_account(self, account) -> bool:
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occurred
        """
        if self.is_corrupted(account):
            print("YES")
        return False


bank = Bank()
account1 = Account(name="Mo", addr="1250 Dr lamaaziz El Attaouia Morocco", value=1000, zip=43150)
account2 = Account(name="Paul", addr="1250 Dr Cal USA", value=3500, zip=40000)
account3 = Account(name="Takashi", addr="1250 Dr Tokyo Japan", value=5000, zip=20000)
account4 = Account(name="Takashi", addr="1250 Dr Tokyo Japan", value=5000, zip=20000)

bank.add(account1)
bank.add(account2)
bank.add(account3)

account1.value = 1000
account2.value = 3500
account3.value = 5000

print(bank.transfer(account2, account1, 1500))
print(bank.fix_account(account4))
