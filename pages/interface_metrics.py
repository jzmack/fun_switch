import streamlit as st

@st.fragment(run_every="5m")
def show_single_interface(database_name:str, table_name:str):
    conn = st.connection(database_name, type="sql")
    interfaces_df = conn.query(f"SELECT DISTINCT interface, interface || ' - ' || description AS dropdown_label FROM {table_name};")

    # need a way to have pretty labels
    label_mapping = dict(zip(interfaces_df["interface"], interfaces_df["dropdown_label"]))

    selected_interface = st.selectbox(
        "Select Interface",
        options=interfaces_df["interface"],
        format_func=lambda x: label_mapping[x]
    )

    interface_df = conn.query(f"SELECT * FROM {table_name} WHERE interface = '{selected_interface}';",
                              ttl=300,
                              )

    st.title("Interface Utilization in mbps", text_alignment="left")
    st.line_chart(
        interface_df,
        y=["rx_mbps", "tx_mbps"],
        color=["#1AFF6F", "#9778FF"],
        y_label="mbps",
        x="timestamp",
        x_label="Time"
    )

    st.title("Utilization %", text_alignment="left")
    st.line_chart(
        interface_df,
        y="util_pct",
        x="timestamp",
        y_label="%",
        x_label="Time",
        color="#F2AAC7"
    )

@st.fragment(run_every="5m")
def show_interface_bytes_comparison(database_name:str, table_name:str):
    conn = st.connection(database_name, type="sql")
    interfaces_df = conn.query(f"SELECT interface FROM {table_name}")
    interface_set = set(interfaces_df['interface'])
    query_limit = len(interface_set)

    total_interface_data_df = conn.query(f"SELECT interface, tx_bytes_gb, rx_bytes_gb FROM {table_name} ORDER BY timestamp DESC, tx_bytes_gb ASC LIMIT {query_limit}")

    st.title("Rx & Tx Comparison")
    st.bar_chart(
        total_interface_data_df,
        y=["rx_bytes_gb", "tx_bytes_gb"],
        x="interface",
        y_label = "GB",
        stack=False,
        color=["#1AFF6F", "#9778FF"],
    )


def main():
    db_name = "aos_cx_fun"
    table_name = "interface_metrics"
    st.set_page_config(page_title="fun switch", layout="wide")

    show_single_interface(db_name, table_name)

    show_interface_bytes_comparison(db_name, table_name)

if __name__ == "__main__":
    main()
