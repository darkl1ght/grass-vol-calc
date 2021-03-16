#!/usr/bin/env python3.7
from pydantic import BaseModel
from grass_engine import grass, GrassEngineException, cleanup_grass_context
import uvicorn
import os
import json
from typing import Optional
from fastapi import FastAPI
from tasks import add, execute_grass_script
from geojson import Feature, Point, FeatureCollection

app = FastAPI()


class Grass_Data(BaseModel):
    polygon_geojson: dict
    area: int
    point_geojson: dict


@app.get("/")
async def read_root():
    a = 'test_ping_successful'
    return {"status": a}


@app.get("/add/{a}/{b}")
def adds(a: int, b: int):
    return {'task_id': add.delay(a, b).task_id}


@app.post("/calcVolume/{project_name}")
def calc_grass_volume(project_name: str, payload: Grass_Data):
    try:
        # grass_data = json.loads(data.data.replace("\\", r"\\")).decode('utf-8')
        area = payload.polygon_geojson
        points = payload.point_geojson
        dsm = os.path.abspath('./files/dsm-' + project_name + '.tif')
    except Exception as e:
        return {'error': str(e)}

    try:
        context = grass.create_context({'auto_cleanup': False})
        context.add_file('area_file.geojson', json.dumps(area))
        context.add_file('points_file.geojson', str(points))
        context.add_param('dsm_file', dsm)
        context.set_location(dsm)

        celery_task_id = execute_grass_script.delay(os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "calc_volume.py"
        ), context.serialize()).task_id

        # data = execute_grass_script(os.path.join(
        #     os.path.dirname(os.path.abspath(__file__)),
        #     "calc_volume.py"
        # ), context.serialize())

        return {'celery_task_id': celery_task_id}
    except GrassEngineException as e:
        return {'error': str(e)}

    return {"project_name": project_name, 'points': points, 'area': area, 'dsm': dsm}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", reload=True,
                port=5000, log_level="info")

# {
#  "data": "{"polygon_geojson":{"type":"Feature","properties":{},"geometry":{"type":"Polygon","coordinates":[[[77.56791878658811,13.111361044641356],[77.5679393868565,13.11131937483033],[77.56799960302692,13.111339438073003],[77.5679885105755,13.111382651206526],[77.56791878658811,13.111361044641356]]]}},"area":37.26398530864275,"point_geojson":{"type":"FeatureCollection","features":[{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.56791878658811,13.111361044641356]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.5679393868565,13.11131937483033]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.56799960302692,13.111339438073003]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.5679885105755,13.111382651206526]}},{"type":"Feature","properties":{},"geometry":{"type":"Point","coordinates":[77.56791878658811,13.111361044641356]}}]}}"
# }
