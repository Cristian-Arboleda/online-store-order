import polars as pl

database = pl.read_excel('Online-Store-Orders.xlsx').fill_null('null')

# ------------------------------------------------------------------------------------------------------------------
# Unique values

filter_column = ['Date', 'PaymentMethod', 'OrderStatus', 'CouponCode', 'ReferralSource']

unique_filters = {
    column : database[column].unique().to_list()
    if column !=  "Date" else
    database[column].dt.year().unique().sort().to_list()
    for column in filter_column
}
