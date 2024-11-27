from application.batch_processor import BatchProcessor

class BatchController:
    def __init__(self, batch_processor: BatchProcessor):
        self.batch_processor = batch_processor

    def execute_batch(self):
        try:
            self.batch_processor.run()
            print("バッチ処理が完了しました。")
        except Exception as e:
            print(f"エラーが発生しました: {e}")
