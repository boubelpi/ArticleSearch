import asyncio
import miyami
from transformers import pipeline

article_url = "https://blog.jetbrains.com/fleet/2025/12/the-future-of-fleet/"

q = asyncio.run(miyami.fetch(article_url))

article_content = q["content"]

article_title = q["metadata"]["title"]

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

search_queries = []

summaries_combined = ""

for _ in range(10):
    summary = summarizer(article_content, do_sample=True)
    search_queries.append(summary[0]["summary_text"])
    summaries_combined += summary[0]["summary_text"] + "\n"

search_queries.append(article_url)

print(summaries_combined)

unique_urls = set()

for query in search_queries:
    search = asyncio.run(miyami.search(query, rerank=True))
    res = search["results"]
    for result in res:
        if "www.fleet" in result["url"] or "-http" in result["url"] or "/http" in result["url"] or "dictionary" in result["url"]:
            continue
        unique_urls.add(result["url"])

print(unique_urls)

# classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# for url in unique_urls:
#    q = asyncio.run(miyami.fetch(url))
#    try:
#        content = q["content"]
#        title = q["metadata"]["title"]
#        candidate_text = f"""
#        Original article:
#        title: {article_title}
#        URL: {url}
#        Key claims: {summaries_combined}

#        Candidate source:
#        title: {title}
#        URL: {url}
#        content: {content}
#        """
#        labels = [
#        "the candidate directly references the original article",
#        "the candidate discusses or debates the original article",
#        "the candidate reuses facts or insights from the original article in a broader context",
#        "the candidate summarizes the original article",
#        "the candidate criticizes the original article or JetBrains decision",
#        "the candidate is irrelevant or only weakly related"
#        ]
#        result = classifier(
#        candidate_text,
#        candidate_labels=labels,
#        multi_label=True
#        )
#        print(url)
#        print(result["scores"])
#    except Exception as e:
#        print(url)
#        print(e)