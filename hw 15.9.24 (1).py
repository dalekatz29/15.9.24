# START
import random

variables = {}
for i in range(4):
    player_name = input("enter player name: ")
    variables[f'var_{i}'] = player_name

print(random.choice([variables['var_0'], variables['var_1'], variables['var_2'], variables['var_3']]))

# END
