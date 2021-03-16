#!/usr/bin/env python3.7
from celery import Celery
from celery.utils.log import get_task_logger
from grass_engine import grass, GrassEngineException
app = Celery('tasks', broker='pyamqp://guest@localhost//')
logger = get_task_logger(__name__)


@app.task
def add(x, y):
    logger.info("Adding %s + %s, res: " % (x, y))
    return x + y


@app.task
def execute_grass_script(script, serialized_context={}, out_key='output'):
    try:
        ctx = grass.create_context(serialized_context)
        return {out_key: ctx.execute(script), 'context': ctx.serialize()}
    except GrassEngineException as e:
        return {'error': str(e), 'context': ctx.serialize()}
