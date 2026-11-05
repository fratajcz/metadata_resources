#!/bin/bash

docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot export --input $1 --header "ID|LABEL|definition" --include classes --entity-select NAMED --export fbbi-classes.csv