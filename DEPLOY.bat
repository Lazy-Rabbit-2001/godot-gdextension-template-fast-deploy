@echo off

echo Starting deployment of renaming...
python .\deploy.py
echo Done deployment of renaming..

timeout /t 3 /nobreak >nul

echo Starting deployment of environment...
cd .\godot-cpp\
scons platform=windows custom_api_file=extension_api.json
echo Done deployment of environment...

timeout /t 3 /nobreak >nul

echo Done deployment of gdextension. Enjoy your deployment. (^_^)