# Avenrix Healthcare Solutions — Google Sheets Form Integration Guide

This guide walks you through connecting your website's contact form directly to a **Google Sheet**. Every time a client submits an inquiry on the website, a new row will be automatically logged into your Google Spreadsheet in real time.

---

## Step 1: Create a New Google Sheet
1. Open your browser and go to **[sheets.new](https://sheets.new)** (or create a new spreadsheet in your Google Drive).
2. Name your spreadsheet (e.g. **`Avenrix Website Inquiries`**).
3. *(Optional)* You don't need to create any headers manually — the script will automatically create and format the navy-blue header row with all columns on the first submission!

---

## Step 2: Open Google Apps Script
1. Inside your Google Sheet, click **Extensions** in the top menu bar.
2. Click **Apps Script**.
3. A new tab will open with a code editor showing a file named `Code.gs`.

---

## Step 3: Paste the Form Handler Code
1. Delete everything inside the `Code.gs` editor window.
2. Open the file [`google_sheets_integration/Code.gs`](./Code.gs) in your project workspace.
3. Copy its entire content and paste it into the Apps Script editor.
4. Click the **Save** icon (disk icon) or press `Ctrl + S`.

---

## Step 4: Deploy as a Web App (Crucial Settings)
1. In the top right corner of the Apps Script window, click the blue **Deploy** button.
2. Select **New deployment**.
3. In the dialog that opens, click the gear icon (⚙️) next to *Select type* and choose **Web app**.
4. Configure the following fields:
   - **Description**: `Avenrix Form Webhook`
   - **Execute as**: `Me (<your-email@gmail.com>)`
   - **Who has access**: **`Anyone`**  
     *(⚠️ Important: You MUST select "Anyone" so visitors on your website can send their inquiries without logging into Google).*
5. Click **Deploy**.
6. If Google asks for authorization:
   - Click **Authorize access**.
   - Choose your Google account.
   - Click **Advanced** > **Go to Avenrix Form Webhook (unsafe)**.
   - Click **Allow**.
7. Google will show you a **Web app URL** that looks like:  
   `https://script.google.com/macros/s/AKfycbx.../exec`
8. Copy this **Web app URL**.

---

## Step 5: Connect the URL to Your Website
1. Open [`js/main.js`](../js/main.js) in your project.
2. Locate line 256 near the top of `initContactForm()`:
   ```javascript
   const GOOGLE_SHEETS_SCRIPT_URL = '';
   ```
3. Paste your Web app URL between the quotes:
   ```javascript
   const GOOGLE_SHEETS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx.../exec';
   ```
4. Save the file.

---

## Step 6: Test It!
1. Open your website in a browser.
2. Scroll to the **Contact Us** section.
3. Fill out the form with a test inquiry and click **Submit Inquiry**.
4. Watch the button change to **"Sending Inquiry..."** with a loading spinner, then show the **"Inquiry Received"** success screen.
5. Open your Google Sheet — your test inquiry will appear immediately as a newly formatted row!

---

## Fields Logged into Google Sheets
| Column Header | Source Field in Form | Example |
| :--- | :--- | :--- |
| **Submission Timestamp** | Automatic browser date/time | `2026-10-29 00:05:00` |
| **Full Name** | `name="name"` | `Dr. Rajesh Sharma` |
| **Company / Organization** | `name="company"` | `Apex Multi-Speciality Hospital` |
| **Email Address** | `name="email"` | `r.sharma@apexhealth.com` |
| **Phone Number** | `name="phone"` | `+91 98765 43210` |
| **Interested Solution** | `name="product"` | `Modular Operation Theatres` |
| **Project Details / Message** | `name="message"` | `Looking to set up 3 OT suites...` |

---

## Optional: Instant Email Alerts
If you would like Google to send you an instant email every time someone submits an inquiry, open `Code.gs` in Apps Script, uncomment the `MailApp.sendEmail(...)` section (lines 84–97), and re-deploy (*Deploy > Manage deployments > Edit > New version > Deploy*).
