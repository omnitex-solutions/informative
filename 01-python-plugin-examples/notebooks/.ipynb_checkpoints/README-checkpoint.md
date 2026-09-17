# Notebooks

Interactive demonstrations of the three plugin approaches.

| Notebook | Approach |
|----------|----------|
| `01_bare_entry_points.ipynb` | Zero-dependency entry points |
| `02_stevedore.ipynb` | Stevedore managers |
| `03_pluggy.ipynb` | Pluggy hooks |

## How to use

1. Install the corresponding example package first:

   ```bash
   cd ../01-bare-entry-points   # or 02-stevedore / 03-pluggy
   pip install -e .
   ```

2. Launch Jupyter from this directory:

   ```bash
   cd notebooks          # if you are not already here
   python -m jupyter notebook
   ```

   Or with JupyterLab:

   ```bash
   python -m jupyter lab
   ```

3. Open the desired notebook and run the cells.

The notebooks assume you are running them from inside the `notebooks/` directory (or that the parent packages are already installed in your environment).
