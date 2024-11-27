from .bigquery_client import BigQueryClient
from domain.sales_data import SalesData

class BigQueryInputRepository:

    def __init__(self, client: BigQueryClient):
        self.client = client

    def get_sales_data(self) -> list[SalesData]:
        results = self.client.query("SELECT product_id, sales FROM sales_table")
        return [SalesData(row['product_id'], row['sales']) for row in results]