#.py para carregar/salvar as configurações do yaml
import yaml
from pathlib import Path
from typing import Any,Dict

BASE_DIR = Path(__file__).resolve().parent
CONFIG_DIR = BASE_DIR/"config"

def _load_yaml(path: Path) -> Dict[str,Any]:
    if not path.exists():
        return {}
    with path.open("r",encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def _merge(a: Dict[str, Any], b: Dict[str, Any]) -> Dict[str, Any]:
    # mescla recursivamente b sobre a
    for k, v in (b or {}).items():
        if isinstance(v, dict) and isinstance(a.get(k), dict):
            a[k] = _merge(a.get(k, {}), v)
        else:
            a[k] = v
    return a

def load_config(env: str = None) -> Dict[str, Any]:
    base = _load_yaml(CONFIG_DIR / "default.yaml")
    if env:
        override = _load_yaml(CONFIG_DIR / f"{env}.yaml")
        base = _merge(base, override)
    return base

def save_config(cfg: Dict[str, Any], env: str = None) -> None:
    path = CONFIG_DIR / (f"{env}.yaml" if env else "default.yaml")
    with path.open("w", encoding="utf-8") as f:
        yaml.safe_dump(cfg, f, sort_keys=False)