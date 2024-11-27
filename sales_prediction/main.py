from presentation.api import BatchController
from application.batch_processor import BatchProcessor
from domain.gpt4_service import GPT4Service
from infrastructure.bigquery.bigquery_input_repository import BigQueryInputRepository
from infrastructure.bigquery.bigquery_output_repository import BigQueryOutputRepository
from infrastructure.bigquery.bigquery_client import BigQueryClient
from infrastructure.gpt4_client import GPT4Client

def main():
    # Initialize dependencies
    bigquery_client = BigQueryClient()
    gpt4_client = GPT4Client()

    input_repository = BigQueryInputRepository(bigquery_client)
    output_repository = BigQueryOutputRepository(bigquery_client)
    gpt4_service = GPT4Service(gpt4_client)
    batch_processor = BatchProcessor(input_repository, gpt4_service, output_repository)
    batch_controller = BatchController(batch_processor)

    # Execute batch process
    batch_controller.execute_batch()

if __name__ == "__main__":
    main()
