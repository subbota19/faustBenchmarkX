from faust import App
from logging import basicConfig, getLogger, INFO

basicConfig(level=INFO)
logger = getLogger(__name__)

app = App(
    'benchmark_fault',
    broker='kafka://192.168.49.2:30000',
    store='memory://',
)

benchmark_topic = app.topic('benchmark_fault', value_type=str)


@app.agent(benchmark_topic)
async def process(stream):
    async for event in stream:
        logger.info(f"Received message: {event}")


def main() -> None:
    app.main()
