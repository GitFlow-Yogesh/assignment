import string
import random
import re
from urllib.parse import urlparse

# In-memory store for short_code → data mapping
url_store = {}

# Character set for short codes
CHARSET = string.ascii_letters + string.digits

def generate_short_code(length=6):
    """Generate a random alphanumeric short code."""
    return ''.join(random.choices(CHARSET, k=length))

def is_valid_url(url):
    """Basic validation for URLs."""
    # Use regex for basic URL structure
    regex = re.compile(
        r'^(https?://)'  # http:// or https://
        r'([\w.-]+)'     # domain
        r'([\w\.-]*)'    # path/query (optional)
        r'/?$',          # trailing slash optional
        re.IGNORECASE
    )
    return re.match(regex, url) is not None

def get_url_data(short_code):
    """Get data associated with a short code."""
    return url_store.get(short_code)

def save_url_mapping(short_code, long_url, timestamp):
    """Save the mapping of short_code → {url, created_at, clicks}."""
    url_store[short_code] = {
        "url": long_url,
        "created_at": timestamp,
        "clicks": 0
    }

def increment_click(short_code):
    """Increment click count for a given short code."""
    if short_code in url_store:
        url_store[short_code]["clicks"] += 1
