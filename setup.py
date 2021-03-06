#!/usr/bin/env python

#
# Copyright (C) 2019 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from setuptools import setup

setup(
    name='databricks-koala',
    version='0.0.5',
    packages=['databricks', 'databricks.koala', 'databricks.koala._dask_stubs'],
    install_requires=[
        'pyspark>=2.4.0',
        'pandas>=0.23',
        'decorator',
        'pyarrow>=0.10,<0.11'],  # See https://github.com/databricks/spark-pandas/issues/26
    author="Timothy Hunter",
    author_email="tim@databricks.com",
    license='http://www.apache.org/licenses/LICENSE-2.0',
    long_description=open('README.md').read(),
)
