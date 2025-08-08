import os
import time
import logging
import schedule
import pandas as pd
import cx_Oracle
from sqlalchemy import create_engine, text
from typing import Dict
from datetime import datetime
from urllib.parse import quote_plus

# Configuration
class Config:
    # Oracle Configuration
    ORACLE_HOST = "10.151.1.75"
    ORACLE_PORT = 1521
    ORACLE_SERVICE = "bmatraffice"
    ORACLE_USER = "SYS"
    ORACLE_PASSWORD = "welcome1"
    
    # PostgreSQL Configuration
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_NAME = "ITS"
    DB_USER = "postgres"
    DB_PASSWORD = "abc@1234"

# Table Mapping Configuration
TABLE_MAPPINGS = {
    "users_sync_1": {
        "oracle_table": "BMA_PHASE_II.USERS",
        "oracle_select": "all",  # ดึงทั้งหมด
        "postgres_table": "users",
        "primary_key": None,
        "postgres_column_select": ["name"],  # จะเลือกเฉพาะคอลัมน์ name ใน postgres insert
        "batch_size": 1000,
        "enabled": True,
        "column_mapping": {},
        "exclude_columns": [],
        "custom_query": None
    },
    "users_sync_2": {
        "oracle_table": "BMA_PHASE_II.USERS",
        "oracle_select": ["name"],
        "postgres_table": "users",
        "primary_key": None,
        "postgres_column_select": ["name"],
        "batch_size": 1000,
        "enabled": True,
        "column_mapping": {},
        "exclude_columns": [],
        "custom_query": None
    }
}

