import streamlit as st

def show_system_data(database_name:str, table_name:str):
    conn = st.connection(database_name, type="sql")
    system_df = conn.query(f"SELECT * FROM {table_name} ORDER BY timestamp DESC LIMIT 1;")
    st.dataframe(system_df)

def main():
    db_name = "aos_cx_fun"
    table_name = "system_data"
    show_system_data(db_name, table_name)

if __name__ == "__main__":
    main()
