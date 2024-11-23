import wbdata
import datetime

# Setting up the indicators for querying the World Bank data
indicators = {
    'NY.GDP.MKTP.CD': 'GDP (current US$)',
    'NY.GDP.PCAP.CD': 'GDP per capita (current US$)',
    'FP.CPI.TOTL.ZG': 'Inflation, consumer prices (annual %)'
}

# Querying the data from the World Bank
data_date = (datetime.datetime(2023, 1, 1), datetime.datetime(2023, 12, 31))
df = wbdata.get_dataframe(indicators, data_date=data_date, convert_date=False)

# Printing the results
print("World Finance Overview 2023:")
print(df.describe())


