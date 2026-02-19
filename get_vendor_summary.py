import sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

def create_vendor_summary(con):
    '''This function will merge the different tables to get the overall vendor summary and adding new column in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary AS(
    Select 
        VendorNumber, sum(Freight) as FreightCost 
    from vendor_invoice
    group by VendorNumber
),
                        
PurchaseSummary AS (
    SELECT 
        p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice,
        pp.Price as ActualPrice, pp.Volume,
        sum(p.Quantity) as TotalPurchaseQuantity,
        sum(p.Dollars) as TotalPurchaseDollars
        from purchases p
        join purchase_prices pp
        using(Brand)
        where p.PurchasePrice>0
        group by p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice,
        pp.Price, pp.Volume
),
                
SalesSummary AS(
    Select VendorNo, Brand, sum(SalesDollars) as TotalSalesDollars,
                  sum(SalesPrice) as TotalSalesPrice,
                  sum(SalesQuantity) as TotalSalesQuantity,
                  sum(ExciseTax) as TotalExciseTax
                  from sales
                  group by VendorNo, Brand
)
                                         
Select ps.VendorNumber, ps.VendorName, ps.Brand, ps.Description, ps.PurchasePrice,
        ps.ActualPrice, ps.Volume, ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars, ss.TotalSalesQuantity, ss.TotalSalesDollars,
        ss.TotalSalesPrice, ss.TotalExciseTax, fs.FreightCost
    from PurchaseSummary ps
    left join SalesSummary as ss
    on ps.VendorNumber = ss.VendorNo
    and ps.Brand = ss.Brand
    left join FreightSummary fs
    on ps.VendorNumber = fs.VendorNumber
    order by ps.TotalPurchaseDollars Desc""",con)

    return vendor_sales_summary


def clean_data(df):
    '''This function will clean the data'''
    # changing datatype to float
    df['Volume'] = df['Volume'].astype('float')

    # filling missing value with 0
    df.fillna(0,inplace=True)

    # removing spaces from categorical columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df['Description'].str.strip()

    # creating new columns for better analysis
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = (df['GrossProfit']/df['TotalSalesDollars'])*100
    df['StockTurnOver'] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']
    df['SalesToPurchaseRatio'] = df['TotalSalesDollars']/df['TotalPurchaseDollars']

    return df

if __name__ == '__main__':
    # creating database connection
    con = sqlite3.connect('inventory.db')
    
    logging.info('Creating vendor Summary Tabel.....')
    summary_df = create_vendor_summary(con)
    logging.info(summary_df.head())

    logging.info('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingestion data.....')
    ingest_db(clean_df,'vendor_sales_summary',con)
    logging.info('Completed')


