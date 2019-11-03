from bs4 import BeautifulSoup


class Stats(object):
    def __init__(self, transaction_source, balance_source, stats_table):
        self.transaction_source = transaction_source
        self.balance_source = balance_source
        self.stats_table = stats_table
        self.transaction_soup = BeautifulSoup(self.transaction_source, "lxml")
        self.balance_soup = BeautifulSoup(self.balance_source, "lxml")
        self.transactions = []

    # form a list of transactions
    def form_transactions(self):
        raw_transactions = self.transaction_soup.find_all('tr')
        raw_transactions.pop(0)  # remove the empty transaction
        for i in raw_transactions:
            temp_transaction = [i.contents[1].contents[0],
                                i.contents[3].contents[0],
                                i.contents[11].contents[0]]
            self.transactions.append(temp_transaction)
        for i in self.transactions:
            print(i)

    def get_residence_plan_balance(self):
        balances = self.balance_soup.find('td', text="RESIDENCE PLAN").parent.find_all('td')
        self.stats_table["remaining_residence_plan_balance"] = float(balances[3].text[1:])

    # get statistics
    def stats(self):
        breakfast_lunch = [0, 0]
        for i in self.transactions:
            if "MUDIES" in i[2]:
                self.stats_table["v1_cafe_times"] += 1
            if "FS-" in i[2] and "-" in i[1]:
                self.stats_table["meal_expense_60days"] += (float(i[1][2:]))
            if "FS-" in i[2]:
                if "AM" in i[0] and len(i[0]) == 21 \
                        and 7 <= int(i[0][11:12]) < 10 and int(i[0][13:15]) <= 59:
                    breakfast_lunch[0] += 1
                if "AM" in i[0] and len(i[0]) == 22 and 10 <= int(i[0][11:13]) < 12:
                    breakfast_lunch[1] += 1
                if "PM" in i[0] and len(i[0]) == 21 and int(i[0][11:12]) <= 3:
                    breakfast_lunch[1] += 1
        self.stats_table["meal_expense_60days"] = \
            round(self.stats_table["meal_expense_60days"], 2)
        self.stats_table["average_meal_expense_60days"] = \
            round(self.stats_table["meal_expense_60days"]/60, 2)
        missed_breaklun = [60 - breakfast_lunch[0], 60 - breakfast_lunch[1]]
        self.stats_table["missed breakfasts and lunches"] = missed_breaklun


"""
Transaction format from beautifulsoap
['\n',
 <td data-title="Date:">09/27/2019 6:31:34 PM</td>, 
 '\n', 
 <td class="ow-align-right" data-title="Amount:">-$2.95</td>, 
 '\n', 
 <td data-title="Balance:">1</td>, 
 '\n',
  <td data-title="Units:">0</td>, 
  '\n', 
  <td data-title="Trantype:">104 : FINANCIAL VEND                          </td>, 
  '\n', 
  <td data-title="Terminal:">00033 : FS-V1 MUDIES-36               </td>, 
  '\n']
"""



