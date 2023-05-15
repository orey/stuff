Rem ---------------------------------------------------
Public Function CustomAmount(a) As Currency

CustomAmount = a * (1 + Range("Abaques!$E$16").value) / 1.2

End Function


Rem ---------------------------------------------------
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


Rem ---------------------------------------------------
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

Rem ---------------------------------------------------
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

Rem ---------------------------------------------------
Sub Workbook_RefreshAll()

Rem Worksheets("Total").Calculate

Dim cell, newcell As Range

For Each cell In Range("C2:C200")
    cell.Formula = cell.Formula
    cell.Calculate
Next
    
End Sub

Rem ---------------------------------------------------
Function test01(c) As String

MsgBox ("Row: ")
MsgBox (c.Row())
MsgBox ("Column: ")
MsgBox (c.Column())

Cells(20, 6) = "12"


test01 = "OK"


End Function

Rem ---------------------------------------------------
Sub VisionGlobale()

' depart est supposé être un range avec une cell
' Nous allons écrire la synthèse à droite et en bas

Dim x, y As Integer
x = 1
y = 2

Dim orga As String
Dim rc, nrc As Currency
Dim r As Range


For Each WS In ThisWorkbook.Worksheets
    If (WS.Name Like "(*") Then
        'MsgBox (WS.Name)
        orga = Range("'" + WS.Name + "'!E1").value
        typepack = Range("'" + WS.Name + "'!E2").value
        nrc = Range("'" + WS.Name + "'!G1").value
        rc = Range("'" + WS.Name + "'!G2").value
        
        nrc18 = Range("'" + WS.Name + "'!J1").value
        rc18 = Range("'" + WS.Name + "'!J2").value
        
        nrcS1 = Range("'" + WS.Name + "'!M1").value
        rcS1 = Range("'" + WS.Name + "'!M2").value
        
        nrcS2 = Range("'" + WS.Name + "'!P1").value
        rcS2 = Range("'" + WS.Name + "'!P2").value
        
        nrcS3 = Range("'" + WS.Name + "'!S1").value
        rcS3 = Range("'" + WS.Name + "'!S2").value
        
        'Worksheets("Total").
        ' Globales
        Cells(y, x) = WS.Name
        
        Cells(y, x + 1) = typepack
        Cells(y, x + 2) = orga
        
        ' Scénario à 40 M€
        Cells(y, x + 3) = nrc
        Cells(y, x + 4) = rc
        
        ' Scénario à 18 M€
        Cells(y, x + 5) = nrc18
        Cells(y, x + 6) = rc18
        
        ' Scénario 1
        Cells(y, x + 7) = nrcS1
        Cells(y, x + 8) = rcS1
        
        ' Scénario 2
        Cells(y, x + 9) = nrcS2
        Cells(y, x + 10) = rcS2
        
        ' Scénario 3
        Cells(y, x + 11) = nrcS3
        Cells(y, x + 12) = rcS3
        
        y = y + 1
    End If
Next

End Sub

Rem ---------------------------------------------------
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


Rem Offer
Rem ---------------------------------------------------

Function PrintScenario(y As Integer, mp As String, hs As String) As Integer

Dim s1manpower, s1hardsoft, im, mt, extim, extmt, yim, yextim, yextmt, ymt As Long
Dim StartDate, EndDate, duration, mystart, myend, externalhours, internalhours As Integer

Dim wp_offre As String


