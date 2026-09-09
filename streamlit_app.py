import streamlit as st
import pandas as pd


@st.fragment(run_every="5m")
def show_single_interface(database_name:str, table_name:str):
    conn = st.connection(database_name, type="sql")
    interfaces_df = conn.query(f"SELECT interface FROM {table_name}")
    interface_set = set(interfaces_df['interface'])

    selected_interface = st.selectbox("Select Interface", interface_set)
    interface_df = conn.query(f"SELECT * FROM {table_name} WHERE interface = '{selected_interface}';",
                              ttl="5m",
                              )
    st.line_chart(interface_df, y="Bps", x="timestamp")
    st.line_chart(interface_df, y="util_pct", x="timestamp", y_label="Utilization %", x_label="Time")

@st.fragment(run_every="5m")
def show_interface_bytes_comparison(database_name:str, table_name:str):
    conn = st.connection(database_name, type="sql")
    interfaces_df = conn.query(f"SELECT interface FROM {table_name}")
    interface_set = set(interfaces_df['interface'])
    query_limit = len(interface_set)

    total_interface_data_df = conn.query(f"SELECT interface, tx_bytes, rx_bytes FROM {table_name} ORDER BY timestamp DESC, tx_bytes ASC LIMIT {query_limit}")
    st.bar_chart(total_interface_data_df, y=["tx_bytes", "rx_bytes"], x="interface", stack=False)


def main():
    db_name = "aos_cx_fun"
    table_name = "interface_metrics"
    st.set_page_config(page_title="fun switch", layout="wide")

    st.title("Interface Metrics")
    show_single_interface(db_name, table_name)
    show_interface_bytes_comparison(db_name, table_name)    

if __name__ == "__main__":
    main()