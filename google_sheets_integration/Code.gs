/**
 * ============================================================================
 * AVENRIX HEALTHCARE SOLUTIONS - GOOGLE SHEETS FORM HANDLER
 * ============================================================================
 * This Google Apps Script connects the Avenrix website contact form
 * directly to your Google Spreadsheet.
 *
 * FEATURES:
 * - Auto-creates formatted header row on first submission.
 * - Handles concurrent submissions safely with LockService.
 * - Parses JSON and form-encoded data.
 * - Optional instant email alert to the sheet owner.
 * ============================================================================
 */

function doPost(e) {
  var lock = LockService.getScriptLock();
  // Wait up to 30 seconds for concurrent writes
  lock.tryLock(30000);

  try {
    var doc = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = doc.getActiveSheet();

    // If the sheet is empty, automatically create and format the header row
    if (sheet.getLastRow() === 0) {
      var headers = [
        "Submission Timestamp",
        "Full Name",
        "Company / Organization",
        "Email Address",
        "Phone Number",
        "Interested Solution",
        "Project Details / Message"
      ];
      sheet.appendRow(headers);

      // Apply Avenrix brand styling to header row
      var headerRange = sheet.getRange(1, 1, 1, headers.length);
      headerRange.setFontWeight("bold");
      headerRange.setFontSize(11);
      headerRange.setBackground("#0D233A"); // Avenrix Dark Navy
      headerRange.setFontColor("#FFFFFF");
      headerRange.setHorizontalAlignment("center");
      headerRange.setVerticalAlignment("middle");
      sheet.setRowHeight(1, 38);
      sheet.setFrozenRows(1);
    }

    // Parse input from JSON string or form post parameters
    var data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (parseErr) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    var timestamp = data.submittedAt || Utilities.formatDate(new Date(), Session.getScriptTimeZone() || "GMT", "yyyy-MM-dd HH:mm:ss");
    var name = data.name || "N/A";
    var company = data.company || "N/A";
    var email = data.email || "N/A";
    var phone = data.phone || "N/A";
    var product = data.product || "General Inquiry";
    var message = data.message || "No message provided";

    // Append the row to Google Sheets
    sheet.appendRow([
      timestamp,
      name,
      company,
      email,
      phone,
      product,
      message
    ]);

    // Optional: Format the newly added row
    var lastRow = sheet.getLastRow();
    var newRowRange = sheet.getRange(lastRow, 1, 1, 7);
    newRowRange.setVerticalAlignment("middle");
    sheet.setRowHeight(lastRow, 30);

    // Optional: Send instant email notification to the sheet owner
    // Uncomment the lines below to receive an email for every new submission:
    /*
    var recipientEmail = Session.getActiveUser().getEmail();
    var subject = "New Project Inquiry - " + name + (company !== "N/A" ? " (" + company + ")" : "");
    var emailBody = "New project inquiry received from Avenrix Healthcare Solutions website:\n\n" +
                    "• Full Name: " + name + "\n" +
                    "• Company: " + company + "\n" +
                    "• Email: " + email + "\n" +
                    "• Phone: " + phone + "\n" +
                    "• Interested Solution: " + product + "\n\n" +
                    "• Project Message:\n" + message + "\n\n" +
                    "• Submitted At: " + timestamp + "\n";
    MailApp.sendEmail(recipientEmail, subject, emailBody);
    */

    return ContentService
      .createTextOutput(JSON.stringify({ result: "success", row: lastRow }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: "error", error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);

  } finally {
    lock.releaseLock();
  }
}

/**
 * Friendly status check if the Web App URL is opened directly in a browser
 */
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({
      status: "online",
      message: "Avenrix Healthcare Solutions Form Submission Webhook is active."
    }))
    .setMimeType(ContentService.MimeType.JSON);
}
