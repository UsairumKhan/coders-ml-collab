# Git-Based Collaboration for an ML Project

## Telco Customer Churn Prediction

This project is a collaborative Machine Learning workflow built using Git, DVC, and GitHub Actions.

### Project Structure
- `configs/`: Pipeline parameters and hyperparameters (`params.yaml`)
- `data/`: Dataset storage (tracked by DVC, ignored by Git)
- `models/`: Trained model artifacts (tracked by DVC, ignored by Git)
- `notebooks/`: Exploratory analysis paired with Jupytext
- `src/`: Modular Python scripts for pipeline execution
- `tests/`: Unit tests and dataset quality checks
- `.github/workflows/`: CI/CD automation pipelines

### Getting Started
```bash
# Clone the repository
git clone https://github.com/UsairumKhan/coders-ml-collab.git
cd coders-ml-collab

# Set up environment and dependencies
pip install -r requirements.txt
```
