# YouTube PO-Token Extraction & Automation

This repository provides a technical framework for identifying, extracting, and implementing **Proof of Origin (PO) Tokens** and **Visitor Data** required to bypass `403 Forbidden` errors and playback throttling on YouTube.

## 📋 Overview

YouTube uses a client-side integrity system (BotGuard) to verify that requests originate from a legitimate browser environment. The **PO Token** is a cryptographic string generated after a series of browser challenges. Without this token, automated tools (like `yt-dlp` or custom scrapers) are increasingly flagged as bots.

### Key Components
| Component | Description |
| :--- | :--- |
| **PO Token** | Proof of Origin; validates the session integrity. |
| **Visitor Data** | A unique identifier (`visitorData`) linked to the initial request. |
| **Integrity Service** | The `serviceIntegrityDimensions` block in the internal YouTube API. |

---

## 🛠 Extraction Methods

### 1. Manual Extraction (Browser DevTools)
The most reliable way to find a working token is via a manual session:
1. Open a YouTube video in a clean browser window (Incognito recommended).
2. Open **DevTools (F12)** > **Network Tab**.
3. Filter for `v1/player`.
4. Under the **Payload** tab, navigate to:
   `context` > `serviceIntegrityDimensions` > **`poToken`**.
5. Copy both the `poToken` and the `visitorData` found under `context` > `client`.

### 2. Automated Extraction (Headless Browser)
To automate this, use a browser automation tool (Playwright/Puppeteer) to solve the challenge:

```javascript
// Example logic for token interception
const { chromium } = require('playwright');

async function getTokens() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  await page.goto('https://www.youtube.com/watch?v=YOUR_VIDEO_ID');
  
  // Intercept the player request
  const [request] = await Promise.all([
    page.waitForRequest(res => res.url().includes('v1/player')),
  ]);

  const postData = JSON.parse(request.postData());
  const poToken = postData.context.serviceIntegrityDimensions.poToken;
  
  console.log("PO_TOKEN:", poToken);
  await browser.close();
}
```

---

## 🚀 Implementation

Once you have the token, it must be passed in the `context` object of your API requests.

### Request Body Structure
```json
{
  "context": {
    "client": {
      "clientName": "WEB",
      "clientVersion": "2.2024xxxx",
      "visitorData": "YOUR_VISITOR_DATA"
    },
    "serviceIntegrityDimensions": {
      "poToken": "YOUR_PO_TOKEN"
    }
  },
  "videoId": "v3cL2VfFkVg"
}
```

---

## ⚠️ Troubleshooting & Limits

* **Token Expiry:** PO Tokens are session-bound. If you encounter a `403` after a period of success, the token has likely expired or the `visitorData` mismatch triggered a flag.
* **IP Binding:** Tokens generated on one IP address (e.g., your local machine) may not work when used on a different IP (e.g., a VPS or GitHub Action).
* **BotGuard Updates:** YouTube frequently updates the VM constants used to generate these tokens. If extraction fails, check for updates in the `bg.js` script on the YouTube frontend.

---

## ⚖️ Disclaimer
This project is for educational and research purposes only. Bypassing YouTube's integrity systems may violate their Terms of Service. Use responsibly.

---

*Generated for the Research Community @ MACE/NIT.*
