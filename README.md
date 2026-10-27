# Jothiroopa D – Portfolio

A responsive, single-page portfolio built with plain HTML, CSS and JavaScript (no installs needed).

## Folder structure

```
portfolio/
├── index.html                 # content (text, sections)
├── style.css                  # design (colors, layout)
├── script.js                  # behaviour (typing effect, dark mode, menu)
├── Resume_jothiroopad.pdf     # copy your resume here (for the Download button)
└── images/
    └── profile.jpg            # YOUR PHOTO goes here
```

## Setup in VS Code

1. Create an `images` folder inside `portfolio` and save your photo as `profile.jpg`.
2. Copy `Resume_jothiroopad.pdf` into the `portfolio` folder.
3. Open the `portfolio` folder in VS Code (File → Open Folder).
4. Install the **Live Server** extension, then right-click `index.html` → **Open with Live Server**.
   The page refreshes automatically each time you save.

## Easy edits

| What | Where |
|------|-------|
| Colors | `:root { ... }` at the top of `style.css` |
| Typing words in the hero | `roles` array at the top of `script.js` |
| Text, projects, links | `index.html` (search for the section comment, e.g. `PROJECTS`) |
| Project GitHub links | `href` of the "View on GitHub" links — point them at each repo |

## Publish for free

Upload the folder to **GitHub Pages**, **Netlify** or **Vercel** to get a shareable link
for your resume and LinkedIn.
