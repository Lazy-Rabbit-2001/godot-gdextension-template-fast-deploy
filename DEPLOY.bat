@echo off

echo Starting deployment of renaming tool...
cd .\deployment\
python .\deploy
echo Done deployment.

timeout /t 3 /nobreak >nul

echo Starting deployment of environment...
cd ..\godot-cpp\
scons platform=windows custom_api_file=custom_api.json
echo Done deployment of environment...

timeout /t 3 /nobreak >nul

echo Done deployment of gdextension. Enjoy your deployment. (^_^)