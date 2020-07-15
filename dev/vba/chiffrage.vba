Public Function CustomAmount(a) As Currency

CustomAmount = a * (1 + Range("Abaques!$E$16").value) / 1.2

End Function


Public Function MyPrice(value) As Range

Select Case value
    ' Interfaces
    Case Range("Abaques!$B$22")
        Set MyPrice = Range("Abaques!$F$22")
    Case Range("Abaques!$B$23")
        Set MyPrice = Range("Abaques!$F$23")
    Case Range("Abaques!$B$24")
        Set MyPrice = Range("Abaques!$F$24")
    Case Range("Abaques!$B$25")
        Set MyPrice = Range("Abaques!$F$25")
    Case Range("Abaques!$B$26")
        Set MyPrice = Range("Abaques!$F$26")
        
    ' Implémentation fonctions progiciels
    Case Range("Abaques!$B$31")
        Set MyPrice = Range("Abaques!$F$31")
    Case Range("Abaques!$B$32")
        Set MyPrice = Range("Abaques!$F$32")
    Case Range("Abaques!$B$33")
        Set MyPrice = Range("Abaques!$F$33")
    Case Range("Abaques!$B$34")
        Set MyPrice = Range("Abaques!$F$34")
        
    ' Implémentation fonctions développement
    Case Range("Abaques!$B$40")
        Set MyPrice = Range("Abaques!$F$40")
    Case Range("Abaques!$B$41")
        Set MyPrice = Range("Abaques!$F$41")
    Case Range("Abaques!$B$42")
        Set MyPrice = Range("Abaques!$F$42")
    Case Range("Abaques!$B$43")
        Set MyPrice = Range("Abaques!$F$43")

    ' Implémentation analytiques
    Case Range("Abaques!$B$49")
        Set MyPrice = Range("Abaques!$F$49")
    Case Range("Abaques!$B$50")
        Set MyPrice = Range("Abaques!$F$50")
    Case Range("Abaques!$B$51")
        Set MyPrice = Range("Abaques!$F$51")
    Case Range("Abaques!$B$52")
        Set MyPrice = Range("Abaques!$F$52")
    Case Range("Abaques!$B$53")
        Set MyPrice = Range("Abaques!$F$53")
    Case Range("Abaques!$B$54")
        Set MyPrice = Range("Abaques!$F$54")
    Case Range("Abaques!$B$55")
        Set MyPrice = Range("Abaques!$F$55")
    Case Range("Abaques!$B$56")
        Set MyPrice = Range("Abaques!$F$56")
    Case Range("Abaques!$B$57")
        Set MyPrice = Range("Abaques!$F$57")
    
    Case Else
        Set MyPrice = Range("Abaques!$E$16")
End Select

End Function


Public Function TotalNrc() As Currency

Dim total As Currency
total = 0
Dim value As Currency
Dim chaine As String


For Each WS In ThisWorkbook.Worksheets
    'MsgBox (WS.Name)
    If WS.Name <> "Intro" And WS.Name <> "Abaques" And WS.Name <> "Total" And Not (WS.Name Like "OLD*") Then
        Rem chaine = """'" + WS.Name + "'!G1" + """"
        chaine = "'" + WS.Name + "'!G1"
        'MsgBox (chaine)
        value = Range(chaine).value
        'MsgBox (value)
        total = total + value
    Else
        'MsgBox ("Not taken")
    End If
Next

'MsgBox (total)

TotalNrc = total

End Function


Rem ==========================
Rem Public Function DisplayNrc() As Range

Rem MsgBox ("toto")
Rem ActiveCell.value = TotalNrc()
'MsgBox ("titi")
'ActiveCell.NumberFormat = "#,##0€"

'End Function
Rem ==========================

Public Function CumulateAmountsInCell(cellref) As Currency

Dim total As Currency
total = 0
Dim value As Currency
Dim chaine As String


For Each WS In ThisWorkbook.Worksheets
    'MsgBox (WS.Name)
    If WS.Name <> "Intro" And WS.Name <> "Abaques" And WS.Name <> "Total" And Not (WS.Name Like "OLD*") Then
        chaine = "'" + WS.Name + "'!" + cellref
        'MsgBox (chaine)
        value = Range(chaine).value
        total = total + value
    Else
        'MsgBox ("Not considered")
    End If
Next

CumulateAmountsInCell = total

End Function

Public Function CumulateAmountsPerOrganization(orgacell) As Currency

Dim orgavalue As String
orgavalue = orgacell.value
Rem MsgBox (orgavalue)

Dim chaine1, chaine2 As String
Dim total As Currency
total = 0

For Each WS In ThisWorkbook.Worksheets
    'MsgBox (WS.Name)
    If WS.Name <> "Intro" And WS.Name <> "Abaques" And WS.Name <> "Total" And Not (WS.Name Like "OLD*") Then
        chaine1 = "'" + WS.Name + "'!G1"
        chaine2 = "'" + WS.Name + "'!E1"
        If Range(chaine2).value = orgavalue Then
            Rem MsgBox ("OK")
            Rem MsgBox (Range(chaine1).value)
            total = total + Range(chaine1).value
        End If
    Else
        'MsgBox ("Not considered")
    End If
Next

CumulateAmountsPerOrganization = total

End Function

Sub Workbook_RefreshAll()

Rem Worksheets("Total").Calculate

Dim cell, newcell As Range

For Each cell In Range("C2:C200")
    cell.Formula = cell.Formula
    cell.Calculate
Next
    
End Sub

Function test01(c) As String

MsgBox ("Row: ")
MsgBox (c.Row())
MsgBox ("Column: ")
MsgBox (c.Column())

Cells(20, 6) = "12"


test01 = "OK"


End Function

Sub VisionGlobale()

' depart est supposé être un range avec une cell
' Nous allons écrire la synthèse à droite et en bas

Dim x, y As Integer
x = 8
y = 3

Dim orga As String
Dim rc, nrc As Currency
Dim r As Range


For Each WS In ThisWorkbook.Worksheets
    If (WS.Name Like "(*") Then
        'MsgBox (WS.Name)
        orga = Range("'" + WS.Name + "'!E1").value
        nrc = Range("'" + WS.Name + "'!G1").value
        rc = Range("'" + WS.Name + "'!G2").value
        'Worksheets("Total").
        Cells(y, x) = WS.Name
        'Worksheets("Total").
        Cells(y, x + 1) = orga
        'Worksheets("Total").
        Cells(y, x + 2) = nrc
        'Worksheets("Total").
        Cells(y, x + 3) = rc
        
        y = y + 1
    End If
Next

End Sub

Sub RefreshAll()

Dim cell As Range

For Each WS In ThisWorkbook.Worksheets
    If (WS.Name Like "(*") Then
        For Each cell In Range("'" + WS.Name + "'!G3:G200")
            cell.Formula = cell.Formula
            cell.Calculate
        Next
    End If
Next
End Sub

