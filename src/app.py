from json import dumps
from logging import INFO, basicConfig, getLogger

from faust import App

from .benchmark.models import BenchmarkMessage
from .utils.s3 import (
    bucket_exists,
    create_bucket,
    create_s3_client,
    upload_object,
)

BUFFER_MESSAGE_COUNT = 100
BUFFER_PERIOD = 60
BUCKET_NAME = "faust"
ENCODING = "utf-8"

basicConfig(level=INFO)
logger = getLogger(__name__)

app = App(
    "benchmark_fault",
    broker="kafka://192.168.49.2:30000",
    store="memory://",
)

benchmark_topic = app.topic("benchmark_fault", value_type=BenchmarkMessage)


@app.agent(benchmark_topic)
async def process(stream):
    s3_client = create_s3_client(
        endpoint_url="http://localhost:9000",
        access_key="ADMIN",
        secret_key="12345678",
    )

    if not bucket_exists(s3_client, BUCKET_NAME):
        create_bucket(s3_client, BUCKET_NAME)

    async for batch in stream.take(
            max_=BUFFER_MESSAGE_COUNT, within=BUFFER_PERIOD
    ):

        logger.info("Batch is initialized.")
        for event in batch:
            event_data = dumps(
                {
                    "id": event.id,
                    "type": event.type,
                    "message": event.message,
                    "datetime": event.datetime.isoformat(),
                    "process_id": event.process_id,
                    "client_id": event.client_id,
                }
            ).encode(ENCODING)

            blob_key = (
                f"client_id={event.client_id}/"
                f"key={event.id}_{event.datetime.isoformat()}.json"
            )

            upload_object(s3_client, BUCKET_NAME, blob_key, event_data)


def main() -> None:
    app.main()
