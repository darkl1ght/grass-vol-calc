#!/usr/bin/env python3.7
import tempfile
# import sys
# import shutil
# import os
# from geojson import Feature, FeatureCollection, Point

# area = {
#     "type": "Feature",
#     "properties": {},
#     "geometry": {
#             "type": "Polygon",
#             "coordinates": [
#                 [
#                     [77.56916023082744, 13.110411278165714],
#                     [77.57070518321939, 13.110515770008163],
#                     [77.57069445438441, 13.109251415736395],
#                     [77.56931043453199, 13.109230517263853],
#                     [77.56932116336816, 13.109230517263853],
#                     [77.56888128108972, 13.109272314207189],
#                     [77.56916023082744, 13.110411278165714]
#                 ]
#             ]
#     }
# }
# points = FeatureCollection([Feature(geometry=Point(coords))
#                             for coords in area['geometry']['coordinates'][0]])

# print(points)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MEDIA_ROOT = os.path.join(BASE_DIR, 'app', 'media')
# MEDIA_TMP = os.path.join(MEDIA_ROOT, 'tmp')

# print(BASE_DIR)
# print(MEDIA_ROOT)
# # print(MEDIA_TMP)
# grass_binary = shutil.which('grass7') or \
#     shutil.which('grass7.bat') or \
#     shutil.which('grass72') or \
#     shutil.which('grass72.bat') or \
#     shutil.which('grass74') or \
#     shutil.which('grass74.bat') or \
#     shutil.which('grass76') or \
#     shutil.which('grass76.bat') or \
#     shutil.which('grass78') or \
#     shutil.which('grass78.bat') or \
#     shutil.which('grass80') or \
#     shutil.which('grass80.bat')


# with open('abc.txt', 'w+') as f:
#     f.write(grass_binary)

# env = os.environ.copy()
# env["LC_ALL"] = "C.UTF-8"
# # print(env)
# project_name = 'lime_stock_pile_1'

# dsm = os.path.abspath('./files/dsm-'+project_name)

# print(dsm)

# print(os.path.join(os.path.dirname(os.path.abspath(__file__)), "calc_volume.py"))
# if 'LD_LIBRARY_PATH' not in os.environ:
#     os.environ['GISBASE'] = "/usr/lib/grass78"
#     sys.path.append(os.environ['GISBASE'] + "/etc/python/")
#     os.environ["LD_LIBRARY_PATH"] = os.environ['GISBASE'] + "/lib"
#     os.environ['GIS_LOCK'] = "$$"
#     os.environ['GISRC'] = os.environ["HOME"] + "/.grass7/rc"
#     print(sys.argv)
#     try:
#         os.execv(sys.argv[0], sys.argv)
#     except Exception as exc:
#         print('Failed re-exec:', exc)
#         sys.exit(1)

# import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# # File uploads
# # MEDIA_TMP = os.path.join(MEDIA_ROOT, 'tmp')
# MEDIA_TMP = os.path.join(BASE_DIR, 'media')

# tmpdir = None
# if tmpdir is None:
#     tempdir = tempfile.mkdtemp(
#         '_grass_engine', dir=MEDIA_TMP)
#     tmpdir = os.path.basename(tempdir)
#     cwd = os.path.join(MEDIA_TMP, tmpdir)
#     os.chmod(cwd, 0o777)
