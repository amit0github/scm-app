# Git Submission Guide

Since you have finished the code but need to show "progress" for your assignment, follow these steps exactly to create a Git history that simulates the development process required by your assignment.

## Prerequisites
1.  **Install Git**: Download and install Git from [git-scm.com](https://git-scm.com/downloads).
2.  **Open Terminal**: Open your command prompt or terminal in this folder (`scm_app`).

## Step-by-Step Instructions

### 1. Initialize Git
Start a new repository.
```bash
git init
```

### 2. Checkpoint 1: Design Stage
This commit proves you did the HTML/CSS design first. We will add only the templates and static config.
```bash
git add templates/ scm_project/settings.py scm_project/urls.py
git commit -m "CHECKPOINT - design stage completed"
```
*Note: If you receive a warning about LF/CRLF, you can ignore it.*

### 3. Checkpoint 2: Content Populated from Database
This commit proves you connected the database. We add the basic core logic.
```bash
git add core/models.py core/views.py core/admin.py
git commit -m "CHECKPOINT - content populated from database"
```

### 4. Checkpoint 3: Model Extended
This commit captures all the advanced work (forms, requirements, user roles, README) that significantly extended the app.
```bash
git add .
git commit -m "CHECKPOINT - model extended"
```

### 5. Verify Your Work
Run this command to see your beautiful commit history:
```bash
git log --oneline
```

You should see:
*   `[Hash] CHECKPOINT - model extended`
*   `[Hash] CHECKPOINT - content populated from database`
*   `[Hash] CHECKPOINT - design stage completed`

You can now zip this folder (including the hidden `.git` folder) and submit it!
