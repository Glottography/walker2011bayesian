# Releasing the dataset

## Recreate the raw data from glottography-data

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_walker2011bayesian.py
```

## Recreate the CLDF data

```shell
cldfbench makecldf cldfbench_walker2011bayesian.py --glottolog-version v5.2
cldfbench cldfreadme cldfbench_walker2011bayesian.py
cldfbench zenodo --communities glottography cldfbench_walker2011bayesian.py
cldfbench readme cldfbench_walker2011bayesian.py
```

## Validation

```shell
cldf validate cldf
```

```shell
cldfbench geojson.validate cldf
```

```shell
cldfbench geojson.glottolog_distance cldf --format pipe
```

| ID | Distance | Contained | NPolys |
|:---------|-----------:|:------------|---------:|
| acha1250 | 0.00 | True | 1 |
| apur1254 | 0.00 | True | 3 |
| araw1276 | 0.00 | False | 4 |
| asha1243 | 0.00 | True | 1 |
| bani1255 | 0.60 | False | 2 |
| cabi1241 | 0.00 | True | 1 |
| cham1318 | 0.00 | True | 1 |
| curr1243 | 1.00 | False | 1 |
| guar1293 | 0.36 | False | 1 |
| igna1246 | 0.01 | False | 1 |
| inap1242 | 0.06 | False | 1 |
| mach1267 | 0.00 | True | 1 |
| mand1448 | 0.00 | False | 4 |
| mapi1252 | 0.80 | False | 1 |
| mehi1240 | 0.05 | False | 1 |
| noma1263 | 0.00 | True | 1 |
| pali1279 | 0.00 | False | 2 |
| para1316 | 0.00 | True | 1 |
| pare1272 | 0.00 | True | 1 |
| piap1246 | 0.00 | False | 2 |
| resi1247 | 1.18 | False | 1 |
| tari1256 | 0.10 | False | 2 |
| tere1279 | 0.00 | True | 2 |
| trin1274 | 0.00 | True | 1 |
| wapi1253 | 0.00 | True | 2 |
| waur1244 | 0.05 | False | 1 |
| wayu1243 | 0.00 | True | 4 |
| yane1238 | 0.00 | True | 1 |
| yine1238 | 0.00 | True | 1 |
| yucu1253 | 0.00 | True | 3 |
