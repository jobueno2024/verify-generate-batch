from .bigquery_client import BigQueryClient
from domain.sales_data import SalesData

class BigQueryOutputRepository:
    def __init__(self, client: BigQueryClient):
        self.client = client

    def save_predictions(self, datas: list[SalesData], generated_datas: list[str]):
        for data, generated_data in zip(datas, generated_datas):
            sql = f"INSERT INTO predictions_table (product_id, sales) VALUES ('{data.product_id}', {data.sales}, {generated_data})"
            self.client.query(sql)