# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Installation
```bash
python -m venv .venv && source .venv/bin/activate
pip install -U pip wheel
pip install "{{cookiecutter.core_dependency}}"
pip install -e .
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
make prep   # prépare le dataset
make train  # fine-tune LoRA
make eval   # évaluation
```

---

## `LICENSE`
*(rempli selon choix de `cookiecutter.license`)*

---
