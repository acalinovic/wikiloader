import pandas as pd
from uuid import uuid4, UUID

_registry = pd.DataFrame(
    columns=[
        "uuid",
        "label",
        "type",
        "content"
    ])


def generate_uuid() -> UUID:
    return uuid4()


def register_file():
    pass
