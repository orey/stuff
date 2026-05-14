' =============================================================================
' ExportMails.bas
' Exports Inbox mails received since last run to a flat folder.
' One .txt file per mail (metadata + body), attachments saved alongside.
' Last-run date is persisted in the Windows registry.
' =============================================================================

Option Explicit

' --- Configuration -----------------------------------------------------------
' Root folder where all exports land. A dated subfolder is created each run.
Private Const EXPORT_ROOT     As String = "C:\MailExport\"

' Registry key used to store the last successful run timestamp.
Private Const REG_KEY         As String = "HKCU\Software\MailExporter\LastRun"
' -----------------------------------------------------------------------------


' =============================================================================
' Main entry point. Run this macro from Outlook.
' =============================================================================
Public Sub ExportInboxSinceLastRun()

    Dim dtLastRun       As Date
    Dim dtNow           As Date
    Dim strExportFolder As String
    Dim oInbox          As Outlook.Folder
    Dim oItems          As Outlook.Items
    Dim oFiltered       As Outlook.Items
    Dim oMail           As Outlook.MailItem
    Dim oItem           As Object
    Dim nExported       As Long
    Dim nSkipped        As Long

    dtNow = Now()

    ' --- Read last run date from registry ------------------------------------
    dtLastRun = GetLastRunDate()
    If dtLastRun = 0 Then
        ' First ever run: export last 24 hours as a safe default
        dtLastRun = dtNow - 1
        MsgBox "No previous run found. Exporting mails from the last 24 hours." & vbCrLf & _
               "From: " & Format(dtLastRun, "yyyy-mm-dd hh:nn:ss"), vbInformation, "Mail Exporter"
    End If

    ' --- Build export folder (named after today's date) ----------------------
    strExportFolder = EXPORT_ROOT & Format(dtNow, "yyyy-mm-dd") & "\"
    If Not FolderExists(strExportFolder) Then
        MkDir strExportFolder
    End If

    ' --- Get Inbox and filter by received date -------------------------------
    Set oInbox = Application.Session.GetDefaultFolder(olFolderInbox)
    Set oItems = oInbox.Items
    oItems.Sort "[ReceivedTime]", False   ' ascending

    ' Outlook filter syntax requires date in this locale-independent format
    Dim strFilter As String
    strFilter = "[ReceivedTime] > '" & Format(dtLastRun, "ddddd h:nn AMPM") & "'"
    Set oFiltered = oItems.Restrict(strFilter)

    ' --- Export each mail item -----------------------------------------------
    nExported = 0
    nSkipped = 0

    Dim oObj As Object
    For Each oObj In oFiltered
        ' Only process proper mail items (skip meeting requests, etc.)
        If oObj.Class = olMail Then
            Set oMail = oObj
            ExportSingleMail oMail, strExportFolder
            nExported = nExported + 1
        Else
            nSkipped = nSkipped + 1
        End If
    Next oObj

    ' --- Persist new last-run timestamp --------------------------------------
    SaveLastRunDate dtNow

    ' --- Done ----------------------------------------------------------------
    MsgBox "Export complete." & vbCrLf & _
           "Folder : " & strExportFolder & vbCrLf & _
           "Exported: " & nExported & " mail(s)" & vbCrLf & _
           "Skipped : " & nSkipped & " non-mail item(s)", _
           vbInformation, "Mail Exporter"

    ' Cleanup
    Set oFiltered = Nothing
    Set oItems = Nothing
    Set oInbox = Nothing

End Sub


