

def read_file(name: str, strip=True):
    with open(f"resources/{name}") as f:
        content = f.readlines()
    if strip:
        return [x.strip() for x in content]
    return content
