import pandas as pd

path = input('CSV path: ')
df = pd.read_csv(path)
print('Tasks')
tasks = ['1. Print CSV',
         '2. Parse date into a consistent datetime format (handle multiple formats)',
         '3. Convert amount from string currency to float',
         '4. Convert quantity to integer',
         '5. Convert discount from percentage string to float',
         '6. Compute a new column net_amount = amount × (1 − discount)',
         '7. Exit']
for item in tasks:
    print(item)
print('-' * 8)
while True:
    task = input('Select task: ')
    if task == '1':
        choice = input('(f) full or (t) truncated: ')
        if choice == 'f':
            print(df.to_string())
            print('-' * 8)
        elif choice == 't':
            print(df)
            print('-' * 8)
        else:
            print('Invalid input')
    elif task == '2':
        df['date'] = pd.to_datetime(df['date'])
        print('Task complete')
        print('-' * 8)
    elif task == '3':
        df['amount'] = df['amount'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
        print('Task complete')
        print('-' * 8)
    elif task == '4':
        df['quantity'] = df['quantity'].astype(int)
        print('Task complete')
        print('-' * 8)
    elif task == '5':
        df['discount'] = df['discount'].str.replace('%', '', regex=False).astype(int) / 100
        print('Task complete')
        print('-' * 8)
    elif task == '6':
        if df['discount'].dtype == 'float64' and df['amount'].dtype == 'float64':
            df['net_amount'] = df['amount'] * (1 - df['discount'])
            print('Task complete')
            print('-' * 8)
        else:
            print('Convert amount and discount to float first')
            print('-' * 8)
    elif task == '7':
        print('Program closed')
        break
    else:
        print('Invalid input')
