# Hostinger pe Git se Website Auto-Update karne ka Guide 🚀

Aapki website ko modularize kar diya gaya hai! Ab HTML, CSS aur JavaScript sabhi alag-alag files me hain:
- `index.html` (Main website structure)
- `css/style.css` (Design & Styling)
- `js/script.js` (Interactive features)
- `.github/workflows/deploy.yml` (GitHub Actions workflow for Hostinger)

---

## 🛠️ Step 1: Apne Computer se GitHub par Code Push karein

1. Terminal / Command Prompt kholein apne website folder (`d:\ansu\website`) me.
2. Niche diye gaye commands run karein:

```bash
git init
git add .
git commit -m "Modularized HTML CSS JS and added Hostinger deployment setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.name.git
git push -u origin main
```
*(Yahan `YOUR_USERNAME/YOUR_REPOSITORY` ki jagah apna GitHub repository link dalein).*

---

## ⚡ Step 2 (Option A - Recommended): Hostinger Direct Git Deployment + Auto-Update

Hostinger me built-in Git deployment feature hota hai jisse GitHub par push karte hi website auto-update ho jaati hai.

### Implementation Steps:
1. **Hostinger hPanel** me login karein (`hpanel.hostinger.com`).
2. **Advanced** section me **Git** par click karein.
3. Yahan details bharein:
   - **Repository Branch**: `main`
   - **Repository URL**: `https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git`
   - **Install Path**: `/public_html` (ya domain ka folder)
4. **Create** button par click karein.
5. Setup hone ke baad Hostinger aapko ek **Webhook URL** dikhayega.
6. **GitHub Webhook Add karein**:
   - Apne GitHub repository me jayein -> **Settings** -> **Webhooks** -> **Add webhook**.
   - **Payload URL**: Hostinger ka diya hua Webhook URL paste karein.
   - **Content type**: `application/json`
   - **Add webhook** par click kar dein.

**Done!** Ab jab bhi aap GitHub par commit & push karenge, Hostinger par aapki website bina kisi manual upload ke **automatic update** ho jayegi.

---

## ⚙️ Step 2 (Option B): GitHub Actions (FTP Deployment)

Agar aap Hostinger ke FTP ke zariye auto-update chahte hain:

1. Hostinger hPanel se apna **FTP Host, FTP Username, aur FTP Password** note karein (**Files -> FTP Accounts**).
2. Apne GitHub Repository me jayein:
   - **Settings** -> **Secrets and variables** -> **Actions** -> **New repository secret**.
3. Teeno Secrets add karein:
   - `HOSTINGER_FTP_SERVER` = `ftp.yourdomain.com` (ya FTP Host IP)
   - `HOSTINGER_FTP_USERNAME` = `u123456789` (Aapka FTP Username)
   - `HOSTINGER_FTP_PASSWORD` = `Aapka FTP Password`
4. `.github/workflows/deploy.yml` file pehle se project me bana di gayi hai.
5. Jaise hi aap code push karenge, GitHub Actions automatic Hostinger FTP server par saare updated files push kar dega!

---

## 💡 Quick Tips:
- Main file `index.html` hai jo Hostinger hPanel direct load karta hai.
- Assets / images (jaise `assets/hero_luxury_villa.png`) folder ko bhi repository me rakhein taaki live site par saari images proper load hon.