For Each WS In ThisWorkbook.Worksheets
    If (WS.Name Like "(*") Then
        'MsgBox (WS.Name)
        ' Je dois récupérer 2 nombres du scénario
        s1manpower = Range("'" + WS.Name + "'!" + mp).value
        'MsgBox s1manpower
        s1hardsoft = Range("'" + WS.Name + "'!" + hs).value
        
        StartDate = Range("'" + WS.Name + "'!B1").value
        EndDate = Range("'" + WS.Name + "'!B2").value
        
        wp_offre = Range("'" + WS.Name + "'!A1").value
        
        externalhours = Round(Cells(1, 2) * s1manpower / Cells(1, 6))
        internalhours = Round(Cells(2, 2) * s1manpower / Cells(2, 6))
        im = Round(internalhours / 2)
        mt = im
        extim = Round(externalhours / 2)
        extmt = extim
        
        ' Ligne 1 : im costs + hard/soft
        Cells(y, 27) = s1hardsoft ' only once
        
        Cells(y, 2) = wp_offre
        Cells(y + 1, 2) = wp_offre
        Cells(y + 2, 2) = wp_offre
        Cells(y + 3, 2) = wp_offre
        
        Cells(y, 3) = "Systèmes d'informations"
        Cells(y + 1, 3) = "Systèmes d'informations"
        Cells(y + 2, 3) = "Systèmes d'informations"
        Cells(y + 3, 3) = "Systèmes d'informations"
        
        ' S1
        Cells(y, 4) = WS.Name
        Cells(y + 1, 4) = WS.Name
        Cells(y + 2, 4) = WS.Name
        Cells(y + 3, 4) = WS.Name
        
        Cells(y, 5) = "EII"
        Cells(y + 1, 5) = "ES"
        Cells(y + 2, 5) = "EII"
        Cells(y + 3, 5) = "ES"
        
        Cells(y, 13) = "'" + CStr(StartDate)
        Cells(y + 1, 13) = "'" + CStr(StartDate)
        Cells(y + 2, 13) = "'" + CStr(StartDate)
        Cells(y + 3, 13) = "'" + CStr(StartDate)
        
        Cells(y, 14) = "'" + CStr(EndDate)
        Cells(y + 1, 14) = "'" + CStr(EndDate)
        Cells(y + 2, 14) = "'" + CStr(EndDate)
        Cells(y + 3, 14) = "'" + CStr(EndDate)
        
        duration = EndDate - StartDate + 1
        
        Cells(y, 15) = 12 * duration
        Cells(y + 1, 15) = 12 * duration
        Cells(y + 2, 15) = 12 * duration
        Cells(y + 3, 15) = 12 * duration
        
        Cells(y, 16) = "Internal"
       Cells(y + 1, 16) = "Internal"
        Cells(y + 2, 16) = "External"
        Cells(y + 3, 16) = "External"
        
        yim = Round(im / duration)
        ymt = Round(mt / duration)
        yextim = Round(extim / duration)
        yextmt = Round(extmt / duration)
        
        'Init à blanc
        For i = 17 To 24
            Cells(y, i) = ""
            Cells(y + 1, i) = ""
            Cells(y + 2, i) = ""
            Cells(y + 3, i) = ""
        Next
        
        ' cell origine est 2022 = x=17
        mystart = StartDate - 2022 + 17
        myend = mystart + duration - 1
        For i = mystart To myend
            Cells(y, i) = yim
        Next
        For i = mystart To myend
            Cells(y + 1, i) = ymt
        Next
        For i = mystart To myend
            Cells(y + 2, i) = yextim
        Next
        For i = mystart To myend
            Cells(y + 3, i) = yextim
        Next
        
        y = y + 4

    End If
Next

PrintScenario = y

End Function

Rem ---------------------------------------------------
Sub Offre()

Dim y As Integer

Cells(8, 1) = "Scénario 1"
y = 9

y = PrintScenario(y, "M3", "M4")

y = y + 4
Cells(y - 1, 1) = "Scénario 2"

y = PrintScenario(y, "P3", "P4")

y = y + 4
Cells(y - 1, 1) = "Scénario 3"

y = PrintScenario(y, "S3", "S4")



'For Each WS In ThisWorkbook.Worksheets
'    If (WS.Name Like "(*") Then
'        'MsgBox (WS.Name)
'        ' Je dois récupérer 6 nombres
'        s1manpower = Range("'" + WS.Name + "'!M3").value
'        s1hardsoft = Range("'" + WS.Name + "'!M4").value
'
'
'
'        s2manpower = Range("'" + WS.Name + "'!P3").value
'        s2hardsoft = Range("'" + WS.Name + "'!P4").value
'
'        s3manpower = Range("'" + WS.Name + "'!S3").value
'        s3hardsoft = Range("'" + WS.Name + "'!S4").value
'
'
'
'
'    End If
'Next

