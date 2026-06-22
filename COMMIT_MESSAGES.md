# Commit message examples and guidelines

Recommended lightweight format for daily progress commits:

- Day NN: Short Title — brief description

Examples:

- Day 01: Blackjack GUI — add initial GUI and card-dealing logic
- Day 02: Data types exercises — add solutions and notes
- Day 10: Web scraping — add scraper for quotes.toscrape

Tips:

- Keep the message concise but descriptive.
- Use the day number at the start for easy filtering and history.
- Use an em dash to separate title from a short description.

Quick commit commands:

```bash
git add .
git commit -m "Day 01: Blackjack GUI — add initial GUI and card-dealing logic"
git push origin main
```

Optional: follow Conventional Commits for tooling compatibility, e.g., `feat`, `fix`, `docs`, `chore`.
