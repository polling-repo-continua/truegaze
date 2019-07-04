#
# Copyright (c) 2019 Nightwatch Cybersecurity.
#
# This file is part of truegaze
# (see https://github.com/nightwatchcybersecurity/truegaze).
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import click
from plugins import *
from utils import *

import pprint

@click.group()
def cli():
    """
    A static analysis tool for Android and iOS applications focusing on security issues outside the source code
    such as resource strings, third party libraries and configuration files
    """


@cli.command('list')
def list_plugins():
    """List supported plugins"""
    click.echo('test')


@cli.command('scan')
@click.argument('filename', type=click.Path(exists=True, dir_okay=False))
def scan(filename):
    """Scan the provided file for vulnerabilities"""

    # Try to open the provided file as a ZIP, fail otherwise
    zip_file = open_file_as_zip(filename)

    # Detect OS, error out if neither one is detected
    is_android = check_if_android(zip_file)
    is_ios = check_if_ios(zip_file)
    if  not is_android and not is_ios:
        click.echo('ERROR: Unable to identify the file as an Android or iOS application')
        sys.exit(-2)

    # Pass the filename to the individual modules for scanning


if __name__ == '__main__':
    cli()