# _*_ coding: UTF-8 _*_
# created by ping on 2020/1/13 23:23

# 类和对象的使用
import datetime


class BankAccount:

    def __init__(self, money):
        """
        创建银行账户，成员变量：金额，创建时间
        """
        self.__money = 0
        self.__create_time = datetime.datetime.today()
        self.__trade_records = []
        self.__title = ('交易日期', '摘要', '金额', '余额')
        self.deposit(money)

    def deposit(self, income):
        if income <= 0:
            print("income is invalid!")
        else:
            nowtime = datetime.datetime.today()
            self.__money = self.__money + income
            trade = {'tp': '转入', 'money': income, 'time': nowtime, 'tot': self.__money}
            self.__trade_records.append(trade)

    def transfer(self, limit):
        if limit <= 0:
            print("limit is invalid!")
        else:
            nowtime = datetime.datetime.today()
            self.__money = self.__money - limit
            trade = {'tp': '转出', 'money': limit, 'time': nowtime, 'tot': self.__money}
            self.__trade_records.append(trade)

    def show(self):
        print('-----------------------------------------------')
        print('交易日期', '摘要', '金额', '余额')
        for trade in self.__trade_records:
            print(trade.get('time'), trade.get('tp'), trade.get('money'), trade.get('tot'))
        print('-----------------------------------------------')


bankAccount = BankAccount(100)
bankAccount.deposit(150)
bankAccount.transfer(30)
bankAccount.show()

