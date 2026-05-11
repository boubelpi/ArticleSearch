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

## Limitations

The analysis is not exhaustive. Search results change over time, and some websites are not relevant to the original article. Also some pages could not be fetched automatically.

While HF model by Facebook gets mostly relevant summary to the article, it's not perfect either and can sometimes distort the facts (for example, in some runs it named Fleet as toolbox, which is not true). That's why I got several different summaries for search queries to get more stable search results.

The classification also needs manual review, since current HF model doesn't provide relevant classification.

While searching is done pretty well by Miyami websearch tool, I needed to exclude some websites, that often appeared as a result of search and that aren't connected to the original article. These exclusions are connected to the article of discontinuation of Fleet, for different articles these exclusions are likely not relevant. And still, there are some articles that aren't connected with the original one, but this number is lower than it was before I made exclusions.

I used automation mainly for discovery and preprocessing, while final classification was done manually.

## Ways to improve

While I used HF models for analysis, which are free for use, using paid models could improve the approach, for example, it could get some more valued summaries of original article for search query, it could get some key claims from the article, which are also relevant for search queries. Paid model could also be used in classification purpose, but still manual review is required here to check, if the results of classification are relevant.

And while Miyami websearch tool is good for the current task (especially for searching queries), it's not that good in fetching: while fetching query works for the website with the original article, many other popular websites (such as Medium) couldn't be fetched as the result of query was error. This problem is not that trivial, but could be solved by working with website-specific APIs. And in this case I would need to write websearch tool by myself or use Miyami websearch tool only for searching queries.

Nonetheless Miyami websearch tool does good job in processing searching queries, some of the websites could be missing. One of the reasons I could see is that some articles reference not to the original task, but to other articles, which are still based on the original one (for example, some sources had links to infoworld article and were based on it, not the original one) and this process could be recursive in some way. The idea could be to manage finding all relevant URLs recursively: if the current URL is relevant to the original one, this URL should be added to the set of all URLs and after that Miyami websearch tool should look for articles, which are based on the current one. After finding this articles for the current one, check all of them and if they're not added to the set of all URLs for the original article, continue recursions with that article. At the end, only articles, which are based on the original one could be passed as `Direct reference`, other articles should be passed as `Usage of insights`.
