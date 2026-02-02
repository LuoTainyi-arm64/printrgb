#!/bin/bash
ver=1.2.3
python -m build --no-isolation
pip uninstall printrgb -y
pip install ./dist/printrgb-${ver}-py3-none-any.whl
