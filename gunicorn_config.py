"""
Configuration for gunicorn
"""

from migration_db import init_pg


def when_ready(server):
    """
    Function ready gunicorn
    """
    server.log.info("Server is ready")
    init_pg(server)
