from faust import App
from logging import basicConfig, getLogger, INFO
from .benchmark.models import BenchmarkMessage
from .utils.s3 import (
    create_s3_client,
    create_bucket,
    bucket_exists,
    upload_object
)

BUFFER_MESSAGE_COUNT = 100
BUFFER_PERIOD = 60

basicConfig(level=INFO)
logger = getLogger(__name__)

app = App(
    'benchmark_fault',
    broker='kafka://192.168.49.2:30000',
    store='memory://',
)

benchmark_topic = app.topic('benchmark_fault', value_type=BenchmarkMessage)


def output_sink(value):
    yield f'AGENT YIELD: {value!r}'


@app.agent(benchmark_topic)
async def process(stream):
    async for batch in stream.take(max_=BUFFER_MESSAGE_COUNT, within=BUFFER_PERIOD):
        s3_client = create_s3_client(
            endpoint_url='http://localhost:9000',
            access_key='ADMIN',
            secret_key='ADMINADMIN'
        )

        bucket_name = "faust"

        if not bucket_exists(s3_client, bucket_name):
            create_bucket(s3_client, bucket_name)

        logger.info("Batch is initialized.")
        for event in batch:
            logger.info(f"Received message: {event}")
            upload_object(
                s3_client,
                bucket_name,
                str(event.id),
                "Test Message"
            )


def main() -> None:
    app.main()
