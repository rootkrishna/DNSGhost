# 🕵️‍♂️ DNSGhost

> **Author:** KRISHNA DUBEY  
> 🔥 Founder of HEXAFORCE ALLIANCE | VIOLENT CYBER FORCE | CYBER GUARDIAN | ANTI-CYBER CRIME TASKFORCE  
> 🧠 Ethical Hacker • AI Specialist • Cyber Warrior

---

## 👻 What is DNSGhost?

**DNSGhost** is a high-speed subdomain scanner and DNS reconnaissance tool built for ethical hackers, red teamers, and cyber researchers.

It helps uncover hidden subdomains using a powerful wordlist-based brute-force technique.

---

## ⚔️ Features

- 🚀 Ultra-fast DNS resolution
- 📡 Reveals hidden & forgotten subdomains
- 🧠 Optimized for large wordlists
- 💥 Terminal-based with clean output
- 📁 Easy-to-edit Python script

---

## 🧪 How It Works

- DNSGhost takes a **target domain** and a **wordlist** of possible subdomains.
- It attempts to resolve each one.
- Any valid subdomain found is printed in green ✅.

---

## 🔧 Requirements

- Python 3.x  
- Internet Connection  
- A wordlist (e.g., `subdomains.txt`)

Install dependencies:
```bash
pip install -r requirements.txt

python dnsghost.py <target-domain> <wordlist.txt>
