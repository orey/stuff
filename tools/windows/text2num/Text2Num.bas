Attribute VB_Name = "Module1"
Function Text2Num(cell)
    Rem MsgBox cell.Value
    Dim value As Variant
    value = cell.value
    value = Replace(value, " ", "")
    value = Replace(value, ",", ".")
    Text2Num = CDec(value)
End Function

