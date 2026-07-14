# Italian Driving Theory Tester

A tiny, self-contained web app to practise the Italian driving-theory (patente B)
true/false questions — in Italian, with English translations and explanations of
the wording traps that catch learners out.

Each question shows:

- the original **Italian** statement,
- **VERO / FALSO** answer buttons with instant scoring,
- an **English translation**,
- the **tricky wording** (`non obbliga`, `può / non può`, `solo`, `salvo`, …)
  highlighted and explained,
- the road-sign **image** where relevant,
- **read-aloud** of the Italian using your browser's built-in text-to-speech.

## Run it

No build, no server, no dependencies. Just open **`index.html`** in a browser.

To hear the Italian read aloud you need an Italian (it-IT) voice installed on your
system (on Windows: *Settings → Time & Language → Speech → Add voices → Italian*).

## Live version (GitHub Pages)

If Pages is enabled for this repo, the quiz is served straight from `index.html`
at the repo's Pages URL — no download needed.

## What's in here

| File | Purpose |
|------|---------|
| `index.html` | The whole quiz UI (HTML + CSS + JS). |
| `questions.js` | The question data (`window.QUESTIONS = [...]`). Pre-generated — this is what the page reads. |
| `images/` | Road-sign images referenced by some questions. |
| `export_questions.py` | Build script that regenerated `questions.js`. Not needed to use the app. |

## Regenerating the data (optional)

`questions.js` is already generated and committed, so you do **not** need any of
this to use the quiz.

`export_questions.py` rebuilds `questions.js` from a source SQLite database
(`driving_test.sqlite`) that holds the questions and their AI-generated English
translations and trap explanations. **That database is not included in this repo.**

Producing the AI enrichment (translations + trap explanations) requires access to
a large-language-model API — the original pipeline used **Azure OpenAI**. In other
words, regenerating the data from scratch needs your own LLM account and API key;
running the finished quiz needs nothing.

## License

MIT — see [LICENSE](LICENSE).
