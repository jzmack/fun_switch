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

def main():
    st.set_page_config(page_title="fun switch")

    st.title("Interface Metrics")
    show_single_interface("aos_cx_fun", "interface_metrics")
    

if __name__ == "__main__":
    main()