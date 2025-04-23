# Releasing the dataset

In case of upstream changes in glottography-data:
```shell
cldfbench download cldfbench_walker2011bayesian.py
```

```shell
cldfbench makecldf cldfbench_walker2011bayesian.py --glottolog-version v5.1
```

```shell
cldf validate cldf
cldfbench geojson.validate cldf
```

```shell
cldfbench cldfreadme cldfbench_walker2011bayesian.py
```

```shell
cldfbench zenodo cldfbench_walker2011bayesian.py
```

```shell
cldfbench readme cldfbench_walker2011bayesian.py
```

```shell
cldfbench geojson.glottolog_distance cldf
```