End Sub





Rem Scénatio offer

Rem ---------------------------------------------------
Function PrintScenarioMCO(y As Integer, mp As String, hs As String) As Integer

' Version MCO de la macro

Dim s1manpower, s1hardsoft, im, mt, extim, extmt, yim, yextim, yextmt, ymt As Long
Dim StartDate, EndDate, duration, mystart, myend, externalhours, internalhours As Integer

Dim wp_offre As String

Dim montantext As Currency
Dim hsperyear As Currency




For Each WS In ThisWorkbook.Worksheets
    If (WS.Name Like "(*") Then
        'MsgBox (WS.Name)
        ' Je dois récupérer 2 nombres du scénario : le chiffre de coûts bruts
        ' et le chiffre de hardware et de software
        s1manpower = Range("'" + WS.Name + "'!" + mp).value
        'MsgBox s1manpower
        s1hardsoft = Range("'" + WS.Name + "'!" + hs).value
        
        ' 10 ans de MCO
        StartDate = 2027
        EndDate = 2036
        
        ' Clef de répartition des WP de l'offre
        wp_offre = Range("'" + WS.Name + "'!A1").value
        
        ' Découpage des 4 postes d'heures
        externalhours = Round(Cells(1, 2) * s1manpower / Cells(1, 6))
        internalhours = Round(Cells(2, 2) * s1manpower / Cells(2, 6))
        im = Round(internalhours / 2)
        mt = im
        extim = Round(externalhours / 2)
        extmt = extim
        
        'Init à blanc
