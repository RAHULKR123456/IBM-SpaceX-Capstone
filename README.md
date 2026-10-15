# IBM Data Science Capstone — SpaceX Falcon 9

## Project overview

This project analyzes historical SpaceX Falcon 9 launch data to explore launch-site patterns, payload characteristics, landing outcomes, and landing-success prediction.

## Repository contents

The repository contains **nine Jupyter notebooks** and **one Python application**.

| File | Purpose |
| --- | --- |
| `01_Data_Collection_API.ipynb` | SpaceX API data collection attempt (the request returned HTTP 525; historical course data used as fallback) |
| `02_Data_Collection_Wikipedia.ipynb` | Web scraping of a fixed Wikipedia revision (29 tables found) |
| `03_Data_Wrangling.ipynb` | Data preparation and target creation |
| `04_EDA_Visualization.ipynb` | Exploratory data analysis and charts |
| `05_EDA_SQL.ipynb` | SQL queries on the SPACEXTBL dataset |
| `05b_EDA_SQL_Additional_Queries.ipynb` | Additional SQL queries: launch sites, payloads, success rates, ranking, payload bands, time analysis |
| `06_Folium_Interactive_Map.ipynb` | Interactive launch-site map |
| `07_Predictive_Analysis.ipynb` | Classification models (Logistic Regression, SVM, Decision Tree, KNN) and evaluation |
| `08_Interactive_Dashboard_Plots.ipynb` | Interactive Plotly visualizations |
| `app.py` | Plotly Dash dashboard (site dropdown, success pie chart, payload slider, payload vs outcome scatter) |
| `SpaceX_Capstone_Presentation.pdf` | Presentation slides |

## Tools and technologies

Python, pandas, SQLite, scikit-learn, Matplotlib, Seaborn, Folium, Plotly, Dash, and Google Colab.

## Data sources

The project uses historical IBM Skills Network SpaceX datasets and a historical Wikipedia page. The live SpaceX API request was attempted but returned connection errors (HTTP 525) during execution.

## How to reproduce

1. Open notebooks `01` to `08` and `05b` in Google Colab and run the cells from top to bottom. Make sure the dataset URLs are accessible.
2. To run the dashboard locally:

```bash
pip install pandas plotly dash
python app.py
```

Then open http://127.0.0.1:8050 in your browser.

## Key results

- Landing success rose from 0% (2010 to 2013) to 90.0% in 2019 and 84.2% in 2020.
- KSC LC-39A has the highest landing success rate (76.9%); CCAFS LC-40 the lowest (26.9%).
- The best classifier is the SVM (sigmoid kernel, C = 1) with 83.3% test accuracy on 18 test launches, against a 66.7% baseline of always predicting success.

The full analysis is documented in the notebooks and in the project report PDF.

*This project was completed as part of the IBM Data Science Professional Certificate capstone exercise.*
