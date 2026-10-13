# reyprocess.org

The official site of **REY Process**: a single-page, dark-and-gold site built from one template and one build script.

**Live:** https://reyprocess.org

![Desktop](screenshots/desktop.png)

| Mobile |
|---|
| <img src="screenshots/mobile.png" width="320"> |

## How it works
- `template.html` holds the layout and styles with `{{placeholders}}` for images.
- `build.py` inlines everything in `assets/` as data URIs and writes a single, dependency-free `index.html`.
- No framework, no tracking, no build chain beyond Python 3.

```bash
python3 build.py   # writes index.html
```

## Sections
Hero with the rooted cross · The Path Church app · ROOTED apparel · home and yard builds · timeline · verse · contact.

---
Built by **Samuel Rey Pineda**, founder of REY Process. Jesus is King.
