from scrape import Scrape
from stats import Stats
stats_list = ["v1_cafe_times", "meal_expense_60days"]
stats_table = {}
for i in range(len(stats_list)):
    stats_table.update({stats_list[i]: 0})

data = Scrape("id", "pin")

pageSource = data.scrape()

records = Stats(pageSource, stats_table)
records.form_transactions()
records.stats()
print(stats_table)
# print(pageSource)
