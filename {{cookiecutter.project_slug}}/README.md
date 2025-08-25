# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation (avec uv)

```bash
# Créer/activer un venv (optionnel)
uv venv .venv && source .venv/bin/activate

# Installer les dépendances depuis pyproject.toml (dont slmlab-core via [tool.uv.sources])
uv sync
```

---

## Arborescence

```
slm-lab-case-template/
├─ cookiecutter.json
├─ {{cookiecutter.project_slug}}/
│  ├─ README.md
│  ├─ LICENSE
│  ├─ .gitignore
│  ├─ .env.example
│  ├─ pyproject.toml
│  ├─ Makefile
│  ├─ configs/
│  │  ├─ default.yaml
│  │  ├─ methods/
│  │  │  └─ sft_lora.yaml
│  │  └─ models/
│  │     └─ model.yaml
│  ├─ data/
│  │  ├─ raw/.gitkeep
│  │  ├─ processed/.gitkeep
│  │  └─ eval/
│  │     ├─ golden_tests.yaml
│  │     └─ heldout.jsonl
│  ├─ src/
│  │  └─ {{cookiecutter.project_slug}}/
│  │     ├─ __init__.py
│  │     ├─ prep/
│  │     │  └─ templating.py
│  │     └─ io/
│  │        └─ loader_hf.py
│  ├─ scripts/
│  │  └─ smoke_eval.sh
│  └─ .github/workflows/
│     └─ ci-smoke.yml

```

---

## Usage

```
make venv
make install
make prep   # prépare le dataset
make train  # fine-tune LoRA
make eval   # évaluation
```

--- 

## Config in default.yaml 

- bf16: true → Use bfloat16 precision.
  - Works best on Ampere / Hopper NVIDIA GPUs (A100, H100, etc.) and on TPUs.
  - Safe numerically (much wider exponent range than fp16, so fewer NaN issues).
  - Usually preferred when supported.
- fp16: true → Use half precision (float16).
  - Works on most NVIDIA GPUs (including older ones).
  - Smaller dynamic range → sometimes requires loss scaling to avoid overflows.
- Don’t set both → Hugging Face Trainer expects one or the other.

---

## Misc

- .venv in notebooks
```
ipython kernel install --user --name=.venv
```

---

## `LICENSE`
{{cookiecutter.license}}

---
