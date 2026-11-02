# ISM2411 — Python for Business

**Name:** Jordan Lurch

**Semester:** Fall 2026

## About This Repo

This repository contains my weekly lab submissions for ISM2411 at the University of South Florida. It documents my work learning Python for business and using Git and GitHub to track changes.

## Modules

- `week07/` — Functions: calculate_tax, apply_discount, final_price, debugging, and variable scope.
- Module 8 — Git and GitHub setup, repository documentation, and version control.

## How to Run

Open a terminal in the repository folder and run:

```bash
python3 week07/functions.py
```

The script prints examples of tax calculations, membership discounts, final prices, sales totals, and variable scope.

## Reflection

### 1. Commit History

```text
6e98964 (HEAD -> main, origin/main, origin/HEAD) add README with module listing and run instructions
2f29eb2 add module 7 functions: calculate_tax, apply_discount, final_price
5aba246 add .gitignore for Python and OS files
d160241 Initial commit
```

If I were hiring someone, this history would show that they organize their work into separate, focused changes. The descriptive messages explain what each commit accomplishes, making the project easier to review and maintain.

### 2. How Git Changes My Editing Process

Using Git should encourage me to make small, focused edits and test my script before committing each working change. Instead of making many changes at once, I would save clear checkpoints so I can compare versions and restore an earlier version if something breaks.

### 3. An Additional .gitignore Entry

One entry I would add is `.venv/`, for a local Python virtual environment if I use one in this project. It contains installed packages and machine-specific files that can be recreated, so it should not be tracked in the repository.