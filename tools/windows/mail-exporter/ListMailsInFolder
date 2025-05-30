Sub ListMailsInFolder()

    Dim objNS As Outlook.NameSpace
    Dim objFolder As Outlook.MAPIFolder

    Set objNS = GetNamespace("MAPI")
    Set objFolder = objNS.Folders.GetFirst ' folders of your current account
    Rem Set objFolder = objFolder.Folders("Foldername").Folders("Subfoldername")
    Set objFolder = objFolder.Folders("Boîte de réception")
    
    Debug.Print Now
    Debug.Print ("---------------------------------------------------")
    
    For Each Item In objFolder.Items
        If TypeName(Item) = "MailItem" Then
            Dim myitem As MailItem
            Set myitem = Item
            
            Dim datedisplay As String
            datedisplay = Format(myitem.CreationTime, "yyyymmdd-hhmmss")
            
            Dim conv As String
            conv = CleanString(myitem.ConversationTopic)
            Rem Debug.Print myitem.CreationTime, Format(myitem.CreationTime, "yyyymmdd-hhmmss")
            Rem Debug.Print myitem.ConversationTopic
            
            Dim fullname As String
            fullname = datedisplay & "-" & conv & ".msg"
            myitem.SaveAs "C:\Users\a876246\Documents\temp\" & fullname
            Debug.Print "OK => " & fullname
            
            Dim atts As Attachments
            Set atts = myitem.Attachments
            Debug.Print atts.Count
            If atts.Count <> 0 Then
                For Each att In atts
                    Dim myatt As Attachment
                    Set myatt = att
                    Debug.Print myatt.FileName
                    myatt.SaveAsFile "C:\Users\a876246\Documents\temp\" & datedisplay & myatt.FileName
                    
                    
                Next att
            End If
            

            
            
            
            
        End If
    Next
    Debug.Print "End"
    Debug.Print "************************************"
End Sub

Function CleanString(mystr) As String
Const NC As String = "_"
Dim temp As String
temp = mystr
Dim arr As Variant
arr = Array(":", "/", "\", " ", "»", "«", Chr(34))

For Each ch In arr
    temp = Replace(temp, ch, NC)
Next ch

If Len(temp) > 70 Then
    temp = Left(temp, 65) & "(...)"
End If

CleanString = temp
End Function

