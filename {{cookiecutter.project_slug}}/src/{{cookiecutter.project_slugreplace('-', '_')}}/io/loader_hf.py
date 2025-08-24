import json
from pathlib import Path
import typer
from datasets import load_dataset
from slmlab.utils.config import load_config
from {{cookiecutter.project_slug|replace('-', '_')}}.prep.templating import make_example

app = typer.Typer()

@app.command()
def build(
    repo: str,
    train: Path = Path("data/processed/train.jsonl"),
    eval: Path = Path("data/eval/heldout.jsonl"),
    eval_ratio: float = 0.2,
    cfg_path: Path = Path("configs/default.yaml"),
):
    cfg = load_config(cfg_path)
    mode = cfg.get("templating", {}).get("mode", "base")

    ds = load_dataset(repo)["train"]
    rows = [r for r in ds if r.get("metadata") and r.get("unimarc_record")]
    n = len(rows)
    n_eval = max(1, int(n * eval_ratio))
    eval_rows = rows[:n_eval]
    train_rows = rows[n_eval:]

    train.parent.mkdir(parents=True, exist_ok=True)
    eval.parent.mkdir(parents=True, exist_ok=True)

    with train.open("w", encoding="utf-8") as ftr:
        for r in train_rows:
            ex = make_example(r["metadata"], r["unimarc_record"], mode=mode)
            ftr.write(json.dumps(ex, ensure_ascii=False) + "\n")

    with eval.open("w", encoding="utf-8") as fev:
        for r in eval_rows:
            ex = make_example(r["metadata"], r["unimarc_record"], mode=mode)
            fev.write(json.dumps(ex, ensure_ascii=False) + "\n")

    typer.echo(f"Wrote {len(train_rows)} train and {len(eval_rows)} eval examples (mode={mode}).")

if __name__ == "__main__":
    app()