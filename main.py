import faust
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = faust.App(
    'benchmark_fault',
    broker='kafka://192.168.49.2:30000',
    store='memory://',
)

benchmark_topic = app.topic('benchmark_fault', value_type=str)


@app.agent(benchmark_topic)
async def process(stream):
    async for event in stream:
        logger.info(f"Received message: {event}")


if __name__ == '__main__':
    app.main()
