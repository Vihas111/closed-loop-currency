# Development Workflow

## 1. Pull Latest Changes From Dev Branch

git checkout dev

git pull origin dev

---

## 2. Create Feature Branch

git checkout -b feature/<feature-name>

Example:

git checkout -b feature/auth

---

## 3. Work on Your Feature

Make your code changes.

---

## 4. Add and Commit Changes

git add .

git commit -m "Add auth API"

---

## 5. Push Feature Branch

git push -u origin feature/auth

---

## 6. Create Pull Request

GitHub Flow:

feature/* → dev

DO NOT push directly to:
- dev
- main

---

## 7. Wait for CI Checks

GitHub Actions will run automatically:
- Flutter checks
- Backend tests
- Linting
- Build verification

Fix any failing checks before merge.

---

## 8. Merge After Approval

Merge only after:
- CI passes
- PR is reviewed

---

# Important Rules

- Never push directly to `main`
- Always pull latest `dev` before starting work
- Use one feature branch per task
