# GLO Coding Club

[![MkDocs](https://img.shields.io/badge/Made%20with-MkDocs-526CFE?logo=materialformkdocs)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/Material%20for%20MkDocs-526CFE?logo=materialformkdocs)](https://squidfunk.github.io/mkdocs-material/)
[![GitHub Pages](https://img.shields.io/badge/View%20on-GitHub%20Pages-blue?logo=github)](https://dmccreary.github.io/glo-coding-club/)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-DA7857?logo=anthropic)](https://claude.ai/code)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## View the Live Site

Visit the site at: [https://dmccreary.github.io/glo-coding-club/](https://dmccreary.github.io/glo-coding-club/)

## Overview

GLO Coding Club is the companion website for the Groves Learning Organization (GLO) Coding Club, an interactive textbook for learning coding through creative projects. It is designed for club members learning to code through hands-on activities in Scratch, Turtle Graphics, Python, and build-your-own projects.

The site is built with MkDocs Material and will incorporate interactive MicroSims (p5.js simulations), a learning graph of coding concepts, and project write-ups as the club's curriculum develops. It also covers club logistics — meeting times, sample projects, volunteering, and background check requirements.

The site is currently in an early scaffolding stage: front matter and navigation are in place, and chapter content, MicroSims, and the learning graph are being built out incrementally.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/dmccreary/glo-coding-club.git
cd glo-coding-club
```

### Install Dependencies

This project uses MkDocs with the Material theme:

```bash
pip install mkdocs
pip install mkdocs-material
```

### Build and Serve Locally

Build the site:

```bash
mkdocs build
```

Serve locally for development (with live reload):

```bash
mkdocs serve
```

Open your browser to `http://localhost:8000`

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

This builds the site and pushes it to the `gh-pages` branch.

## Repository Structure

```
glo-coding-club/
├── docs/                       # MkDocs documentation source
│   ├── chapters/               # Chapter content (in progress)
│   ├── sims/                   # Interactive p5.js MicroSims
│   ├── appendices/             # Appendices and list of websites
│   ├── learning-graph/         # Concept list, taxonomy, dependency graph
│   ├── css/                    # Custom CSS (extra.css)
│   ├── img/                    # Logo, license badge, mascot images
│   ├── index.md                # Home page
│   ├── about.md                # Club logistics and audience
│   ├── license.md              # License terms
│   └── contact.md              # Contact information
├── plugins/                    # MkDocs hooks (social_override.py)
├── mkdocs.yml                  # MkDocs configuration and nav
└── README.md                   # This file
```

## Reporting Issues

Found a bug, typo, or have a suggestion for improvement? Please report it:

[GitHub Issues](https://github.com/dmccreary/glo-coding-club/issues)

When reporting issues, please include:

- Description of the problem or suggestion
- Steps to reproduce (for bugs)
- Expected vs actual behavior
- Screenshots (if applicable)

## License

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**You are free to:**

- Share — copy and redistribute the material
- Adapt — remix, transform, and build upon the material

**Under the following terms:**

- **Attribution** — Give appropriate credit with a link to the original
- **NonCommercial** — No commercial use without permission
- **ShareAlike** — Distribute contributions under the same license

See [license.md](docs/license.md) for full details.

## Acknowledgements

This project is built on the shoulders of giants in the open source community:

- **[MkDocs](https://www.mkdocs.org/)** — Static site generator optimized for project documentation
- **[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)** — Beautiful, responsive theme
- **[p5.js](https://p5js.org/)** — Creative coding library from NYU ITP
- **[Claude AI](https://claude.ai)** by Anthropic — AI-assisted content generation

## Contact

**Dan McCreary**

- GitHub: [@dmccreary](https://github.com/dmccreary)

Questions, suggestions, or collaboration opportunities? Feel free to open an issue on GitHub.
