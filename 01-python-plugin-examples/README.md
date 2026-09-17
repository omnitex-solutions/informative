# Python Plugin Examples

Working examples that accompany the article:

> **Python Plugin Systems: From Bare Entry Points to Stevedore & Pluggy**

This repository contains four complete, runnable demonstrations of the same simple “formatter” plugin system implemented four different ways.

## Structure

```
01-bare-entry-points/   → zero third-party dependencies (importlib.metadata only)
02-stevedore/           → Stevedore quality-of-life layer
03-pluggy/              → Pluggy hook-based approach
04-stevedore-pluggy/    → Stevedore for discovery + Pluggy for hook dispatch
```

Each folder is a self-contained package you can install and run.

## Quick start

### 1. Bare entry points (no extra dependencies)

```bash
cd 01-bare-entry-points
pip install -e .
python -m myapp.loader
```

### 2. Stevedore

```bash
cd 02-stevedore
pip install -e .
python -m myapp.loader
```

### 3. Pluggy

```bash
cd 03-pluggy
pip install -e .
python -m myapp.loader
```

### 4. Stevedore + Pluggy

```bash
cd 04-stevedore-pluggy
pip install -e .
python -m myapp.loader
```

## What each example shows

| Example | Focus |
|---------|-------|
| **01-bare-entry-points** | How far you can get with only the standard library |
| **02-stevedore** | DriverManager, ExtensionManager, and the `map()` helper |
| **03-pluggy** | Hook specifications, multiple implementations, result collection |
| **04-stevedore-pluggy** | Stevedore for entry-point discovery, Pluggy for hook contract and dispatch |

## Requirements

- Python ≥ 3.10
- For Stevedore example: `stevedore`
- For Pluggy example: `pluggy`
- For Stevedore + Pluggy example: `stevedore`, `pluggy`

---

Feel free to use these examples as a starting point for your own plugin systems.
