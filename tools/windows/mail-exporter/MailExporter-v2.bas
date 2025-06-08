Attribute VB_Name = "MailExporter"
Option Explicit

Const test As String = "test"
Const OUTPUTFOLDER = "C:\ProgramData\orey\data\outlook\test2\"

'Private Type T_ChosenFolder
'    index As Integer
'    folder As Outlook.MAPIFolder
'End Type

'=====================================================================
' This function get the full path to extract with the various folders
'=====================================================================
Sub PathToExtract()
    Dim objNS As Outlook.NameSpace
    Dim nb As Integer ' nb of mailboxes
    Dim choices As String ' list of mailbox in text
    Dim mailb As Variant ' choice of mailbox
    
    
    Dim f As Outlook.folder
    Dim nbbox, j As Integer
    Dim res As Variant
    
    ' thefolders is a collection because it is complicated to have a recursive function
    ' returning a type Outlook.folder
    Dim theFolders As New Collection
    
    '*** Step 1: getting the mailbox (not the exact same interface than the MAPI Folders)
    ' main namespace
    Set objNS = GetNamespace("MAPI")
    nb = objNS.Folders.Count
    For j = 1 To nb
        Set f = objNS.Folders.item(j)
        choices = choices & j & " " & f.name + vbNewLine
    Next j
    Debug.Print choices
    
    mailb = InputBox("Choose the number corresponding to the mailbox" & vbNewLine & choices, "Mailbox choice")
    If mailb = "" Then
        MsgBox "No mailbox was selected. Exiting..."
        End
    End If
    
    theFolders.Add objNS.Folders.item(mailb)
    
    '*** Step 2: calling the recursive function for the choice of folders
    Call ChooseOneFolder(theFolders)
    
    Dim thepath As String
    Dim elem As Outlook.folder
    thepath = ""
    For Each elem In theFolders
        thepath = thepath & "/" & elem
    Next elem
    Dim confirm As Variant
    confirm = MsgBox("Do you confirm you want to export the folder: " & vbNewLine & _
                        thepath, vbYesNo, "Confirmation")
    If confirm = vbNo Then
        MsgBox ("Doing nothing. Exiting...")
        End
    End If
    
    '*** Step 3: exporting the folder
    Dim realcount As Integer
    Dim exportFolder As Outlook.folder
    Set exportFolder = theFolders.item(theFolders.Count) ' C'est le dernier
    realcount = ExportTheFolder(exportFolder)

    Debug.Print "Stop"
    

End Sub

'---------------------------------------------------------
' Recursive function returning the Outlook.Folder chosen by the user
' returns 0 if there are no subfolders, other wise returns a
' folder
'---------------------------------------------------------
Function ChooseOneFolder(collec As Collection)

    Dim fold, f As Outlook.folder
    Dim nb, j As Integer
    Dim choices As String

    ' getting the last folder
    Set fold = collec.item(collec.Count)

    nb = fold.Folders.Count
    
    ' There are no subfolders, exiting
    If nb = 0 Then
        ' we can stop the recursive loop
        Exit Function
    End If
    
    ' We build the text with the folders to choose from
    choices = "Here are the folders to choose from:" & vbNewLine & "[0] " _
                & fold.name & vbNewLine
    
    For j = 1 To nb
        Set f = fold.Folders.item(j)
        choices = choices & "-> [" & j & "] " & f.name + vbNewLine
    Next j
    
    Debug.Print choices
    
Question:
    Dim x As Variant
    x = InputBox("Choose the number corresponding to the folder" & vbNewLine & choices, _
                    "Folder choice")
    If CInt(x) < 0 Or CInt(x) > nb = "" Then
        MsgBox "Error in typing"
        GoTo Question
    End If
    
    If x = 0 Then
        ' The previous choice in the stack is correct
        ' we can stop the recursive loop
        Exit Function
    Else
        ' the number pick may have subfolders
        collec.Add fold.Folders.item(CInt(x))
        ' calling recursively for subfolders
        Call ChooseOneFolder(collec)
        Exit Function
    End If
    
End Function


Function ExportTheFolder(folder As Outlook.folder) As Integer
    ' To measure elapse time of treatment
    Dim StartTime As Double
    Dim MinutesElapsed As String
    StartTime = Timer

    Dim nb, mmax, i, realcount As Integer
    Dim limit As Boolean
    Dim item, att As Variant
    
    nb = folder.items.Count
    
    Dim x As Variant
    x = InputBox("There are " & CStr(nb) & " elements in the folder. How many do you want?" & _
                    vbNewLine & "[0] means all of them", "Choice of number")
    If x = "" Then
        MsgBox "Exiting..."
        End
    End If
    
    ' TODO: Il faudrait mettre le choix du folder
    
    mmax = CInt(x)
    If mmax = 0 Then
        limit = False
    Else
        limit = True
        i = 0
    End If
    
    realcount = 0
    
    For Each item In folder.items
        If TypeName(item) = "MailItem" Then
            ' controlling the nb
            If limit Then
                i = i + 1
                If i = mmax Then
                    MsgBox "Reached maximum number of item exported: " & mmax
                    Exit For
                End If
            End If
            Dim myitem As MailItem
            Set myitem = item
            
            Dim datedisplay As String
            datedisplay = Format(myitem.CreationTime, "yyyymmdd-hhmmss")
            
            Dim conv As String
            conv = CleanString(myitem.ConversationTopic)
            
            Dim sender As String
            sender = CleanString(myitem.SenderName)
            
            'Building name of the file
            Dim fullname, textname As String
            fullname = datedisplay & "-(" & sender & ")-" & conv & ".msg"
            textname = datedisplay & "-(" & sender & ")-" & conv & ".txt"
            
            ' Don't export the file if it already was exported
            If Not IsFile(OUTPUTFOLDER & fullname) Then
                myitem.SaveAs OUTPUTFOLDER & fullname
                myitem.SaveAs OUTPUTFOLDER & textname, olTXT
                realcount = realcount + 1
                Debug.Print "OK => " & fullname
            Else
                Debug.Print "File already exists => " & fullname
            End If
            
            'Export the attachments
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
                            realcount = realcount + 1
                        Else
                            Debug.Print "File already exists"
                        End If
                Next att
            End If
        End If
    Next
    
    'Determine how many seconds code took to run
    MinutesElapsed = Format((Timer - StartTime) / 86400, "hh:mm:ss")

    MsgBox "Real number of files created: " & realcount & " in " & MinutesElapsed & " minutes", vbInformation
    
    ExportTheFolder = realcount

End Function



Function CleanString(mystr) As String
Const NC As String = "_"
Dim temp As String
Dim ch As Variant

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
