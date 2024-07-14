
#місце для твого коду
import pandas as pd

df = pd.read_csv('investments_VC.csv')

df = df.drop(['permalink','homepage_url','state_code','category_list'],axis=1)


def cleancolumn(price):
    if price.strip() == '-':
        price = 0

    else:
        price= price.replace(',','')
        price = int(price)
    return price

def name_clean(name):
    name = str(name)
  
    if name.find('.com'):
        name.replace('.com','')
    



df['funding_total_usd'] = df['funding_total_usd'].apply(cleancolumn)


df = df.dropna()
df.info()

print(df['product_crowdfunding'].value_counts())
df.to_csv('InvestmentCleaned.csv')