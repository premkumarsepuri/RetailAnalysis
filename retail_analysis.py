from abstract_base import BaseAnalysis
from data_processor import DataProcessor
from report_generator import ReportGenerator

class Analysis(BaseAnalysis):
    def __init__(self, level, file_path):
        print(file_path)
        self.level = level
        self.dp = DataProcessor(file_path)
        self.rg = ReportGenerator(level)


    def run_analysis(self):
        print(f"Running analysis for {self.level}")
        self.dp.load_data()
        self.rg.add_title()

        # Level-1
        self.rg.add_paragraph(self.dp.get_description())
        self.rg.add_table(self.dp.get_column_info())
        self.rg.add_paragraph("Column Data Types:")
        for col, dtype in self.dp.get_column_types().items():
            self.rg.add_paragraph(f"{col}: {dtype}")
        for fact in self.dp.get_facts():
            self.rg.add_paragraph(fact)

        # Level-2
        if self.level in ["LEVEL-2", "LEVEL-3"]:
             self.dp.load_data()
             self.dp.generate_country_plot()
             self.rg.add_paragraph("Top 5 Countries by Transactions:")
             self.rg.add_image("assets/top_countries.png")

             self.dp.generate_product_revenue_plot()
             self.rg.add_paragraph("Top 5 Products by Revenue:")
             self.rg.add_image("assets/top_products.png")

             self.dp.generate_monthly_revenue_plot()
             self.rg.add_paragraph("Monthly Revenue Trend:")
             self.rg.add_image("assets/monthly_revenue.png")

        # Level-3
        if self.level == "LEVEL-3":
            self.dp.generate_top_customers_plot()
            self.rg.add_paragraph("Top 5 Customers by Revenue:")
            self.rg.add_image("assets/top_customers.png")

            self.dp.generate_unit_price_dist_plot()
            self.rg.add_paragraph("Unit Price Distribution:")
            self.rg.add_image("assets/unit_price_dist.png")

            self.dp.generate_weekday_pattern_plot()
            self.rg.add_paragraph("Orders by Weekday:")
            self.rg.add_image("assets/weekday_orders.png")

        self.rg.save_pdf()
        print(f"✅ PDF generated: {self.rg.filename}")
        
