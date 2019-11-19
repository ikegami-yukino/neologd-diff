# neologd-diff
This repository aims at comparing your mecab-ipadic-neologd with latest it.
Results (diff; added/removed entries) are written to `results/added.csv` and `results/removed.csv`.

## USAGE

### Put source mecab-ipadic-neologd repository
If you did not clone mecab-ipadic-neologd, then you would like to execute the following command:
```
$ make initialize
```
By executing this command, mecab-ipadic-neologd v0.0.6 is downloaded and it put to `previous/mecab-ipadic-neologd` directory.

If you cloned mecab-ipadic-neologd, then you should execute the following command:
```
cp -r path-to-cloned-neologd-repo previous/mecab-ipadic-neologd
```

### Update latest mecab-ipadic-neologd repository
```
make update
```

### Write diff
```
make diff
```
Results (diff; added/removed entries) are written to `results/added.csv` and `results/removed.csv`.

### Move latest mecab-ipadic-neologd repository to previous
```
make replace
```

## Acknowledgments
This repository relies on [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd).
