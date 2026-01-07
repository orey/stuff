/*****************************************************************
This script creates 2 mails per each mail received.
The function forwardMessage can be run in recuurent batches
********************************************************************/
const EMAIL="toto@titi.com";

function sendPlain(subject, content) {
  GmailApp.sendEmail(EMAIL, subject, content)
}

function sendHtml(subject, htmlContent) {
  GmailApp.sendEmail(EMAIL, subject, "", {htmlBody:htmlcontent})
}

function forwardMessage(){
  // find unread messages
  var threads = GmailApp.search("is:unread AND in:Inbox");
  
  for (var thread of threads) {
    var mymessages = thread.getMessages();
    var count = 0;

    for (var message of mymessages){
      logMessage(message);
      // We parse the messages from the last hour only
      // if message arrived after "now", delta <0, it will be processed later by the trigger
      if (message.isUnread()) {
        message.forward(EMAIL);
        Logger.log("Message forwarded. From: " + message.getFrom() + " - Subject: " + message.getSubject());
        message.markRead(); // not to forward it again in the next run
        count= count+1;
        if (message){
          GmailApp.sendEmail(EMAIL,
                             "HEADER: " + message.getSubject(),
                             "\n---\n\nFrom: " + message.getFrom() + "\nTo: " + message.getTo() + "\nCc: " + message.getCc() + "\n\n---\n\n"
                             );
        }
      }
    }
    Logger.log("Forwarded " + count + " messages.")
  }
}

function logMessage(m) {
  Logger.log("Date: " + m.getDate() + " - From: " + m.getFrom()
              + " - Subject: " + m.getSubject() + " - Is Unread: " + m.isUnread());
}
