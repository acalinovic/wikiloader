from uuid import uuid4, UUID

import pandas as pd

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
