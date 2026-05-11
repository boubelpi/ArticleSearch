# ArticleSearch

Prototype script for semi-automated search of external references to a public article.

The script fetches the original article, generates summaries using a Hugging Face summarization model, uses the article URL and generated summaries as search queries, collects candidate URLs through Miyami web search

The final analysis is available in:

* Report: [REPORT.md](./REPORT.md)
* Spreadsheet with findings: [Spreadsheet](https://docs.google.com/spreadsheets/d/1js68QZD8jFLb2auvIfnbzE5MzGzg_Uq9FSSA966AQgY/edit?usp=sharing)

## Requirements

* Python 3.11.9+
* Internet connection

No Hugging Face access token is required for this prototype

## Dependencies

The script uses:

* `httpx` for HTTP requests (which are made by [Miyami websearch tool](https://github.com/ankushthakur2007/miyami_websearch_tool))
* `transformers` for Hugging Face pipelines
* `torch` as the model backend

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running

You need to run main.py file. This can be done in this way:

```bash
python main.py
```

## Notes on runs

Runs of script may take some time, first run takes more time, since Hugging Face model is downloaded. Please, be patient.

Search results may change over time because the script uses live web search. In addition, generated summaries may differ between runs, which can lead to slightly different search queries and results.
