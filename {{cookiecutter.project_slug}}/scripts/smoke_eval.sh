#!/usr/bin/env bash
set -euo pipefail

CFG="configs/default.yaml"
BASE="{{cookiecutter.default_model_id}}"
EVAL="data/eval/heldout.jsonl"

echo "[prep] building tiny split from HF (if configured)…"
make prep || true

echo "[train] quick LoRA run…"
python -m slmlab.cli.finetune run --cfg_path "$CFG"

echo "[eval] comparing baseline vs tuned…"
python -m slmlab.cli.evaluate run "$BASE" runs/adapter "$EVAL"