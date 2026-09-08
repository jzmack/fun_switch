import sqlite3

DB_FILE = "aos_cx_fun.db"

def create_insert_statements(all_int_stats:list[dict]) -> list[str]:
    sql_insert_statements:list[str] = []
    # wrap the TEXT types(the VALUE for interface in this case) around single ' quotes
    for interface in all_int_stats:
        insert_statement = f"""
        INSERT INTO interface_metrics (
            interface,
            tx_bytes,
            rx_bytes,
            Bps,
            util_pct,
            timestamp
        )
        VALUES (
            '{interface["interface"]}',
            {interface["tx_bytes"]},
            {interface["rx_bytes"]},
            {interface["total_Bps"]},
            {interface["util_pct"]},
            datetime('now','localtime')
        );
        """
        sql_insert_statements.append(insert_statement)
    return sql_insert_statements

def send_inserts(insert_list:list[str]):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        for insert_statement in insert_list:
            cursor.execute(insert_statement)
        conn.commit()
