# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""  """
import os
import sys

import django
django.setup()

root_dir = os.path.abspath(os.curdir)
sys.path.insert(0, root_dir)

from researches.controllers import openfoodfacts_api
from researches.controllers import save_data_api

api_off = openfoodfacts_api.ApiOff()

product = api_off.api_connection(5, 400)
data_db = save_data_api.SaveDataApi()
data_db.save_products(product)
