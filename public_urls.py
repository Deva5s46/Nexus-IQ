"""Public base URLs for admin and client apps (e.g. Railway). Set in .env — no trailing slash."""
import os
from urllib.parse import urlparse


def _normalize_base(url):
    if not url or not isinstance(url, str):
        return ""
    s = url.strip().rstrip("/")
    if not s:
        return ""
    p = urlparse(s)
    if p.scheme not in ("http", "https") or not p.netloc:
        return ""
    return s


def get_client_public_base_url():
    return _normalize_base(os.getenv("CLIENT_PUBLIC_BASE_URL", ""))


def get_admin_public_base_url():
    return _normalize_base(os.getenv("ADMIN_PUBLIC_BASE_URL", ""))


def join_public_base(base, path):
    """Join base URL with a path starting with /."""
    if not base:
        return ""
    p = path or "/"
    if not p.startswith("/"):
        p = "/" + p
    return base + p
