#!/bin/bash

docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot export --input efo.owl --header "ID|LABEL|hasExactSynonym|IAO_0000115" --include classes --entity
-select NAMED --export EFO_classes.csv