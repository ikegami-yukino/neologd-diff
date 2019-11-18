.PHONY: initialize update diff replace

initialize:
	wget -O previous/mecab-ipadic-neologd.tar.gz https://github.com/neologd/mecab-ipadic-neologd/archive/v0.0.6.tar.gz
	cd previous; tar -xzvf mecab-ipadic-neologd.tar.gz; mv mecab-ipadic-neologd-0.0.6 mecab-ipadic-neologd
	rm previous/mecab-ipadic-neologd.tar.gz

update:
	git submodule foreach git fetch origin
	git submodule foreach git reset --hard origin/master

diff:
	./write_diff.py

replace:
	rm -rf previous/mecab-ipadic-neologd
	cp -r latest/mecab-ipadic-neologd previous/mecab-ipadic-neologd
