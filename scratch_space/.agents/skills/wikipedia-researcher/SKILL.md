---
name: wikipedia-researcher
description: Use this skill when asked to research a topic with Wikipedia and produce a small research folder with facts and a final report.
---

# Wikipedia Researcher

When given a research question:

1. Create a new folder for the question.
2. Name it with a very short hyphenated slug.
   - Example: `Who invented Rust?` -> `who-invented-rust`
3. In that folder, maintain:
   - `facts.md`
   - `report.md`

## Research process

Use Wikipedia's public APIs and machine-readable content when possible.

Prefer:
- Wikipedia search API to find relevant pages
- Wikipedia page summary/extract APIs
- raw or structured content formats rather than opening the HTML website

Good starting points:
- `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=...&format=json`
- `https://en.wikipedia.org/api/rest_v1/page/summary/...`
- `https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles=...&format=json`

Prefer plain text extracts (`explaintext=1`) or summary endpoints over reading rendered HTML.

## Facts file

Whenever you find a relevant fact, append it to `facts.md`.

Each fact should include:
- the fact
- the source URL

Keep it simple, for example:

```md
- Rust was originally created by Graydon Hoare.
  Source: https://en.wikipedia.org/wiki/Rust_(programming_language)
```

## Final report

Once you have enough facts to answer the question:

- write `report.md`
- answer the question clearly and succinctly
- synthesize from the facts
- do **not** cite `facts.md`
- do **not** include source links in `report.md`

`report.md` should just contain the research result itself.

For the final response, give the user the path to the file on disk. Don't reiterate the report in your final response.
