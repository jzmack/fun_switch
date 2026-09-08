def create_insert_statements(all_int_stats:list[dict]) -> list[str]:
    sql_insert_statements:list[str] = []
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

def insert_to_db(insert_list:list[str]):
    pass