class DatabaseManager:
    def __init__(self):
        self.oracle_conn = None
        self.postgres_engine = None
        self.setup_logging()
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('data_sync.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def get_oracle_connection(self):
        try:
            if self.oracle_conn is None:
                dsn = cx_Oracle.makedsn(
                    Config.ORACLE_HOST, 
                    Config.ORACLE_PORT, 
                    service_name=Config.ORACLE_SERVICE
                )
                self.oracle_conn = cx_Oracle.connect(
                    user=Config.ORACLE_USER,
                    password=Config.ORACLE_PASSWORD,
                    dsn=dsn,
                    mode=cx_Oracle.SYSDBA  # สำหรับ SYS user
                )
                self.logger.info("Oracle connection established")
            else:
                # เช็ค connection ว่ายังใช้ได้หรือไม่
                try:
                    self.oracle_conn.ping()
                except cx_Oracle.DatabaseError:
                    self.logger.warning("Oracle connection lost. Reconnecting...")
                    self.oracle_conn.close()
                    self.oracle_conn = None
                    return self.get_oracle_connection()
            return self.oracle_conn
        except Exception as e:
            self.logger.error(f"Failed to connect to Oracle: {e}")
            raise
    
    def get_postgres_engine(self):
        try:
            if self.postgres_engine is None:
                password_encoded = quote_plus(Config.DB_PASSWORD)
                connection_string = f"postgresql://{Config.DB_USER}:{password_encoded}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"
                self.postgres_engine = create_engine(connection_string)
                self.logger.info("PostgreSQL engine created")
            return self.postgres_engine
        except Exception as e:
            self.logger.error(f"Failed to create PostgreSQL engine: {e}")
            raise
    
    def fetch_oracle_data(self, table_config: Dict) -> pd.DataFrame:
        try:
            oracle_conn = self.get_oracle_connection()
            
            if table_config.get("custom_query"):
                query = table_config["custom_query"]
            else:
                oracle_select = table_config.get("oracle_select", "*")
                
                if isinstance(oracle_select, str) and oracle_select.lower() in ["all", "*"]:
                    select_clause = "*"
                elif isinstance(oracle_select, list) and oracle_select:
                    select_clause = ", ".join(oracle_select)
                else:
                    select_clause = "*"
                
                query = f"SELECT {select_clause} FROM {table_config['oracle_table']}"
            
            self.logger.info(f"Executing Oracle query: {query}")
            df = pd.read_sql(query, oracle_conn)
            
            # เก็บ DataFrame เดิมไว้สำหรับแสดง Log (ก่อนการ filter columns)
            df_original = df.copy()
            
            df.columns = [col.lower() for col in df.columns]
            
            if table_config.get("column_mapping"):
                df = df.rename(columns=table_config["column_mapping"])
            
            if table_config.get("exclude_columns"):
                df = df.drop(columns=table_config["exclude_columns"], errors='ignore')
            
            # Log ข้อมูลทั้งหมดเมื่อ oracle_select == "all" (ใช้ DataFrame เดิม)
            oracle_select = table_config.get("oracle_select", "*")
            if isinstance(oracle_select, str) and oracle_select.lower() == "all":
                self.logger.info(f"Data fetched all rows (full dump) - Original columns: {list(df_original.columns)}")
                self.logger.info(f"Full data from Oracle (all columns):\n{df_original.to_string(index=False, max_cols=None, max_rows=None)}")
            
            # ตอนนี้ค่อยทำการ filter columns สำหรับการ insert ลง PostgreSQL
            postgres_cols = table_config.get("postgres_column_select")
            if postgres_cols:
                df_cols_lower = {col.lower(): col for col in df.columns}
                selected_cols_actual = []
                for col in postgres_cols:
                    col_lower = col.lower()
                    if col_lower in df_cols_lower:
                        selected_cols_actual.append(df_cols_lower[col_lower])
                    else:
                        self.logger.warning(f"Column '{col}' specified in postgres_column_select not found in Oracle data columns")
                
                if selected_cols_actual:
                    df = df[selected_cols_actual]
                    self.logger.info(f"Filtered data for PostgreSQL insert (selected columns {postgres_cols}): columns={list(df.columns)}, records={len(df)}")
                else:
                    self.logger.error("None of the specified postgres_column_select columns found in Oracle data. Returning empty DataFrame.")
                    return pd.DataFrame()
            
            self.logger.info(f"Final data for insert: columns={list(df.columns)}, records={len(df)}")
            
            # แสดงตัวอย่างข้อมูลสำหรับการ insert
            if not (isinstance(oracle_select, str) and oracle_select.lower() == "all"):
                self.logger.info(f"Data preview for insert:\n{df.head().to_string(index=False)}")
            
            return df
            
        except Exception as e:
            self.logger.error(f"Error fetching data from Oracle: {e}")
            raise

    def upsert_postgres_data(self, df: pd.DataFrame, table_config: Dict):
        if df.empty:
            self.logger.info("No data to sync")
            return

        try:
            engine = self.get_postgres_engine()
            table_name = table_config["postgres_table"]

            self.logger.info(f"Inserting into {table_name}, shape={df.shape}")
            self.logger.info(f"Columns: {df.columns.tolist()}")
            self.logger.info(f"Data preview:\n{df.head()}")

            with engine.begin() as conn:
                # ตรวจสอบว่าตารางว่างหรือไม่
                result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
                row_count = result.scalar()

                if row_count == 0:
                    # ถ้าว่าง → reset id
                    conn.execute(text(f"TRUNCATE TABLE {table_name} RESTART IDENTITY"))
                    self.logger.info(f"Table '{table_name}' was empty, reset identity (id starts from 1)")
                else:
                    self.logger.info(f"Table '{table_name}' already has {row_count} rows, continuing insert")

                # Insert ข้อมูลใหม่
                df.to_sql(table_name, conn, if_exists='append', index=False, method='multi')

            self.logger.info(f"Successfully inserted {len(df)} records into '{table_name}'")
        except Exception as e:
            self.logger.error(f"Error inserting data into PostgreSQL: {e}")
            raise
    
    def sync_table(self, sync_name: str, table_config: Dict):
        if not table_config.get("enabled", True):
            self.logger.info(f"Sync '{sync_name}' is disabled")
            return
        
        try:
            start_time = datetime.now()
            self.logger.info(f"Starting sync for '{sync_name}'")
            
            df = self.fetch_oracle_data(table_config)
            
            if df.empty:
                self.logger.warning(f"No data fetched for '{sync_name}', skipping sync.")
                return
            
            self.upsert_postgres_data(df, table_config)
            
            duration = (datetime.now() - start_time).total_seconds()
            self.logger.info(f"Completed sync for '{sync_name}' in {duration:.2f} seconds")
            
        except Exception as e:
            self.logger.error(f"Failed to sync '{sync_name}': {e}")
    
    def sync_all_tables(self):
        self.logger.info("=" * 50)
        self.logger.info("Starting data synchronization")
        
        for sync_name, table_config in TABLE_MAPPINGS.items():
            self.sync_table(sync_name, table_config)
        
        self.logger.info("Data synchronization completed")
        self.logger.info("=" * 50)
    
    def close_connections(self):
        if self.oracle_conn:
            self.oracle_conn.close()
            self.oracle_conn = None
        if self.postgres_engine:
            self.postgres_engine.dispose()
            self.postgres_engine = None
        self.logger.info("Database connections closed")

class DataSyncScheduler:
    def __init__(self):
        self.db_manager = DatabaseManager()
    
    def run_sync(self):
        try:
            self.db_manager.sync_all_tables()
        except Exception as e:
            self.db_manager.logger.error(f"Sync process failed: {e}")
    
    def start_scheduler(self):
        self.db_manager.logger.info("Starting data sync scheduler (every 5 minutes)")
        
        schedule.every(5).minutes.do(self.run_sync)
        
        self.run_sync()
        
        try:
            while True:
                schedule.run_pending()
                time.sleep(30)
        except KeyboardInterrupt:
            self.db_manager.logger.info("Scheduler stopped by user")
        except Exception as e:
            self.db_manager.logger.error(f"Scheduler error: {e}")
        finally:
            self.db_manager.close_connections()

def main():
    try:
        scheduler = DataSyncScheduler()
        scheduler.start_scheduler()
    except Exception as e:
        logging.error(f"Application error: {e}")
        raise

if __name__ == "__main__":
    main()