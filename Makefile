VENV = langcogenv

install:
	python3 -m venv langcogenv
	./langcogenv/bin/pip install -r requirements.txt

preprocess:
	./langcogenv/bin/python3 ./data_for_analysis/preprocessing.py

train:
	./langcogenv/bin/python3 ./data_for_analysis/train.py

clean:
	rm -rf langcogenv

reinstall: clean install