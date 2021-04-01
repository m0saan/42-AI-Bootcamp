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
        self.has_b_prefix = False

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

    def is_corrupted(self, account):
        ok = False
        count = 0
        attributes = list(filter(lambda att: not att.startswith("__"), dir(account)))
        if len(attributes) % 2 == 0:
            return True
        for attr in attributes:
            if attr[0] == "b":
                self.has_b_prefix = True
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
            attr_dict = {'addr': '', 'value': 0, 'zip': 0}
            account_attrs = list(account.__dict__.keys())
            account_attrs.sort()
            for attr in attr_dict.keys():
                if attr not in account_attrs:
                    account.__setattr__(attr, attr_dict[attr])
                    print(attr)
            if self.has_b_prefix:
                for i, attr in account.__dict__.keys():
                    if attr[0] == "b":
                        print(attr)
                        # account.__delattr__(attr)
                        # account.__setattr__()

        return False


bank = Bank()
account1 = Account(name="Mo", baddr="1250 Dr lamaaziz El Attaouia Morocco", value=1000)

print(bank.__dict__)
print(account1.__dict__)

bank.fix_account(account1)

# account2 = Account(name="Paul", addr="1250 Dr Cal USA", value=3500, zip=40000)
# account3 = Account(name="Takashi", addr="1250 Dr Tokyo Japan", value=5000, zip=20000)
# account4 = Account(name="Takashi", addr="1250 Dr Tokyo Japan", value=5000, zip=20000)
#
# bank.add(account1)
# bank.add(account2)
# bank.add(account3)
#
# account1.value = 1000
# account2.value = 3500
# account3.value = 5000
#
# print(bank.transfer(account2, account1, 1500))
# print(bank.fix_account(account4))
