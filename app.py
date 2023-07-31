from src.db.infrastructure.postgresql.postgresql_init_controller import PostgresqlInitController
from src.user.infrastructure.user_create_controller import UserCreateController
import psycopg2
from get_docker_secret import get_docker_secret
from loguru import logger
import uuid
from time import time
import asyncio
import aiopg

if __name__ == "__main__":
    pwd = get_docker_secret('db-password')
    
    dsn = f"dbname=postgres user=postgres password={pwd} host=db"
    
    postgresql_connection = psycopg2.connect(dsn)
    logger.info("Data base connected")
    
    try:
        logger.info("Init database")
        PostgresqlInitController.init(postgresql_connection)
        
        logger.info("creating 1000 users syncronous method")
        start = time()
        UserCreateController.sync_create_user_list_by_number(postgresql_connection,1000)
        syncronous_time = time() - start
        logger.info(f"created user at {syncronous_time} secs")
        postgresql_connection.close()
        
        logger.info("creating 1000 users asyncronous method")
        event_loop = asyncio.get_event_loop()
        start = time()
        event_loop.run_until_complete(UserCreateController.async_create_user_list_by_number(dsn,event_loop,1000))
        asyncronous_time = time() - start
        logger.info(f"created user at {asyncronous_time} secs")
        
        logger.info(f"Benchmarking: asyncronous = {asyncronous_time} vs syncronous = {syncronous_time}")
        
    except Exception as e:
        print(e)
    finally:
        if postgresql_connection:
            postgresql_connection.close()
            
        if event_loop:
            event_loop.close()
        logger.debug("Data base disconnected")
    
    
    
    
    
    