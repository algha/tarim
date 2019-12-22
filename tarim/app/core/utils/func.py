from ..template.asset import Asset

def to_string(data):
    if isinstance(data, str):
        return data
    return str(data)
