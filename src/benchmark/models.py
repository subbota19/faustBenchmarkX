from datetime import datetime

from faust import Record


class BenchmarkMessage(Record, serializer="json", isodates=True):
    id: int
    type: str
    message: str
    datetime: datetime
    process_id: int
    client_id: int
