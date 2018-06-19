#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from curator.cli import run

def bootstrap():
    run("curator.yml", "actions.yml", dry_run=os.environ.get('DRY_RUN', True))

def lambda_handler(event, context):
    bootstrap()

def main():
    bootstrap()

if __name__ == "__main__":
    main()