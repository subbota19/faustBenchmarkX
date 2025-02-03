# faustBenchmarkX

This project demonstrates how to use the Faust framework to process Kafka messages and store them in S3-compatible storage (in my case MinIO). The goal is to test how Faust can handle Kafka messages under load while leveraging buffering techniques.

While I did not run this in production, my experiment showed that Faust can efficiently handle such workloads for simpler setups, particularly when Python is preferred. Although Faust lacks built-in aggregation support and is not as widely used as other stream processing frameworks, it can still be suitable for basic stream processing needs.

Please refer to [repo](https://github.com/subbota19/msgGeneratorKafka) for more info about generating Kafka messages and [repo](https://github.com/subbota19/kafkaInfra) for Kafka setup.

# Run Worker

python -m src worker -l info

