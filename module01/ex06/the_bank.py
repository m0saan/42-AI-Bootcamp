# in the_bank.py

class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        # if hasattr(self, 'value'):
        #     self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def is_corrupted(self):
        ok = True
        attributes = list(self.__dict__.keys())
        if "value" not in attributes:
            return True
        if len(attributes) % 2 == 0:
            return True
        for attr in attributes:
            if attr[0] == "b":
                return True
            if attr.startswith("zip") or attr.startswith("addr"):
                ok = False
        return ok


# in the_bank.py

class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []
        self.has_b_prefix = False

    def add(self, account):
        self.account.append(account)

    def get_account(self, p):
        if isinstance(p, int):
            for account in self.account:
                if account.id == p:
                    return account
        if isinstance(p, str):
            for account in self.account:
                if account.name == p:
                    return account

    def transfer(self, origin, dest, amount: float) -> bool:
        """
        @origin:  int(id) or str(name) of the first account
        @dest:    int(id) or str(name) of the destination account
        @amount:  float(amount) amount to transfer
        @return         True if success, False if an error occurred
        """
        origin_account = self.get_account(origin)
        dest_account = self.get_account(dest)
        if not isinstance(origin_account, Account) or not isinstance(dest_account, Account):
            return False
        elif not origin_account.is_corrupted() and not dest_account.is_corrupted():
            value = origin_account.value
            if value >= amount and value > 0:
                origin_account.value -= amount
                dest_account.transfer(amount)
                return True
        return False

    def fix_account(self, account: Account) -> bool:
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occurred
        """
        if account.is_corrupted():
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


if __name__ == '__main__':
    print("\n1- Initial tow Accounts 'abdlali' and 'salmi':")
    abdlali = Account("abdelaali", addr="el kelaa des sraghna", value=100, test=10)
    salmi = Account("salmi", addr="bengerir", value=0, test=10)

    print("\n2- Check if any accounr is corrupted:")
    print("\tabdlali : ", abdlali.is_corrupted())
    print("\tsalmi   : ", salmi.is_corrupted())

    print("\n3- Adding the two accounts to the Bank:")
    bank = Bank()
    bank.add(abdlali)
    bank.add(salmi)

    print("\n4- Show the amount of the two accounts:")
    print("\tabdlali : ", abdlali.value)
    print("\tsalmi   : ", salmi.value)

    print("\n5- Make a transfer with 10 from abdlali --> salmi:")
    bank.transfer("abdelaali", "salmi", 10)

    print("\n6- Show the amount of the two accounts again:")
    print("\tabdlali : ", abdlali.value)
    print("\tsalmi   : ", salmi.value)

    print("\n7- Create a correpted account 'mohammed' and adding it to the Bank:")
    mohammed = Account("mohammed")
    bank.add(mohammed)

    print("\n8- Check if 'mohammed' is a corrupted account:")
    print("\tmohammed : ", mohammed.is_corrupted())

    # print("\n9- Try to fixing it:")
    # print("\tAttributes before fixing: ", mohammed.__dict__)
    # bank.fix_account('mohammed')
    # print("\tAttributes after fixing: ", mohammed.__dict__)
#
# print("\n10- Check if 'mohammed' is still corrupted:")
# print("\tmohammed : ", mohammed.is_corrupted())
