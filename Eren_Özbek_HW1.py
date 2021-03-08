#I assume that all of the transactions are done within a fiscal year so I don't add year
class Date(): #Defining the class Date so that we can decide if we receive dividends
    def __init__(self, month, day):
        self.month = month
        self.day = day       
    def today_date(self):
        self.month = '0'*(2-len(str(self.month)))+str(self.month)
        self.day = '0'*(2-len(str(self.day)))+str(self.day)
        return self.month+'/'+self.day
        
class Cash():
    liquidity= 3
    def __init__(self):
        pass

class Stock():
    liquidity= 2
    def __init__(self, price, ticker, exchange):
        self.price = price
        self.ticker = ticker
        self.exchange= exchange

class MutualFund():
    liquidity=1
    def __init__(self, ticker, price=1):
        self.price = price
        self.ticker= ticker

class Bond(Stock):
    liquidity=2
    def __init__(self, price, ticker, exchange, coupon_payment):
        Stock.__init__(self, price, ticker, exchange)
        self.coupon_payment= coupon_payment
        
from random import uniform

class Portfolio():
    def __init__(self, Name):
        self.Name = Name
        self.cash_balance= 0
        self.stock_amount=0
        self.fund_share=0
        self.bond_amount=0
        self.my_stocks={}
        self.my_funds= {}
        self.my_bonds={}
        self.transaction_history=[]

    
    def addCash(self, cash_input, Date):
        self.cash_balance += cash_input
        self.transaction_history.append('Cash input of $%d ' %cash_input + 'on '+ Date.today_date())
        return 'Your current cash balance is %d as of ' %self.cash_balance +Date.today_date()
    
    def withdrawCash(self, cash_output, Date):
        self.cash_balance -= cash_output
        self.transaction_history.append('Cash output of $%d ' %cash_output + 'on '+ Date.today_date())
        return 'Your current cash balance is %d as of ' %self.cash_balance +Date.today_date()
        
    def buyStock(self, Stock, stock_amount, Date):
        self.stock_amount += stock_amount
        self.my_stocks[Stock.ticker]= stock_amount
        self.transaction_cost= stock_amount*Stock.price
        self.cash_balance -= self.transaction_cost
        self.transaction_history.append('%d shares of ' %stock_amount + Stock.ticker + ' is bought at ' +Stock.exchange+ ' for $ %d' %self.transaction_cost + ' on ' +Date.today_date())
        print ('Stocks you possess are ', self.my_stocks)
    
    def sellStock(self, Stock, stock_amount, Date):
        self.stock_amount -= stock_amount
        self.my_stocks[Stock.ticker] = stock_amount
        if int(Date.month) >= 9: #we assume a hypothetical dividend randomly chosen by board of directors and it is only given to the ones who sell their stocks after september
            self.transaction_gain = stock_amount*(Stock.price*uniform(0.5, 1.5) + uniform(Stock.price*0.01, Stock.price*0.1))
        else:
            self.transaction_gain = stock_amount*Stock.price*uniform(0.5, 1.5)      
        self.cash_balance += self.transaction_cost
        self.transaction_history.append('%d shares of ' %stock_amount + Stock.ticker + ' is sold at ' +Stock.exchange+ ' for $ %d' %self.transaction_gain + ' on ' +Date.today_date())
        print ('Stocks you possess are ', self.my_stocks)
    
    def buyMutualFund(self, MutualFund, fund_share, Date):
        self.fund_share += fund_share
        self.my_funds[MutualFund.ticker] = fund_share
        self.transaction_cost = fund_share*MutualFund.price
        self.cash_balance -= self.transaction_cost
        self.transaction_history.append('%d shares of ' %fund_share + MutualFund.ticker + ' is bought for $ %d' %self.transaction_cost + ' on ' +Date.today_date())
        print ('Mutual Funds you possess are ', self.my_funds)
    
    def sellMutualFund(self, MutualFund, fund_share, Date):
        self.fund_share -= fund_share
        self.my_funds[MutualFund.ticker] = fund_share
        self.transaction_gain= fund_share*MutualFund.price*uniform(0.9, 1.2)
        self.cash_balance += self.transaction_cost
        self.transaction_history.append('%d shares of ' %fund_share + MutualFund.ticker + ' is sold for $ %d' %self.transaction_gain + ' on ' +Date.today_date())
        print ('Mutual Funds you possess are ', self.my_funds)
    
    def buyBond(self, Bond, bond_amount, Date):
        self.bond_amount += bond_amount
        self.my_bonds[Bond.ticker] = bond_amount
        self.transaction_cost= bond_amount*Bond.price
        self.cash_balance -= self.transaction_cost
        self.cash_balance += Bond.coupon_payment
        self.transaction_history.append('%d shares of ' %bond_amount + Bond.ticker + ' is bought at ' +Bond.exchange+ ' for $ %d' %self.transaction_cost + ' on ' +Date.today_date())
        print ('Bonds you possess are ', self.my_bonds)
    
    def sellBond(self, Bond, bond_amount, Date):
        self.bond_amount -= bond_amount
        self.my_bonds[Bond.ticker] = bond_amount
        self.transaction_gain= bond_amount*Bond.price
        self.cash_balance += self.transaction_gain
        self.transaction_history.append('%d shares of ' %bond_amount + Bond.ticker + ' is sold at ' +Bond.exchange+ ' for $ %d' %self.transaction_cost + ' on ' +Date.today_date())
        print ('Bonds you possess are ', self.my_bonds)
    
    def transactions(self):
        print(self.transaction_history)
    
    def in_cash(self, Stock, MutualFund, Bond):
        total_stock=0
        for key in self.my_stocks.keys():
            total_stock += Stock.price*self.my_stocks[key]*uniform(0.5, 1.5)
        total_fund=0
        for key in self.my_funds.keys():
            total_fund += MutualFund.price*self.my_funds[key]* uniform(0.9, 1.2)
        total_bond=0
        for key in self.my_bonds.keys():
            total_bond += Bond.price*self.my_bonds[key]* uniform(0.95, 1.15)
        self.in_cash= self.cash_balance+total_stock+total_fund+total_bond
        return self.in_cash
    
    def liquidity_check(self):
        if float(self.cash_balance)/float(self.in_cash) < 0.25:
            print('Your liquidity is low, consider to sell some of your stocks or funds in case of need for cash')
        elif 0.25 <= float(self.cash_balance)/float(self.in_cash) < 0.75:
             print('Your liquidity is fine, have fun!')
        else:
            print('You have too much cash, consider to invest it for future gain')
    
    def whats_up(self):
        print(f"""Here is what you have:
              Your cash is ${self.cash_balance}
              Your stocks are {self.my_stocks}
              Your mutual funds are {self.my_funds}
              Your bonds are {self.my_bonds}
              Your assets' current value is ${self.in_cash}
              {self.liquidity_check()}""")


