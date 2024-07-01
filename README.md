# Godot Cpp with Fast Deployment
This repository is a fan-extended version of [original Godot Cpp Template](https://github.com/godotengine/godot-cpp-template). About detailed information, please check this link.

## What's optimized in this version?
* Deployed an example h/cpp file for starting.
* Added a `DEPLOY.bat` for quick start before your development

## Before you start
* Create your own repository based on this template.
* Make sure you have installed [Godot](https://godotengine.org/download) and [Visual Studio Code](https://code.visualstudio.com/download). (Of course you can use any other IDE or text editor, but here we will use Visual Studio Code as an example.)
* Clone this repository to your local machine.
* Open the project in Visual Studio Code.
* Run `DEPLOY.bat` to rename all `example` files and literals and deploy the godot-cpp environment for your GDExtension.
* To compile your test build, run 
```bat
scons platform=<your current os platform> target=template_debug
scons platform=<your current os platform> target=template_release
```
* To build full GDExtension that supports almost all major platforms, please push your updates to your repo and the github action will run automatically. Once the build is successful, you can download the `godot-cpp-template.zip` and unpack the folders into the `gdextension/<your extension name>/bin/` and overlap all of the folders in the directory.
