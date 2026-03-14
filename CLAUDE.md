# Instructions for Claude

This file contains instructions for Claude to follow when working on this project.

## Project Notes File
There is a `PROJECT_NOTES.md` file in this folder that serves as the owner's reference document for everything related to this business and website.

**You must keep PROJECT_NOTES.md up to date.** Specifically:

- When a new service or account is created (hosting, email, shop, etc.), add it to the Accounts Summary table and add relevant details in the appropriate section
- When a to-do item is completed, mark it as done with [x] or remove it from the list
- When new to-do items come up, add them to the Outstanding To-Dos list
- When the website design changes significantly (new fonts, colors, sections, layout), update the Design section
- When photos are added or removed, update the photo counts in the Design section
- When selling or hosting decisions are made, update those sections
- When DNS records are added or changed, update the Email section

## Git & GitHub
- The website is hosted on GitHub Pages
- After making any changes to website files, commit and push to GitHub:
  ```
  cd /Users/knitwit1/website
  git add .
  git commit -m "description of what changed"
  git push
  ```
- When the GitHub username and repository name are known, record them in PROJECT_NOTES.md and here
- GitHub username: janetlhardy
- GitHub repository URL: https://github.com/janetlhardy/werecured
- GitHub Pages URL: TBD
- Custom domain: werecured.ca

## File Structure
- All website files live in `/Users/knitwit1/website/`
- `index.html` — the entire website (single file)
- `images/` — all product photos as .jpg files
- `.gitignore` — excludes .HEIC, .aae, and .DS_Store files from git

## General Project Notes
- The owner has no coding experience — always explain steps in plain, simple language
- The website is a single `index.html` file — avoid splitting it into multiple files unless absolutely necessary
- Photos were originally HEIC (iPhone) format and were converted to JPG using the macOS `sips` command
- The owner uses Dashlane to store passwords
- When suggesting new services, prefer free or low-cost options and beginner-friendly interfaces
