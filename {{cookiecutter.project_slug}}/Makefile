.PHONY: venv install prep train eval smoke clean

VENV := .venv

# Create the uv-managed virtualenv and bootstrap basic tooling
$(VENV):
	uv venv $(VENV)
	uv pip install -U pip wheel

venv: $(VENV)

# Sync project deps from pyproject.toml; ensures venv exists
install: $(VENV)
	uv sync

# ---- Project tasks (always run inside the venv via `uv run`) ----

prep: install
	uv run python -m slm_lab_unimarc.io.loader_hf build \
	  --repo Geraldine/metadata-to-unimarc-reasoning \
	  --train data/processed/train.jsonl \
	  --eval data/eval/heldout.jsonl \
	  --eval-ratio 0.2

train: install
	uv run python -m slmlab.cli.finetune run --cfg_path configs/default.yaml

eval: install
	uv run python -m slmlab.cli.evaluate run LiquidAI/LFM2-350M runs/adapter data/eval/heldout.jsonl

smoke: install
	bash scripts/smoke_eval.sh

clean:
	rm -rf $(VENV) .python-version .venv.lock