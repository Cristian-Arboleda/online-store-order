import polars as pl

data = pl.read_excel('Online-Store-Orders.xlsx')

# ------------------------------------------------------------------------------------------------------------------
# Unique values
years = data.select(
    pl.col('Date').dt.year().unique().sort()
)

products = data['Product'].unique()

Paymentmethod = data['PaymentMethod'].unique()

orderstatus = data['OrderStatus'].unique()

referralsource = data['ReferralSource'].unique()