# Resource tooling for RDM purposes

OWL is the commonly used format for ontologies. It is, however, mostly overpowered and not easily interoperable with other research data management tools, which require tabular data. These scripts therefore extract the required fields from ontologies relevant to us and export them in csv files.

Similarly, original CSV files might include tons of columns that are not necessary for our purposes.

## Setup:

1. an env with pandas installed.
2. for all OWL ontologies (FBbi): docker

### For FBbi:

Install robot via docker

```
docker pull obolibrary/robot
```

Test installation:

```
docker run -v $PWD/:/work -w /work --rm -ti obolibrary/robot robot --version
```

## Download:

All downloaded from `https://data.bioontology.org/ontologies/` , as CSV if possible, for some (like FBbi), OWL is used.

OME-OWL downloaded from https://github.com/German-BioImaging/ome-owl/blob/main/ontology/owl/ome_core/