#!/bin/bash

docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot filter --input $1 -T biological_entity_terms.txt --select "annotations self descendants" --signature true --output EFO_biological_entity.owl

docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot export --input EFO_biological_entity.owl --header "ID|LABEL|hasExactSynonym|IAO_0000115" --include classes --enti
ty-select NAMED --export EFO_biological_entity.csv