
import os
from fastapi import HTTPException, status
from pymongo import MongoClient


__DB_HOST = os.getenv('DB_HOST')
__DB_PORT = int(os.getenv('DB_PORT'))
__DB_USER = os.getenv('DB_USR')
__DB_PSW = os.getenv('DB_PSW')


async def flattens_items(items):
    result = await __flattens_items(items)
    __save_result(result)
    return result


async def __flattens_items(items):
    result = []

    for item in items:
        if isinstance(item, int):
            result.append(item)
        elif isinstance(item, list):
            result.extend(await flattens_items(item))
        else:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail='Each item must be an integer or a integer list or integer nested lists.'
            )
        
    return result


def __save_result(result):
    if __DB_PSW and __DB_USER:
        uri = f'mongodb://{__DB_USER}:{__DB_PSW}@{__DB_HOST}:{__DB_PORT}'
    else:
        uri = f'mongodb://{__DB_HOST}:{__DB_PORT}'
        
    db_client = MongoClient(uri)
    db = db_client['primary_db']
    resutls = db['results']
    resutls.insert_one({'result': result})
