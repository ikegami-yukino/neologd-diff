#!/usr/bin/env python3
from collections import defaultdict
import glob
import lzma
import os


def extract(prefix):
    keys = set()
    features = defaultdict(list)
    pattern = os.path.join(prefix, "mecab-ipadic-neologd", "seed", "*.xz")
    prev_paths = glob.glob(pattern)
    for path in prev_paths:
        with lzma.open(path) as f:
            for line in f:
                line = line.decode("utf8")
                row = line.split(",")
                key = ",".join(row[:3])
                keys.add(key)
                features[key].append(line)
    return (keys, features)


def main():
    (prev_keys, prev_feature) = extract("previous")
    (latest_keys, latest_feature) = extract("latest")
    all_keys = prev_keys | latest_keys

    print("ADDED:", len(all_keys - prev_keys))
    print("REMOVED", len(all_keys - latest_keys))

    with open(os.path.join("results", "added.csv"), "w") as f:
        for key in all_keys - prev_keys:
            for line in latest_feature[key]:
                f.write(line)
    with open(os.path.join("results", "removed.csv"), "w") as f:
        for key in all_keys - latest_keys:
            for line in prev_feature[key]:
                f.write(line)


if __name__ == "__main__":
    main()
