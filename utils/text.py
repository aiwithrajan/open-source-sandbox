import re
import unicodedata

def slugify(value: str) -> str:
    """Normalize string, remove non-alpha characters, and convert spaces to hyphens."""
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower()).strip()
    return re.sub(r'[-\s]+', '-', value)

def truncate(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Safely truncate text to max_length with ellipsis."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix
