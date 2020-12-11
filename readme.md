# FMP SDK
The idea behind this project is to provide a 'one-stop-shop' to the API endpoints provided by 
[Financial Model Prep](http://financialmodelingprep.com) website.

## Breaking Change Update!!!
Use version 20201208.5 or larger!

I know this project is brand new, but I've decided to "flatten" the structure.  Instead of using a Class object with 
methods inside it for each API endpoint I decided to just have regular methods.  So, instead of instantiating an 
"FMP" object you can just call each method directly.  The only main "con" to this new methodology is that you have 
to pass the 'apikey' and 'symbol' (when needed) to each method.  I felt the tradeoff was worth it though.

## Example code
Most of these methods will return a dictionary.  It is up to you to parse out the information you are looking for.
```python
#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import fmpsdk

# Actual API key is stored in a .env file.  Not good to store API key directly in script.
load_dotenv()
apikey = os.environ.get("apikey")
symbol = "AAPL"

# Company Valuation Methods
print(f"Company Profile: {fmpsdk.company_profile(apikey=apikey, symbol=symbol)}")
print(f"Company Quote: {fmpsdk.company_quote(apikey=apikey, symbol=symbol)}")
print(f"Multiple Company Quotes: {fmpsdk.company_quote(apikey=apikey, symbol=['AAPL', 'CSCO', 'QQQQ'])}")
print(f"Key Executives: {fmpsdk.key_executives(apikey=apikey, symbol=symbol)}")
print(f"Search: {fmpsdk.search(apikey=apikey, query='AA', exchange='NYSE', limit=10)}")
print(f"Ticker Search: {fmpsdk.search_ticker(apikey=apikey, query='AA', exchange='NYSE', limit=5)}")
fmpsdk.financial_statement(apikey=apikey, symbol=symbol)
print(f"Annual Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Income Statement: {fmpsdk.income_statement(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.income_statement(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Balance Sheet Statement: {fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.balance_sheet_statement(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, )}")
print(f"Quarterly Cash Flow Statement: {fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.cash_flow_statement(apikey=apikey, symbol=symbol, download=True)
print(f"Financial Statement Symbols List: {fmpsdk.financial_statement_symbol_lists(apikey=apikey)}")
print(f"Income Statement Growth: {fmpsdk.income_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Balance Sheet Statement Growth: {fmpsdk.balance_sheet_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Cash Flow Statement Growth: {fmpsdk.cash_flow_statement_growth(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Annual Income Statement as Reported : {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Income Statement as Reported: {fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.income_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Balance Sheet Statement as Reported : {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Balance Sheet Statement as Reported: {fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.balance_sheet_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Cash Flow Statement as Reported : {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Cash Flow Statement as Reported: {fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
fmpsdk.cash_flow_statement_as_reported(apikey=apikey, symbol=symbol, download=True)
print(f"Annual Full Financial Statement as Reported : {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Full Financial Statement as Reported: {fmpsdk.financial_statement_full_as_reported(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Financial Ratios (TTM): {fmpsdk.financial_ratios_ttm(apikey=apikey, symbol=symbol)}")
print(f"Annual Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='annual')}")
print(f"Quarterly Financial Ratios: {fmpsdk.financial_ratios(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Annual Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol)}")
print(f"Quarterly Enterprise Values: {fmpsdk.enterprise_values(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Key Metrics (TTM): {fmpsdk.key_metrics_ttm(apikey=apikey, symbol=symbol)}")
print(f"Annual Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period='annual')}")
print(f"Quarterly Key Metrics: {fmpsdk.key_metrics(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Annual Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol, period='annual')}")
print(f"Quarterly Financial Growth: {fmpsdk.financial_growth(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Company Rating: {fmpsdk.rating(apikey=apikey, symbol=symbol)}")
print(f"Historical Company Rating: {fmpsdk.historical_rating(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Discounted Cash Flow: {fmpsdk.discounted_cash_flow(apikey=apikey, symbol=symbol)}")
print(f"Annual Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol, period='annual')}")
print(f"Quarterly Historical Discounted Cash Flow: {fmpsdk.historical_discounted_cash_flow(apikey=apikey, symbol=symbol, period='quarter')}")
print(f"Daily Historical Discounted Cash Flow: {fmpsdk.historical_daily_discounted_cash_flow(apikey=apikey, symbol=symbol)}")
print(f"Market Capitalization: {fmpsdk.market_capitalization(apikey=apikey, symbol=symbol)}")
print(f"Historical Market Capitalization: {fmpsdk.historical_market_capitalization(apikey=apikey, symbol=symbol, limit=10)}")
print(f"Symbols List: {fmpsdk.symbols_list(apikey=apikey)}")
print(f"Stock Screener: {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=1000000000, beta_more_than=1, volume_more_than=10000, sector='Technology', exchange='NASDAQ', dividend_more_than=0, limit=100)}")
print(f"Stock Screener (Industry Example): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=1000000000, beta_more_than=1, volume_more_than=10000, sector='Technology', industry='Software', exchange='NASDAQ', dividend_more_than=0, limit=100)}")
print(f"Stock Screener (Multiple Exchanges Example): {fmpsdk.stock_screener(apikey=apikey, market_cap_more_than=10000000000, beta_more_than=1, volume_more_than=100, exchange=['NYSE', 'NASDAQ'])}")
print(f"Delisted Companies: {fmpsdk.delisted_companies(apikey=apikey, limit=10)}")
print(f"Stock News (Single): {fmpsdk.stock_news(apikey=apikey, tickers=symbol)}")
print(f"Stock News (Multiple): {fmpsdk.stock_news(apikey=apikey, tickers=['AAPL', 'CSCO', 'QQQQ'])}")
print(f"Stock News (Latest): {fmpsdk.stock_news(apikey=apikey, limit=10)}")
print(f"Earnings Surprises: {fmpsdk.earnings_surprises(apikey=apikey, symbol=symbol)}")
print(f"SEC Filings: {fmpsdk.sec_filings(apikey=apikey, symbol=symbol, filing_type='10-K')}")
print(f"Press Releases: {fmpsdk.press_releases(apikey=apikey, symbol=symbol)}")

# Calendars
print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey)}")
print(f"Earning Calendar: {fmpsdk.earning_calendar(apikey=apikey, from_date='2000-06-23', to_date='2010-12-12')}")
print(f"Historical Earning Calendar: {fmpsdk.historical_earning_calendar(apikey=apikey, symbol=symbol, limit=25)}")
print(f"IPO Calendar: {fmpsdk.ipo_calendar(apikey=apikey, from_date='2000-06-23', to_date='2010-12-12')}")
print(f"Stock Split Calendar: {fmpsdk.stock_split_calendar(apikey=apikey, from_date='2000-06-23', to_date='2010-12-12')}")
print(f"Dividend Calendar: {fmpsdk.dividend_calendar(apikey=apikey, from_date='2000-06-23', to_date='2010-12-12')}")
print(f"Economic Calendar: {fmpsdk.economic_calendar(apikey=apikey, from_date='2020-09-23', to_date='2020-12-12')}")

# Institutional Fund
print(f"Institutional Holders: {fmpsdk.institutional_holders(apikey=apikey, symbol=symbol)}")
print(f"Mutual Fund Holders: {fmpsdk.mutual_fund_holders(apikey=apikey, symbol=symbol)}")
print(f"ETF Holders: {fmpsdk.etf_holders(apikey=apikey, symbol='SPY')}")
print(f"ETF Sector Weightings: {fmpsdk.etf_sector_weightings(apikey=apikey, symbol='SPY')}")
print(f"ETF Country Weightings: {fmpsdk.etf_country_weightings(apikey=apikey, symbol='SPY')}")
print(f"SEC RSS Feeds: {fmpsdk.sec_rss_feeds(apikey=apikey)}")
print(f"SEC RSS Feeds: {fmpsdk.sec_rss_feeds(apikey=apikey, download=True)}")
print(f"Form 13F List: {fmpsdk.cik_list(apikey=apikey)}")
print(f"CIK Search by Company Name: {fmpsdk.cik_search(apikey=apikey, name='Berkshire')}")
print(f"CIK Search by CIK: {fmpsdk.cik(apikey=apikey, cik_id='0000913760')}")
print(f"Form 13F: {fmpsdk.form_13f(apikey=apikey, cik_id='0000913760', date='2020-06-30')}")
print(f"CUSIP: {fmpsdk.cusip(apikey=apikey, cik_id='000360206')}")

# Stock Time Series Methods
print(f"Quote Realtime: {fmpsdk.quote_short(apikey=apikey, symbol=symbol)}")
print(f"Exchange Realtime: {fmpsdk.exchange_realtime(apikey=apikey, exchange='NYSE')}")
print(f"Historical Stock Prices: {fmpsdk.historical_stock_price(apikey=apikey, symbol=symbol, time_delta='5min')}")
print(f"Historical Daily Prices: {fmpsdk.historical_stock_price_full(apikey=apikey, symbol=symbol, series_type='line')}")
print(f"Historical Daily Prices with Change and Volume: {fmpsdk.historical_stock_price_full(apikey=apikey, symbol=symbol)}")
print(f"Historical Daily Prices with Change and Volume (Interval): {fmpsdk.historical_stock_price_full(apikey=apikey, symbol=symbol, from_date='2020-12-01', to_date='2020-12-09')}")
print(f"Historical Daily Prices with Change and Volume (Time Series): {fmpsdk.historical_stock_price_full(apikey=apikey, symbol=symbol, time_series=5)}")
print(f"Historical Daily Prices (Batch Stocks): {fmpsdk.historical_stock_price_full(apikey=apikey, symbol=['AAPL', 'CSCO', 'MSFT'])}")
print(f"Historical Daily Prices (Batch Mutual Funds): {fmpsdk.historical_stock_price_full(apikey=apikey, symbol=['JBFRX','BPLEX','VEVRX'])}")
print(f"Historical Dividends: {fmpsdk.historical_stock_dividend(apikey=apikey, symbol=symbol)}")
print(f"Historical Stock Split: {fmpsdk.historical_stock_split(apikey=apikey, symbol=symbol)}")

# Technical Indicators
print(f"Daily Technical Indicators: {fmpsdk.technical_indicators(apikey=apikey, symbol=symbol, period=10, statistics_type='sma', time_delta='daily')}")
print(f"Intraday Technical Indicators: {fmpsdk.technical_indicators(apikey=apikey, symbol=symbol, period=10, statistics_type='sma', time_delta='15min')}")

# Market Indexes
print(f"List Market Indexes: {fmpsdk.indexes(apikey=apikey)}")
print(f"Index: {fmpsdk.index_quote(apikey=apikey, index='IMOEX.ME')}")
print(f"SP500 Contituent: {fmpsdk.sp500_constituent(apikey=apikey)}")
fmpsdk.sp500_constituent(apikey=apikey, download=True)
print(f"Historical SP500 Contituent: {fmpsdk.historical_sp500_constituent(apikey=apikey)}")
print(f"NASDAQ Contituent: {fmpsdk.nasdaq_constituent(apikey=apikey)}")
fmpsdk.nasdaq_constituent(apikey=apikey, download=True)
print(f"Historical NASDAQ Contituent: {fmpsdk.historical_nasdaq_constituent(apikey=apikey)}")
print(f"DOWJONES Contituent: {fmpsdk.dowjones_constituent(apikey=apikey)}")
fmpsdk.dowjones_constituent(apikey=apikey, download=True)
print(f"Historical DOWJONES Contituent: {fmpsdk.historical_dowjones_constituent(apikey=apikey)}")
print(f"Available Indexes: {fmpsdk.available_indexes(apikey=apikey)}")
print(f"Intraday Historical Stock Prices: {fmpsdk.historical_index(apikey=apikey, index='^SSEC', time_delta='15min')}")
print(f"Historical Market Index: {fmpsdk.historical_index_full(apikey=apikey, index='^VIX')}")

# Commodities
print(f"Available Commodities': {fmpsdk.available_commodities(apikey=apikey)}")
print(f"Commodities': {fmpsdk.commodities_list(apikey=apikey)}")
print(f"Commodity Quote': {fmpsdk.commodity_quote(apikey=apikey, symbol=['ZGUSD', 'CLUSD', 'HGUSD'])}")
print(f"Historical Commodity Prices: {fmpsdk.historical_stock_price(apikey=apikey, symbol='ZGUSD', time_delta='5min')}")
print(f"Historical Daily Commodity Prices: {fmpsdk.historical_stock_price_full(apikey=apikey, symbol='ZGUSD')}")

# ETF
```
