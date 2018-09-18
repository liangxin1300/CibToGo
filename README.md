# CibToGo

## Prepare
In hawk-apiserver build environment, make sure "pacemaker-cli" be installed firstly

## Install
```
pip3 install cibToGoStruct
```

## Run
```
cibToGoStruct
```
Then go file api_structs.go will be created

## Some points for this project
* Read link file pacemaker.rng, which from package pacemaker-cli
* To fetch each extend ref rng file for specific version recursively
* Using lxml to parse rng file, and using jinja2 to prepare structs template
* Key tags are only "element" and "attribute", which are useful for hawk-apiserver
