import json
from pathlib import Path
import typer
from datasets import load_dataset
import slmlab
from slmlab.utils.config import load_config
from {{cookiecutter.project_slug}}.prep.templating import make_example

app = typer.Typer()

@app.command()
def build(
    repo: str = typer.Option(..., "--repo", "-r", help="HF dataset repo, e.g. owner/dataset"),
    train: Path = typer.Option(Path("data/processed/train.jsonl"), "--train"),
    eval: Path = typer.Option(Path("data/eval/heldout.jsonl"), "--eval"),
    eval_ratio: float = typer.Option(0.2, "--eval-ratio", min=0.0, max=1.0),
    cfg_path: Path = typer.Option(Path("configs/default.yaml"), "--cfg-path"),
):
    cfg = load_config(cfg_path)
    mode = cfg.get("templating", {}).get("mode", "base")
    ds = load_dataset(repo)["train"]
    rows = [r for r in ds if r.get("metadata") and r.get("unimarc_record")]
    n_eval = max(1, int(len(rows) * eval_ratio))
    eval_rows, train_rows = rows[:n_eval], rows[n_eval:]

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
    typer.run(build)