import sqlite3

DB_FILE = "aos_cx_fun.db"

def create_insert_statements(all_int_stats:list[dict]) -> list[str]:
    sql_insert_statements:list[str] = []
    # wrap the TEXT types(the VALUE for interface in this case) around single ' quotes
    for interface in all_int_stats:
        insert_statement = f"""
        INSERT INTO interface_metrics (
            interface,
            description,
            tx_bytes,
            tx_bytes_kb,
            tx_bytes_mb,
            tx_bytes_gb,
            rx_bytes,
            rx_bytes_kb,
            rx_bytes_mb,
            rx_bytes_gb,
            Bps,
            total_bps,
            total_kbps,
            total_mbps,
            tx_bps,
            tx_kbps,
            tx_mbps,
            rx_bps,
            rx_kbps,
            rx_mbps,
            util_pct,
            timestamp
        )
        VALUES (
            '{interface["interface"]}',
            '{interface["description"]}',
            {interface["tx_bytes"]},
            {interface["tx_bytes_kb"]},
            {interface["tx_bytes_mb"]},
            {interface["tx_bytes_gb"]},
            {interface["rx_bytes"]},
            {interface["rx_bytes_kb"]},
            {interface["rx_bytes_mb"]},
            {interface["rx_bytes_gb"]},
            {interface["total_Bps"]},
            {interface["total_bps"]},
            {interface["total_kbps"]},
            {interface["total_mbps"]},
            {interface["tx_bps"]},
            {interface["tx_kbps"]},
            {interface["tx_mbps"]},
            {interface["rx_bps"]},
            {interface["rx_kbps"]},
            {interface["rx_mbps"]},
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
