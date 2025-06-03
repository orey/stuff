Const test As String = "test"
Const OUTPUTFOLDER = "C:\ProgramData\orey\data\outlook\test1\"

'----------------------------------------------------------------
' The objective of that function is to get the mailbox and folder
' The treatment could be made generic as we are just following a tree
' of IMAP folders (code currently duplicated)
'----------------------------------------------------------------
Function WhatMailbox()

    Dim objNS As Outlook.NameSpace
    ' main namespace
    Set objNS = GetNamespace("MAPI")
    
    ' getting mailboxes (first level of "folders")
    Dim choices As String
    
    Dim nb As Integer
    nb = objNS.Folders.Count
    
    For j = 1 To nb
        Set f = objNS.Folders.Item(j)
        Debug.Print j & " " & f.Name
        choices = choices & j & " " & f.Name + vbNewLine
    Next j
    Debug.Print choices
    
    Dim x As Variant
    x = InputBox("Choose the number corresponding to the folder" & vbNewLine & choices, "Mailbox choice")
    If x = "" Then
        MsgBox "No mailbox was selected. Exiting..."
        WhatMailbox = ""
    End If
    
    ' getting folders in mailbox
    nb = objNS.Folders.Item(x).Folders.Count
    choices = ""
    For j = 1 To nb
        Set f = objNS.Folders.Item(x).Folders.Item(j)
        Debug.Print j & " " & f.Name
        choices = choices & j & " " & f.Name + vbNewLine
        ' warning: the index 0 is not used
    Next j
    
    Dim y As Variant
    y = InputBox("Choose the number corresponding to the folder" & vbNewLine & choices, "Folder choice")
    If y = "" Then
        MsgBox "No folder was selected. Exiting..."
        WhatMailbox = ""
    End If
    
    ' Preparing output
    Dim output(2) As Integer
    output(0) = x
    output(1) = y
    
    WhatMailbox = output

End Function


Sub ExportMailsInFolder()

    Dim StartTime As Double
    Dim MinutesElapsed As String
    StartTime = Timer

    Dim objNS As Outlook.NameSpace
    Dim objFolder As Outlook.MAPIFolder

    ' Get the root folder
    Set objNS = GetNamespace("MAPI")
    
    Dim choices As Variant
    choices = WhatMailbox
    Set objFolder = objNS.Folders.Item(choices(0)).Folders.Item(choices(1))
    
    Debug.Print "stop"
    
    Rem ======================== protection contre le nombre d'éléments sauvés
    Dim x As Variant
    
    x = InputBox("How many items? (integer)" & vbNewLine & _
                 "There are " & objFolder.items.Count & " elements in the selected folder." & vbNewLine & _
                 "An empty field abort the treatment." & vbNewLine & _
                 "'0' indicates all elements in folder are selected.", "Mail Exporter")
    If x = "" Then
        MsgBox "No mails are selected. Exiting..."
        Exit Sub
    End If
    
    ' TODO recall the output folder to confirm
        
    Dim mmax, i As Integer
    Dim limit As Boolean
    limit = False
    mmax = Val(x)
    If mmax = 0 Then
        limit = True
    End If
    i = 0
    
    ' Counting the real operations if the folder is reused
    Dim realCount As Integer
    realCount = 0
    
    For Each Item In objFolder.items
        If TypeName(Item) = "MailItem" Then
            ' controlling the nb
            If limit Then
                i = i + 1
                If i = mmax Then
                    MsgBox "Reached maximum number of item exported: " & mmax
                    Exit For
                End If
            End If
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
            If Not IsFile(OUTPUTFOLDER & fullname) Then
                myitem.SaveAs OUTPUTFOLDER & fullname
                realCount = realCount + 1
            Else
                Debug.Print "File already exists"
            End If
            Debug.Print "OK => " & fullname
            
            Dim atts As Attachments
            Set atts = myitem.Attachments
            Debug.Print atts.Count
            If atts.Count <> 0 Then
                For Each att In atts
                    ' There are some strange attachments that make Outlook break
                    On Error Resume Next
                        Dim myatt As Attachment
                        Set myatt = att
                        'Debug.Print myatt.FileName
                        If Not IsFile(OUTPUTFOLDER & datedisplay & "-" & myatt.FileName) Then
                            myatt.SaveAsFile OUTPUTFOLDER & datedisplay & "-" & myatt.FileName
                            realCount = realCount + 1
                        Else
                            Debug.Print "File already exists"
                        End If
                Next att
            End If
        End If
    Next
    
    'Determine how many seconds code took to run
    MinutesElapsed = Format((Timer - StartTime) / 86400, "hh:mm:ss")

    MsgBox "Real number of files created: " & realCount & " in " & MinutesElapsed & " minutes", vbInformation
    
    Debug.Print "*********** END *************************"
End Sub

Function CleanString(mystr) As String
Const NC As String = "_"
Dim temp As String
temp = mystr
Dim arr As Variant
arr = Array(":", "/", "\", " ", "»", "«", Chr(34), ">", "<", "?", "|")

For Each ch In arr
    temp = Replace(temp, ch, NC)
Next ch

If Len(temp) > 70 Then
    temp = Left(temp, 65) & "(...)"
End If

CleanString = temp
End Function

Function IsFile(ByVal fName As String) As Boolean
'Returns TRUE if the provided name points to an existing file.
'Returns FALSE if not existing, or if it's a folder
    On Error Resume Next
    IsFile = ((GetAttr(fName) And vbDirectory) <> vbDirectory)
End Function
