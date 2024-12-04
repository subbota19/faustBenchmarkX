from faust import Record
from datetime import datetime


class BenchmarkMessage(Record, serializer='json', isodates=True):
    id: int
    type: str
    message: str
    datetime: datetime
    process_id: int
