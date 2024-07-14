
#місце для твого коду
import pandas as pd

df = pd.read_csv('investments_VC.csv')

df = df.drop(['permalink','homepage_url','state_code'],axis=1)


def cleancolumn(price):
    if price.strip() == '-':
        price = 0

    else:
        price= price.replace(',','')
        price = int(price)
    return price

def cleancategory(category):

    if isinstance(category,str):
            category = category.split('|')
            category = category[0].replace('|','')
    return category




df['funding_total_usd'] = df['funding_total_usd'].apply(cleancolumn)
    
df['category'] = df['category_list'].apply(cleancategory)

df.info()

print(df['product_crowdfunding'].value_counts())
df.to_csv('InvestmentCleaned.csv')