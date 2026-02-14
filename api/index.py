"""
Vercel serverless function entry point.

Exposes the Flask WSGI app so Vercel's Python runtime can serve it.
"""

from .orchestrator import app
