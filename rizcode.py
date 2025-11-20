
import pandas as pd
import os
import tabulate
data_akun = pd.read_csv('Agrocare/users.csv')
print(tabulate.tabulate(data_akun, headers='keys', tablefmt='fancy_grid'))