'        For i = 1 To 31
'            Cells(y, i) = ""
'            Cells(y + 1, i) = ""
'            Cells(y + 2, i) = ""
'            Cells(y + 3, i) = ""
'        Next
        
        Range(Cells(y, 1), Cells(y, 38)) = ""
        Range(Cells(y + 1, 1), Cells(y + 1, 38)) = ""
        Range(Cells(y + 2, 1), Cells(y + 2, 38)) = ""
        Range(Cells(y + 3, 1), Cells(y + 3, 38)) = ""
        Range(Cells(y + 4, 1), Cells(y + 4, 38)) = ""
        
        Cells(y, 2) = wp_offre
        Cells(y + 1, 2) = wp_offre
        Cells(y + 2, 2) = wp_offre
        Cells(y + 3, 2) = wp_offre
        Cells(y + 4, 2) = wp_offre
        
        Cells(y, 3) = "Systèmes d'informations"
        Cells(y + 1, 3) = "Systèmes d'informations"
        Cells(y + 2, 3) = "Systèmes d'informations"
        Cells(y + 3, 3) = "Systèmes d'informations"
        Cells(y + 4, 3) = "Systèmes d'informations"
        
        ' S1
        Cells(y, 4) = WS.Name
        Cells(y + 1, 4) = WS.Name
        Cells(y + 2, 4) = WS.Name
        Cells(y + 3, 4) = WS.Name
        Cells(y + 4, 4) = WS.Name
        
        Cells(y, 5) = "EII"
        'Cells(y + 1, 5) = "ES"
        Cells(y + 1, 5) = Range("'" + WS.Name + "'!A2").value
        Cells(y + 2, 5) = "EII"
        'Cells(y + 3, 5) = "ES"
        Cells(y + 3, 5) = Range("'" + WS.Name + "'!A2").value
        Cells(y + 4, 5) = "EII"
        
        Cells(y, 13) = "'" + CStr(StartDate)
        Cells(y + 1, 13) = "'" + CStr(StartDate)
        Cells(y + 2, 13) = "'" + CStr(StartDate)
        Cells(y + 3, 13) = "'" + CStr(StartDate)
        Cells(y + 4, 13) = "'" + CStr(StartDate)
        
        Cells(y, 14) = "'" + CStr(EndDate)
        Cells(y + 1, 14) = "'" + CStr(EndDate)
        Cells(y + 2, 14) = "'" + CStr(EndDate)
        Cells(y + 3, 14) = "'" + CStr(EndDate)
        Cells(y + 4, 14) = "'" + CStr(EndDate)
        
        duration = EndDate - StartDate + 1
        
        Cells(y, 15) = 12 * duration
        Cells(y + 1, 15) = 12 * duration
        Cells(y + 2, 15) = 12 * duration
        Cells(y + 3, 15) = 12 * duration
        Cells(y + 4, 15) = 12 * duration
        
        Cells(y, 16) = "Internal"
        Cells(y + 1, 16) = "Internal"
        Cells(y + 2, 16) = "External"
        Cells(y + 3, 16) = "External"
        Cells(y + 4, 16) = "HW/SW"
        
        ' On prend le montant total et on le multiplie par le taux
        'yim = Round(im / duration)
        'ymt = Round(mt / duration)
        'yextim = Round(extim / duration)
        'yextmt = Round(extmt / duration)
        
        yim = Round(im * Cells(1, 9))
        ymt = Round(mt * Cells(1, 9))
        yextim = Round(extim * Cells(1, 9))
        yextmt = Round(extmt * Cells(1, 9))
                
        ' cell origine est 2027 = x=17 $$$$$$$$$$$$
        mystart = StartDate - 2027 + 17
        myend = mystart + duration - 1
        
        ' Coûts IM lissés avec 1/2 année débit et 1/2 année fin
        'Cells(y, mystart) = Round(0.5 * yim)
        For i = mystart To myend
            Cells(y, i) = yim
        Next
        'Cells(y, myend) = Round(0.5 * yim)
        
        ' Coûts MT lissés avec 1/2 année débit et 1/2 année fin
        'Cells(y + 1, mystart) = Round(0.5 * ymt)
       For i = mystart To myend
            Cells(y + 1, i) = ymt
        Next
        'Cells(y + 1, myend) = Round(0.5 * ymt)
        
        ' Count of prestations in euro
        ' cell origine est 2027 = x=28 $$$$$$$$$$$$
        mystart = StartDate - 2027 + 28
        myend = mystart + duration - 1
        
        'Montant de prestation par an MCO
        montantext = Round(Cells(1, 2) * s1manpower * Cells(1, 9) / 2)
        
        'Cells(y + 2, mystart) = Round(0.5 * montantext)
        For i = mystart To myend
            Cells(y + 2, i) = montantext
        Next
        'Cells(y + 2, myend) = Round(0.5 * montantext)
        
        'Cells(y + 3, mystart) = Round(0.5 * montantext)
        For i = mystart To myend
            Cells(y + 3, i) = montantext
        Next
        'Cells(y + 3, myend) = Round(0.5 * montantext)
        
        
        ' Ligne 1 : im costs + hard/soft
        ' nous prenons le coût par an * durée du MCO
        'Cells(y, 30) = s1hardsoft * duration * Cells(2, 9)
        hsperyear = s1hardsoft * Cells(2, 9)
        
        ' Coûts HW/SW lissés avec 1/2 année débit et 1/2 année fin
        'Cells(y + 4, mystart) = Round(0.5 * hsperyear)
        For i = mystart To myend
            Cells(y + 4, i) = hsperyear
        Next
        'Cells(y + 4, myend) = Round(0.5 * hsperyear)
        
        
        y = y + 5

    End If
Next

PrintScenarioMCO = y

End Function

Rem ---------------------------------------------------
Sub OffreMCO()

Dim y As Integer

Cells(8, 1) = "Scénario 1"
y = 9

y = PrintScenarioMCO(y, "M3", "M4")

y = y + 4
Cells(y - 1, 1) = "Scénario 2"

y = PrintScenarioMCO(y, "P3", "P4")

y = y + 4
Cells(y - 1, 1) = "Scénario 3"

y = PrintScenarioMCO(y, "S3", "S4")


End Sub




Best regards, cordialement,

Olivier Rey
Head of IT at NH Industries
EXNH
olivier.o.rey@airbus.com
+33 6 48 27 53 10
Airbus Helicopters

