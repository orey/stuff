/*
The function to run is runMerge
Integrate your docs IDs in the document
*/


function mergeGoogleDocs(docIds) {
  const mergedDoc = DocumentApp.create("EhP7 - Analysis of the offers4"); // Creates a new document
  const body = mergedDoc.getBody();

  docIds.forEach(id => {
    const doc = DocumentApp.openById(id);
    const docBody = doc.getBody();

    // Append content of each document to the merged document
    for (let i = 0; i < docBody.getNumChildren(); i++) {
      // The content of a tab in a Google Docs document. The Body may contain ListItem, Paragraph, Table,
      // and TableOfContents elements
      // (extracted from here: https://developers.google.com/apps-script/reference/document/body)
      const element = docBody.getChild(i).copy();
      switch(element.getType()){
        case DocumentApp.ElementType.PARAGRAPH:
          body.appendParagraph(element.asParagraph());
          Logger.log("PARAGRAPH");
          break;
        case DocumentApp.ElementType.TABLE:
          body.appendTable(element.asTable());
          Logger.log("TABLE");
          break;
        case DocumentApp.ElementType.LIST_ITEM:
          body.appendListItem(element.asListItem());
          Logger.log("LIST_ITEM");
          break;       
        default:
          Logger.log("Zut");
          Logger.log(element.getType());
      }

    }
    body.appendPageBreak(); // Add a page break after each document
  });

  Logger.log("Merged Document URL: " + mergedDoc.getUrl());
}

function runMerge() {
  const docIds = [
    '13Wpvbw35D8tVl-bBSv7BEW2c4bQarJMJeNobPUYZ568', 
    '1eUKexPlYcwr5D9sEX1wxW4O-QCiBKRkpu3KHPTrw140', 
    '1nkv0aUV54nxz2wl7iworNjnhHm1uONVr87UgwrwhoKk',
    '19qOPiZ6rPYgW9BVU7FHX-tJDmP3z5ZK1EYAV-BbJGm8',
    '180kWx1eiFXAngpwaeY3hr6GTaDTr568MxuwduIq0Jkc',
    '1a4GZwpUCSO1usxIpQuSMPhjSHKOloZfsMuMm-lPCev0',
    '17XuphilXOA7VSggSFNZtQmtLVxTAxRLPSYQQI5cSULY'
  ]; // Replace with your actual document IDs

  mergeGoogleDocs(docIds);
}

