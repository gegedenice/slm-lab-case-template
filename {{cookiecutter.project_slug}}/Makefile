.PHONY: venv install prep train eval smoke

venv:
	python -m venv .venv && . .venv/bin/activate && pip install -U pip wheel

install:
	pip install -U pip wheel
	pip install "{{cookiecutter.core_dependency}}"
	pip install -e .

prep:
	python -m {{cookiecutter.project_slug|replace('-', '_')}}.io.loader_hf build \
	  --repo Geraldine/metadata-to-unimarc-reasoning \
	  --train data/processed/train.jsonl \
	  --eval data/eval/heldout.jsonl \
	  --eval-ratio 0.2

train:
	python -m slmlab.cli.finetune run --cfg_path configs/default.yaml

eval:
	python -m slmlab.cli.evaluate run {{cookiecutter.default_model_id}} runs/adapter data/eval/heldout.jsonl

smoke:
	bash scripts/smoke_eval.sh