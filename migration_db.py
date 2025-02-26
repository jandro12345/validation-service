"""
Init schema database pg
"""

from os import getenv, walk, path

from dotenv import load_dotenv
from natsort import natsorted
from psycopg2 import connect, errors
from psycopg2.extensions import connection, cursor

load_dotenv()


def get_pg_connection() -> tuple[connection, cursor]:
    """
    Get pg connection and cursor
    """
    conn_ = connect(
        f"""
    dbname={getenv('PG_DB', '')}
    user={getenv('PG_USER', '')}
    password={getenv('PG_PASS', '')}
    host={getenv('PG_HOST', '')}
    port={getenv('PG_PORT', '')}
    """
    )
    cursor_ = conn_.cursor()
    return (conn_, cursor_)


def verify_file_pg(filename: str) -> bool:
    """
    Verify if file was executed
    """
    conn_, cursor_ = get_pg_connection()
    cursor_.execute("SELECT * FROM tbl_migration WHERE file_name=%s", (filename,))
    rows = cursor_.fetchall()
    conn_.close()
    if rows:
        return True
    return False


def init_pg(server) -> None:
    """ "
    Init schema db pg
    """

    sql_path = "./database/"
    # Create table migration
    conn_, cursor_ = get_pg_connection()
    cursor_.execute(
        """
    CREATE TABLE IF NOT EXISTS tbl_migration(
        migration_id SERIAL PRIMARY KEY,
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT NOW(),
        updated_at TIMESTAMP WITHOUT TIME ZONE,
        file_name VARCHAR(128) UNIQUE,
        status BOOLEAN DEFAULT 't'
    );
    """
    )
    conn_.commit()
    try:
        (_, _, sql_files) = next(walk(sql_path))
    except StopIteration:
        sql_files = []
    for sql_file in natsorted(sql_files):
        server.log.info("[-][Postgres] Applied file: %s", sql_file)
        if verify_file_pg(sql_file):
            continue
        server.log.info("[+][Postgres] Applying file: %s", sql_file)
        path_file = path.join(sql_path, sql_file)
        with open(path_file, "r", encoding="utf-8") as fil:
            raw_sql = fil.read()
            try:
                cursor_.execute(raw_sql)
                conn_.commit()
            except errors.DuplicateTable:
                continue
            cursor_.execute(
                "INSERT INTO tbl_migration(file_name) values(%s)", (sql_file,)
            )
            conn_.commit()
    conn_.close()
