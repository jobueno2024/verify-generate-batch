from domain.gpt4_service import GPT4Service
from infrastructure.bigquery.bigquery_input_repository import BigQueryInputRepository
from infrastructure.bigquery.bigquery_output_repository import BigQueryOutputRepository

class BatchProcessor:
    def __init__(self, input_repository: BigQueryInputRepository, gpt4_service: GPT4Service, output_repository: BigQueryOutputRepository):
        self.input_repository = input_repository
        self.gpt4_service = gpt4_service
        self.output_repository = output_repository

    def run(self):
        data = self.input_repository.get_sales_data()
        generated_data = self.gpt4_service.generate_data(data)
        self.output_repository.save_predictions(data, generated_data)
