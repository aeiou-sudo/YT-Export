# 📺 YT-Export: Automated Media Archival Framework

**YT-Export** is a professional-grade YouTube downloader designed to overcome modern web integrity challenges. By integrating **PO-Token (Proof of Origin)** injection with a fully automated **CI/CD pipeline**, this project ensures reliable, high-speed media extraction even in restricted environments.

---

## 🚀 System Overview

The core of this project is the synergy between localized extraction logic and cloud-based automation.

### 1. The Engine (`downloader.py`)
This script uses a customized `yt-dlp` configuration to bypass "BotGuard" and `403 Forbidden` errors.
* **Integrity Handshake**: Injects specific `PO_TOKEN` and `VISITOR_DATA` directly into the YouTube extractor arguments.
* **Environment Matching**: Mimics the `WEB` client version `2.20260403` with a matching Chrome User-Agent to ensure the server recognizes the request as a legitimate browser session.
* **Muxing**: Utilizes **FFmpeg** to merge high-bitrate video and audio streams into a single `.mkv` container.

### 2. The Orchestrator (`main.yml`)
Located in `.github/workflows/`, this YAML file transforms a simple script into a **Cloud-Based Downloader**.
* **GitHub Actions Workflow**: Runs on `ubuntu-latest`, providing a clean, high-bandwidth environment for every download.
* **Automated Dependency Injection**: Automatically sets up **Python 3.10**, **Node.js 20** (for JS execution), and **FFmpeg**.
* **Secure Authentication**: Uses GitHub Secrets (`YT_COOKIES`) to securely inject session data at runtime without exposing credentials in the codebase.

---

## 🛠 Features

* **Manual Trigger**: Uses `workflow_dispatch` to allow users to paste a URL directly into the GitHub UI.
* **Bypass Technology**: Specifically configured to handle the **PO-Token** challenge, restoring access to 4K and unplayable formats.
* **Artifact Delivery**: Successfully downloaded media is automatically bundled and made available as a GitHub Artifact for easy retrieval.
* **JS Engine Integration**: Forces a clean symlink to `node` within the runner to ensure `yt-dlp` can handle YouTube’s signature decryption in real-time.

---

## 📂 Project Structure

| File | Role | Key Function |
| :--- | :--- | :--- |
| `downloader.py` | **Core Logic** | Handles `PO_TOKEN` injection and stream extraction. |
| `.github/workflows/main.yml` | **CI/CD Pipeline** | Manages the build environment and runs the downloader in the cloud. |
| `cookies.txt` | **Session Data** | (Generated at runtime) Provides authenticated access to YouTube. |

---

## 🚦 Usage via GitHub Actions

1.  Navigate to the **Actions** tab in your repository.
2.  Select the **YouTube Downloader Automation** workflow.
3.  Click **Run workflow**.
4.  Enter the YouTube URL in the `video_url` input field.
5.  Once the job completes, download your media from the **Summary** page under **Artifacts**.

---

## ⚙️ Configuration Detail (Technical)

The downloader is tuned for the **2026 Web Client** environment:
* **Node Path**: Explicitly set to `/usr/local/bin/node` to facilitate complex signature decryption.
* **Format Selection**: Set to `bestvideo+bestaudio/best` to ensure maximum quality archival.
* **Wait for Input**: The script reads the URL from `stdin`, allowing the GitHub Action to pipe inputs directly from the UI.

---

## ⚖️ Disclaimer
This tool is intended for **archival and research purposes only**. Users are responsible for adhering to YouTube's Terms of Service and local copyright regulations.

---
*Built for reliability. Powered by GitHub Actions.*

---

This project is for educational and research purposes only. Bypassing YouTube's integrity systems may violate their Terms of Service. Use responsibly.

---

*Generated for the Research Community @ MACE/NIT.*
