#!/bin/bash

set -o xtrace
set -o errexit

isort --check-only --diff .
black --diff --check .
flake8 --show-source .
