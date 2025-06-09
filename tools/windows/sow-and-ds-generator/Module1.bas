Attribute VB_Name = "Module1"
'-------------------------
' Scripts developed par O. Rey
' Last modif: April 9 2025
'-------------------------

Public Sub UpdateAllFields()
  ' Update all fields est une fonction récupérée sur le net pour avoir une bonne adaptation de la table des matières
  
  Dim rngStory As Word.Range
  Dim lngJunk As Long
  Dim oShp As Shape
  lngJunk = ActiveDocument.Sections(1).Headers(1).Range.StoryType
  For Each rngStory In ActiveDocument.StoryRanges
    'Iterate through all linked stories
    Do
      On Error Resume Next
      rngStory.Fields.Update
      Select Case rngStory.StoryType
        Case 6, 7, 8, 9, 10, 11
          If rngStory.ShapeRange.count > 0 Then
            For Each oShp In rngStory.ShapeRange
              If oShp.TextFrame.HasText Then
                oShp.TextFrame.TextRange.Fields.Update
              End If
            Next
          End If
        Case Else
          'Do Nothing
        End Select
        On Error GoTo 0
        'Get next linked story (if any)
        Set rngStory = rngStory.NextStoryRange
      Loop Until rngStory Is Nothing
    Next
End Sub

Sub searchAndReplace(objDoc, strWord, replace)

    With objDoc.Content.Find
        .Text = strWord
        .Replacement.Text = replace
        .Execute replace:=wdReplaceAll ', Forward:=True, Wrap:=wdFindContinue
    End With
    
End Sub

Sub log(obj)

Dim s As String
Dim n As Integer

n = FreeFile()
Open "C:\Users\a876246\Documents\oreyboulot-NHI\DMD_IS\RFA\log.txt" For Output As #n

Debug.Print obj ' write to immediate
Print #n, obj ' write to file

Close #n

End Sub

Sub logInTab(mytab, str)

If Not mytab.Cells(6, 4) = "" Then
    mytab.Cells(6, 4) = mytab.Cells(6, 4) & vbNewLine & str
Else
    mytab.Cells(6, 4) = str
End If

End Sub

Sub OpenDocumentAndLoop()
    ' D'abord le num de ligne puis de colonne dans les Sheet.Cells(3, 6)

    Dim Sheet, Master As Worksheet
    
    Set Master = Sheets("MASTER")
    Master.Cells(6, 4) = ""
    
    
    Set Sheet = Sheets(CStr(Master.Cells(1, 2)))
    logInTab Master, "Considering worksheet: " & Sheet.Name

    ' Management of the version
    Dim count As Integer
    count = Sheet.Cells(3, 3)
    If count = Empty Then
        count = 0
    End If
    
    ' Management of SOW
    Dim sow_string As String, sow As Boolean
    sow_string = Sheet.Cells(6, 3)
    If sow_string = "NO" Then
        sow = False
        logInTab Master, "No SOW required"
    Else
        sow = True
    End If
    
    ' Management of DS
    Dim ds_string As String, ds As Boolean
    ds_string = Sheet.Cells(8, 3)
    If ds_string = "NO" Then
        ds = False
        logInTab Master, "No DS required"
    Else
        ds = True
    End If

    ' Get document
    Set objWord = CreateObject("Word.Application")
    
    logInTab Master, "MS Word created"
    
    ' Variale declaration SOW
    Dim templateName As String
    Dim filename As String
    
    ' Variale declaration DS
    Dim templateName2 As String
    Dim filename2 As String
    
    '=================================================SOW
    If sow Then
        templateName = Sheet.Cells(1, 2)
        Set objDoc = objWord.Documents.Open(templateName, ReadOnly:=True)
        count = count + 1
        
        ' SOW
        filename = Sheet.Cells(3, 2) & CStr(count) & "_" & Sheet.Cells(7, 2) & Sheet.Cells(2, 2) & Sheet.Cells(8, 2) & Sheet.Cells(9, 2) & ".docx"
        filenamepdf = Sheet.Cells(3, 2) & CStr(count) & "_" & Sheet.Cells(7, 2) & Sheet.Cells(2, 2) & Sheet.Cells(8, 2) & Sheet.Cells(9, 2) & ".pdf"
        objDoc.SaveAs2 filename
        Sheet.Cells(3, 3) = count
    End If
    
    '=================================================DS
    If ds Then
        templateName2 = Sheet.Cells(4, 2)
        Set objDoc2 = objWord.Documents.Open(templateName2, ReadOnly:=True)
        count = count + 1
        
        ' DS
        filename2 = Sheet.Cells(6, 2) & CStr(count) & "_" & Sheet.Cells(7, 2) & Sheet.Cells(5, 2) & Sheet.Cells(8, 2) & Sheet.Cells(9, 2) & ".docx"
        objDoc2.SaveAs2 filename2
        Sheet.Cells(3, 3) = count
    End If
    
    Dim rowStart As Integer
    rowStart = Master.Cells(2, 2)
    Dim rowEnd As Integer
    rowEnd = Master.Cells(3, 2)
    Dim strWord As String
    Dim Separator As String
    Separator = "$"
    Dim replace As String
    
    For Index = rowStart To rowEnd
        strWord = Separator & Sheet.Cells(Index, 1) & Separator
        replace = Sheet.Cells(Index, 2)
        If sow Then
            searchAndReplace objDoc, strWord, replace
        End If
        If ds Then
            searchAndReplace objDoc2, strWord, replace
        End If
    Next Index
    
    logInTab Master, "Replaced " & CStr(Index) & " parameters"
    
    If sow Then
        objDoc.Save
        logInTab Master, "File " & filename & " saved"
        objDoc.ExportAsFixedFormat OutputFileName:=filenamepdf, ExportFormat:=wdExportFormatPDF
    
        logInTab Master, "Exporting PDF file"
        logInTab Master, "File " & filenamepdf & " saved"
        objDoc.Close wdSaveChanges
        Set objDoc = Nothing
    End If
    
    If ds Then
        objDoc2.Save
        logInTab Master, "File " & filename2 & " saved"
        objDoc2.Close wdSaveChanges
        Set objDoc2 = Nothing
    End If
    
    objWord.Quit True
    Set objWord = Nothing
    
    logInTab Master, "Word exited"
    logInTab Master, "End of Treatment"

End Sub