' =============================================================================
' Exports one MailItem to a .txt file, and saves its attachments.
' File naming: YYYY-MM-DD_HHhMM_SS_<subject-slug>.txt
' =============================================================================
Private Sub ExportSingleMail(oMail As Outlook.MailItem, strFolder As String)

    Dim strFileName     As String
    Dim strFilePath     As String
    Dim strSlug         As String
    Dim nFileNum        As Integer
    Dim oAtt            As Outlook.Attachment
    Dim strAttPath      As String
    Dim strAttWarning   As String

    ' --- Build a safe filename from date + subject ---------------------------
    strSlug = SanitizeFilename(oMail.Subject)
    If Len(strSlug) = 0 Then strSlug = "no-subject"
    If Len(strSlug) > 60 Then strSlug = Left(strSlug, 60)  ' cap length

    strFileName = Format(oMail.ReceivedTime, "yyyy-mm-dd_HHhNN_SS") & "_" & strSlug & ".txt"
    strFilePath = strFolder & strFileName

    ' If a file with that name already exists (duplicate subject in same second), append a counter
    Dim n As Integer
    n = 1
    Do While FileExists(strFilePath)
        strFilePath = strFolder & Format(oMail.ReceivedTime, "yyyy-mm-dd_HHhNN_SS") & "_" & strSlug & "_" & n & ".txt"
        n = n + 1
    Loop

    ' --- Save attachments first, collect names -------------------------------
    Dim strAttachmentList As String
    strAttachmentList = ""
    strAttWarning = ""

    If oMail.Attachments.Count > 0 Then
        For Each oAtt In oMail.Attachments
            ' Only save file attachments (Type 1 = olByValue), skip embedded images (Type 5)
            If oAtt.Type = olByValue Then
                ' Prefix attachment filename with same timestamp to keep things grouped
                Dim strAttName As String
                strAttName = Format(oMail.ReceivedTime, "yyyy-mm-dd_HHhNN_SS") & "_" & SanitizeFilename(oAtt.FileName)
                strAttPath = strFolder & strAttName

                On Error Resume Next
                oAtt.SaveAsFile strAttPath
                If Err.Number <> 0 Then
                    strAttWarning = strAttWarning & "WARNING: Could not save attachment [" & oAtt.FileName & "]: " & Err.Description & vbCrLf
                    strAttachmentList = strAttachmentList & "  ! FAILED: " & oAtt.FileName & vbCrLf
                    Err.Clear
                Else
                    strAttachmentList = strAttachmentList & "  " & strAttName & vbCrLf
                End If
                On Error GoTo 0
            End If
        Next oAtt
    End If

    ' --- Write the .txt file -------------------------------------------------
    nFileNum = FreeFile()
    Open strFilePath For Output As #nFileNum

    ' -- Metadata header --
    Print #nFileNum, "FROM:              " & oMail.SenderEmailAddress
    Print #nFileNum, "FROM-NAME:         " & oMail.SenderName
    Print #nFileNum, "TO:                " & oMail.To
    Print #nFileNum, "CC:                " & oMail.CC
    Print #nFileNum, "DATE:              " & Format(oMail.ReceivedTime, "yyyy-mm-dd hh:nn:ss")
    Print #nFileNum, "SUBJECT:           " & oMail.Subject
    Print #nFileNum, "CONVERSATION-ID:   " & oMail.ConversationID
    Print #nFileNum, "CONVERSATION-TOPIC:" & oMail.ConversationTopic
    Print #nFileNum, "IMPORTANCE:        " & ImportanceLabel(oMail.Importance)
    Print #nFileNum, "HAS-ATTACHMENTS:   " & (oMail.Attachments.Count > 0)

    If Len(strAttachmentList) > 0 Then
        Print #nFileNum, "ATTACHMENTS:"
        Print #nFileNum, strAttachmentList
    End If

    ' -- Attachment warnings (if any) --
    If Len(strAttWarning) > 0 Then
        Print #nFileNum, "--- ATTACHMENT ERRORS ---"
        Print #nFileNum, strAttWarning
    End If

    ' -- Body --
    Print #nFileNum, String(80, "-")
    Print #nFileNum, oMail.Body

    Close #nFileNum

End Sub


' =============================================================================
' Registry helpers — store/retrieve the last run date
' =============================================================================
Private Function GetLastRunDate() As Date
    Dim oShell  As Object
    Dim strVal  As String

    On Error Resume Next
    Set oShell = CreateObject("WScript.Shell")
    strVal = oShell.RegRead(REG_KEY)
    If Err.Number <> 0 Or Len(strVal) = 0 Then
        GetLastRunDate = 0
    Else
        GetLastRunDate = CDate(strVal)
    End If
    On Error GoTo 0
    Set oShell = Nothing
End Function

Private Sub SaveLastRunDate(dt As Date)
    Dim oShell As Object
    Set oShell = CreateObject("WScript.Shell")
    oShell.RegWrite REG_KEY, CStr(dt), "REG_SZ"
    Set oShell = Nothing
End Sub


' =============================================================================
' Utility functions
' =============================================================================

' Replaces characters that are illegal in Windows filenames with underscores.
Private Function SanitizeFilename(s As String) As String
    Dim i       As Integer
    Dim c       As String
    Dim result  As String
    Dim illegal As String
    illegal = "/\:*?""<>|" & Chr(9) & Chr(10) & Chr(13)

    result = s
    For i = 1 To Len(illegal)
        result = Join(Split(result, Mid(illegal, i, 1)), "_")
    Next i
    ' Collapse multiple underscores and trim
    Do While InStr(result, "__") > 0
        result = Join(Split(result, "__"), "_")
    Loop
    SanitizeFilename = Trim(result)
End Function

' Returns True if a folder path exists.
Private Function FolderExists(strPath As String) As Boolean
    On Error Resume Next
    FolderExists = (GetAttr(strPath) And vbDirectory) = vbDirectory
    On Error GoTo 0
End Function

' Returns True if a file path exists.
Private Function FileExists(strPath As String) As Boolean
    On Error Resume Next
    FileExists = (GetAttr(strPath) And vbNormal) >= 0 And Err.Number = 0
    On Error GoTo 0
End Function

' Converts Outlook importance constant to a readable string.
Private Function ImportanceLabel(imp As OlImportance) As String
    Select Case imp
        Case olImportanceLow:    ImportanceLabel = "Low"
        Case olImportanceNormal: ImportanceLabel = "Normal"
        Case olImportanceHigh:   ImportanceLabel = "High"
        Case Else:               ImportanceLabel = "Unknown"
    End Select
End Function
