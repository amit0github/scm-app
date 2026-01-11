# How to Upload to GitHub

Yes, **Git** and **GitHub** are different!
*   **Git** is the **tool** installed on your computer that saves versions of your code (like the "Checkpoints" we created).
*   **GitHub** is the **website** where you upload those saved versions so others (like your teacher) can see them using the internet.

To upload your project, follow these steps **after** you have done the steps in `git_guide.md`.

## Step 1: Create a Repository on GitHub
1.  Log in to [GitHub.com](https://github.com/).
2.  Click the **+** icon in the top-right corner and select **New repository**.
3.  **Repository name**: Type `scm-app` (or whatever you want to name it).
4.  **Description**: "Supply Chain Management app for school assignment".
5.  **Public/Private**: Choose **Public** (unless your assignment says otherwise).
6.  **Do NOT check** "Add a README file" (you already have one locally).
7.  Click **Create repository**.

## Step 2: Link Your Computer to GitHub
GitHub will show you a page with commands. Look for the section **"…or push an existing repository from the command line"**.

Run these commands in your project folder (where you ran `git init`):

1.  **Rename your branch to main** (standard practice):
    ```bash
    git branch -M main
    ```

2.  **Add the remote link** (Copy this exact line from YOUR GitHub page, it looks like this):
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/scm-app.git
    ```

3.  **Push your code**:
    ```bash
    git push -u origin main
    ```

## Step 3: Check Your Work
Refresh the page on GitHub. You should now see all your files (`core`, `templates`, `README.md`) listed there!

You can click on "Commits" (usually a little clock icon) to see your "Checkpoints" listed exactly as you created them.
