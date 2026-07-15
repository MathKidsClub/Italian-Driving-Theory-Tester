# Italian Driving Theory Tester

**▶️ Play it live: https://mathkidsclub.github.io/Italian-Driving-Theory-Tester/**

A tiny, self-contained web app to practise the Italian driving-theory (patente B)
true/false questions — over 7,000 of them — in Italian, with English translations and explanations of
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

Served straight from `index.html`, no download needed:
**https://mathkidsclub.github.io/Italian-Driving-Theory-Tester/**

## What's in here

| File             | Purpose                                                                                         |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| `index.html`   | The whole quiz UI (HTML + CSS + JS).                                                            |
| `questions.js` | The question data (`window.QUESTIONS = [...]`). Pre-generated — this is what the page reads. |
| `images/`      | Road-sign images referenced by some questions.                                                  |

## About the data

The English translations and trap explanations in `questions.js` were generated
from an Italian question bank using a large-language-model pipeline (Azure OpenAI).
The data is pre-generated and committed, so nothing beyond a browser is needed to
use the quiz.

## License

MIT — see [LICENSE](LICENSE).
