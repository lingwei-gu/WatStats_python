from bs4 import BeautifulSoup


class Stats(object):
    def __init__(self, page_source, stats_table):
        self.page_source = page_source
        self.stats_table = stats_table
        self.soup = BeautifulSoup(self.page_source, "lxml")
        self.transactions = []

    # form a list of transactions
    def form_transactions(self):
        raw_transactions = self.soup.find_all('tr')
        raw_transactions.pop(0)  # remove the empty transaction
        for i in raw_transactions:
            temp_transaction = [i.contents[1].contents[0],
                                i.contents[3].contents[0],
                                i.contents[11].contents[0]]
            self.transactions.append(temp_transaction)
        for i in self.transactions:
            print(i)

    # get statistics
    def stats(self):
        for i in self.transactions:
            if "MUDIES" in i[2]:
                self.stats_table["v1_cafe_times"] += 1


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



