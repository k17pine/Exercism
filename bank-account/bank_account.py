import threading


lock = threading.Lock()


class BankAccount:
    def __init__(self):
        self.opened = False
        self.balance = 0

    def get_balance(self):
        if not self.opened:
            raise ValueError('ValueError')
        else:
            return self.balance

    def open(self):
        if self.opened:
            raise ValueError('ValueError')
        else:
            self.opened = True

    def deposit(self, amount):
        lock.acquire()
        try:
            if not self.opened:
                raise ValueError('ValueError')
            else:
                if amount >= 0:
                    self.balance = self.balance + amount
                else:
                    raise ValueError('ValueError')
        finally:
            lock.release()

    def withdraw(self, amount):
        lock.acquire()
        try:
            if not self.opened:
                raise ValueError('ValueError')
            else:
                if amount <= self.balance:
                    if amount >= 0:
                        self.balance = self.balance - amount
                    else:
                        raise ValueError('ValueError')
                else:
                    raise ValueError('ValueError')
        finally:
            lock.release()

    def close(self):
        if not self.opened:
            raise ValueError('ValueError')
        else:
            self.opened = False
            self.balance = 0
