from uuid import uuid4


def generate_slug() -> str:
    slug = str(uuid4()).replace("-", "")
    return slug[:10]
