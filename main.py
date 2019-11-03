from scrape import Scrape
from stats import Stats
stats_list = ["remaining_residence_plan_balance", "v1_cafe_times",
              "meal_expense_60days", "average_meal_expense_60days",
              "missed breakfasts and lunches"]
stats_table = {}
for i in range(len(stats_list)):
    stats_table.update({stats_list[i]: 0})

data = Scrape("id", "pin")

sources = []
sources = data.scrape()

records = Stats(sources[0], sources[1], stats_table)
records.form_transactions()
records.get_residence_plan_balance()
records.stats()
print(stats_table)
# print(pageSource)









