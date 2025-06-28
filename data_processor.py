import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates  
import os

class DataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    # load the file from the excel
    def load_data(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")

        print(f"📂 Loading Excel file: {self.file_path}")
        
        # Load Excel
        self.data = pd.read_excel(self.file_path)

        # Strip column names
        self.data.columns = [col.strip() for col in self.data.columns]

        print("🔍 Columns found in Excel:", self.data.columns.tolist())

        os.makedirs("assets", exist_ok=True)
        self.clean_data()
        print(f"✅ Data loaded: {self.data.shape}")

     # cleaning of the data
    def clean_data(self):
        self.data.dropna(subset=["CustomerID"], inplace=True)
        self.data = self.data[(self.data['Quantity'] > 0) & (self.data['UnitPrice'] > 0)]
        self.data['InvoiceDate'] = pd.to_datetime(self.data['InvoiceDate'])

    def get_description(self):
        return "This dataset contains online retail transactions for a UK-based retailer between 2010 and 2011."
     
    def get_column_info(self):
        return {
            "InvoiceNo": "Invoice number",
            "StockCode": "Product code",
            "Description": "Product name",
            "Quantity": "Quantity sold per transaction",
            "InvoiceDate": "Date and time of invoice",
            "UnitPrice": "Price per item (GBP)",
            "CustomerID": "Customer ID",
            "Country": "Customer's Country"
        }

    def get_column_types(self):
        return self.data.dtypes.astype(str).to_dict()

    def get_facts(self):
        return [
            f"Total rows after cleaning: {len(self.data)}",
            f"Unique customers: {self.data['CustomerID'].nunique()}"
        ]

    def generate_country_plot(self):
        if "Country" not in self.data.columns:
            raise KeyError("Column 'Country' not found in dataset")
        top = self.data["Country"].value_counts().head(5)
        top.plot(kind="barh", title="Top 5 Countries by Transactions")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("assets/top_countries.png")
        plt.clf()

    def generate_product_revenue_plot(self):
        self.data["Revenue"] = self.data["Quantity"] * self.data["UnitPrice"]
        top = self.data.groupby("Description")["Revenue"].sum().nlargest(5)
        top.plot(kind="bar", title="Top 5 Products by Revenue")
        plt.figure(figsize=(10, 6))
        top.sort_values().plot(kind="barh", color="teal", title="Top 5 Products by Revenue")
        plt.xlabel("Total Revenue")
        plt.ylabel("Product Description")
        plt.grid(axis='x', linestyle='--', alpha=0.3)
        plt.tight_layout()
        plt.savefig("assets/top_products.png")
        plt.clf()

    def generate_monthly_revenue_plot(self):
     self.data["Revenue"] = self.data["Quantity"] * self.data["UnitPrice"]
     self.data["Month"] = self.data["InvoiceDate"].dt.to_period("M")
     trend = self.data.groupby("Month")["Revenue"].sum()
    
    # Convert PeriodIndex to formatted strings (e.g., "Feb 2011")
     trend.index = trend.index.strftime("%b %Y")  # %b = abbreviated month, %Y = full year
    
    # Plot
     ax = trend.plot(title="Monthly Revenue Trend")
    
    # Format x-axis labels
     plt.xticks(rotation=45, ha='right')
     plt.xlabel("Month")  # Explicitly label x-axis
     plt.ylabel("Revenue")  # Explicitly label y-axis
     plt.grid(True, linestyle='--', alpha=0.3)  # Add grid lines
     plt.tight_layout()
     plt.savefig("assets/monthly_revenue.png")
     plt.clf()
     

    def generate_top_customers_plot(self):
        self.data["Revenue"] = self.data["Quantity"] * self.data["UnitPrice"]
        top = self.data.groupby("CustomerID")["Revenue"].sum().nlargest(5)
        top.plot(kind="bar", title="Top 5 Customers by Revenue")
        plt.tight_layout()
        plt.savefig("assets/top_customers.png")
        plt.clf()

    def generate_unit_price_dist_plot(self):
        self.data["UnitPrice"].plot(kind="hist", bins=50, title="Unit Price Distribution")
        plt.tight_layout()
        plt.savefig("assets/unit_price_dist.png")
        plt.clf()

    def generate_weekday_pattern_plot(self):
        self.data["Weekday"] = self.data["InvoiceDate"].dt.day_name()
        orders = self.data["Weekday"].value_counts()
        orders = orders.reindex([
            "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
        ], fill_value=0)
        orders.plot(kind="bar", title="Orders by Weekday")
        plt.tight_layout()
        plt.savefig("assets/weekday_orders.png")
        plt.clf()
