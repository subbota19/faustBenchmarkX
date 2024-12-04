import faust
import logging

from src.benchmark.models import BenchmarkMessage

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BUFFER_MESSAGE_COUNT = 100
BUFFER_PERIOD = 10

app = faust.App(
    'benchmark_fault',
    broker='kafka://192.168.49.2:30000',
    store='memory://',
)

benchmark_topic = app.topic('benchmark_fault', value_type=BenchmarkMessage)


@app.agent(benchmark_topic)
async def process(stream):
    async for event in stream:
        logger.info(f"Received message: {event}")


@app.agent(benchmark_topic)
async def process_v2(stream):
    async for batch in stream.take(max_=BUFFER_MESSAGE_COUNT, within=BUFFER_PERIOD):
        for event in batch:
            logger.info(f"Received message: {event}")


if __name__ == '__main__':
    app.main()
