@echo off
pip uninstall printrgb -y
set "ver=1.1.3"
py -m build --no-isolation
pip install .\dist\printrgb-%ver%-py3-none-any.whl