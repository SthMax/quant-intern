Option Explicit

' PowerPoint VBA. Paste this entire file into a standard module.
' Each run replaces one explicit RGB color, chosen by the user.
' Body modes use the configured 25.40 x 14.28 cm slide geometry.

Private Const POINTS_PER_CM As Double = 28.3464566929134
Private Const BODY_LEFT_CM As Double = 1.27
Private Const BODY_RIGHT_CM As Double = 24.13
Private Const BODY_TOP_CM As Double = 3.92
Private Const BODY_BOTTOM_CM As Double = 13.01
Private Const EDGE_TOLERANCE_PT As Double = 0.5

Public Sub Recolor_SelectedObjects()
    Recolor 1
End Sub

Public Sub Recolor_CurrentSlideBody()
    Recolor 2
End Sub

Public Sub Recolor_AllSlidesBody()
    Recolor 3
End Sub

Private Sub Recolor(ByVal scope As Long)
    Dim pres As Presentation, sld As Slide, sh As Shape
    Dim picked As ShapeRange, targets As Collection
    Dim oldColor As Long, newColor As Long, mode As Long
    Dim answer As String, scopeText As String, kindText As String
    Dim counts(1 To 3) As Long, i As Long, started As Boolean

    On Error GoTo Failed
    If Presentations.Count = 0 Then
        MsgBox "Open the working presentation first.", vbInformation
        Exit Sub
    End If
    Set pres = ActivePresentation
    Set targets = New Collection

    If scope = 1 Then
        If ActiveWindow.Selection.Type <> ppSelectionShapes Then
            MsgBox "Select shape borders first, then run this macro.", vbInformation
            Exit Sub
        End If
        If ActiveWindow.Selection.HasChildShapeRange Then
            Set picked = ActiveWindow.Selection.ChildShapeRange
        Else
            Set picked = ActiveWindow.Selection.ShapeRange
        End If
        For i = 1 To picked.Count
            targets.Add picked(i)
        Next i
        scopeText = "Selected objects (including group children)"
    ElseIf scope = 2 Then
        Set sld = ActiveWindow.View.Slide
        CollectBody sld, targets
        scopeText = "Slide " & sld.SlideIndex & ": body objects only"
    Else
        For Each sld In pres.Slides
            CollectBody sld, targets
        Next sld
        scopeText = "Slides 1-" & pres.Slides.Count & ": body objects only"
    End If

    If targets.Count = 0 Then
        MsgBox "No objects in this scope. Use Normal view for current-slide mode.", vbInformation
        Exit Sub
    End If
    If Not AskColor("OLD color", "#005A9C", oldColor) Then Exit Sub
    If Not AskColor("NEW color", "#005AA4", newColor) Then Exit Sub
    If oldColor = newColor Then
        MsgBox "The old and new colors are the same.", vbInformation
        Exit Sub
    End If

    answer = Trim$(InputBox("Properties to change:" & vbCrLf & _
        "0 = Fill + lines + text" & vbCrLf & _
        "1 = Fill only" & vbCrLf & _
        "2 = Lines / table borders only" & vbCrLf & _
        "3 = Text only", "PowerPoint color replacement", "0"))
    If answer = "" Then Exit Sub
    Select Case answer
        Case "0": mode = 0: kindText = "Fill + lines + text"
        Case "1": mode = 1: kindText = "Fill only"
        Case "2": mode = 2: kindText = "Lines / table borders only"
        Case "3": mode = 3: kindText = "Text only"
        Case Else
            MsgBox "Enter 0, 1, 2 or 3.", vbInformation
            Exit Sub
    End Select

    If MsgBox("Presentation: " & pres.Name & vbCrLf & _
        scopeText & vbCrLf & kindText & vbCrLf & _
        HexColor(oldColor) & " -> " & HexColor(newColor) & vbCrLf & vbCrLf & _
        "Replace exact RGB matches now?", _
        vbYesNo + vbQuestion + vbDefaultButton2, "PowerPoint color replacement") <> vbYes Then Exit Sub

    started = True
    For Each sh In targets
        VisitShape sh, oldColor, newColor, mode, counts
    Next sh
    MsgBox "Replacement complete." & vbCrLf & _
        "Fills: " & counts(1) & vbCrLf & _
        "Lines / borders: " & counts(2) & vbCrLf & _
        "Text characters: " & counts(3) & vbCrLf & vbCrLf & _
        "The presentation has not been saved automatically.", vbInformation
    Exit Sub

Failed:
    answer = "Stopped: " & Err.Description
    If started Then answer = answer & vbCrLf & "Earlier changes may already be present."
    MsgBox answer & vbCrLf & "No automatic save was performed.", vbExclamation
End Sub

Private Sub CollectBody(ByVal sld As Slide, ByVal targets As Collection)
    Dim sh As Shape
    For Each sh In sld.Shapes
        If InBody(sh) Then targets.Add sh
    Next sh
End Sub

Private Function InBody(ByVal sh As Shape) As Boolean
    ' Check the whole top-level group before visiting its children.
    If sh.Left < BODY_LEFT_CM * POINTS_PER_CM - EDGE_TOLERANCE_PT Then Exit Function
    If sh.Top < BODY_TOP_CM * POINTS_PER_CM - EDGE_TOLERANCE_PT Then Exit Function
    If sh.Left + sh.Width > BODY_RIGHT_CM * POINTS_PER_CM + EDGE_TOLERANCE_PT Then Exit Function
    If sh.Top + sh.Height > BODY_BOTTOM_CM * POINTS_PER_CM + EDGE_TOLERANCE_PT Then Exit Function
    InBody = True
End Function

Private Sub VisitShape(ByVal sh As Shape, ByVal oldColor As Long, _
        ByVal newColor As Long, ByVal mode As Long, ByRef counts() As Long)
    Dim i As Long, r As Long, c As Long, edge As Long, cell As Cell

    Select Case LCase$(sh.Name)
        Case "source.note", "!!source", "map.legend": Exit Sub
    End Select
    If sh.Type = msoPlaceholder Then
        Select Case sh.PlaceholderFormat.Type
            Case ppPlaceholderFooter, ppPlaceholderDate, ppPlaceholderSlideNumber: Exit Sub
        End Select
    End If
    If sh.Type = msoGroup Then
        For i = 1 To sh.GroupItems.Count
            VisitShape sh.GroupItems(i), oldColor, newColor, mode, counts
        Next i
        Exit Sub
    End If
    If sh.HasTable = msoTrue Then
        For r = 1 To sh.Table.Rows.Count
            For c = 1 To sh.Table.Columns.Count
                Set cell = sh.Table.Cell(r, c)
                PaintFillAndText cell.Shape, oldColor, newColor, mode, counts
                If mode = 0 Or mode = 2 Then
                    For edge = 1 To 6
                        If cell.Borders.Item(edge).Visible = msoTrue Then
                            PaintColor cell.Borders.Item(edge).ForeColor, oldColor, newColor, counts(2)
                        End If
                    Next edge
                End If
            Next c
        Next r
        Exit Sub
    End If
    Select Case sh.Type
        Case msoAutoShape, msoFreeform, msoLine, msoTextBox, msoPlaceholder, msoTextEffect
            PaintFillAndText sh, oldColor, newColor, mode, counts
            If mode = 0 Or mode = 2 Then
                If sh.Line.Visible = msoTrue Then
                    PaintColor sh.Line.ForeColor, oldColor, newColor, counts(2)
                End If
            End If
        ' Pictures, charts, SmartArt, media and OLE objects are left intact.
    End Select
End Sub

Private Sub PaintFillAndText(ByVal sh As Shape, ByVal oldColor As Long, _
        ByVal newColor As Long, ByVal mode As Long, ByRef counts() As Long)
    Dim tr As TextRange, i As Long
    If mode = 0 Or mode = 1 Then
        If sh.Fill.Visible = msoTrue Then
            If sh.Fill.Type = msoFillSolid Then
                PaintColor sh.Fill.ForeColor, oldColor, newColor, counts(1)
            End If
        End If
    End If
    If mode = 0 Or mode = 3 Then
        If sh.HasTextFrame = msoTrue Then
            If sh.TextFrame.HasText = msoTrue Then
                Set tr = sh.TextFrame.TextRange
                ' Character-level color changes preserve mixed text formatting.
                For i = 1 To tr.Length
                    PaintColor tr.Characters(i, 1).Font.Color, oldColor, newColor, counts(3)
                Next i
            End If
        End If
    End If
End Sub

Private Sub PaintColor(ByVal col As Object, ByVal oldColor As Long, _
        ByVal newColor As Long, ByRef count As Long)
    ' Leave existing theme bindings in place.
    If col.Type <> msoColorTypeRGB Then Exit Sub
    If col.RGB <> oldColor Then Exit Sub
    col.RGB = newColor
    count = count + 1
End Sub

Private Function AskColor(ByVal caption As String, ByVal initial As String, _
        ByRef value As Long) As Boolean
    Dim s As String
    Do
        s = InputBox("Enter " & caption & " as #RRGGBB or R,G,B.", "PowerPoint color replacement", initial)
        If Trim$(s) = "" Then Exit Function
        If ParseColor(s, value) Then
            AskColor = True
            Exit Function
        End If
        MsgBox "Use six HEX digits, or three integers from 0 to 255.", vbInformation
        initial = s
    Loop
End Function

Private Function ParseColor(ByVal inputText As String, ByRef value As Long) As Boolean
    Dim s As String, parts As Variant, channel(0 To 2) As Long
    Dim i As Long, number As Double
    On Error GoTo Invalid
    s = UCase$(Trim$(inputText))
    If Left$(s, 1) = "#" Then s = Mid$(s, 2)
    If Len(s) = 6 And InStr(s, ",") = 0 Then
        If s Like "*[!0-9A-F]*" Then Exit Function
        For i = 0 To 2
            channel(i) = CLng("&H" & Mid$(s, 2 * i + 1, 2))
        Next i
    Else
        s = Replace(s, "RGB", "")
        s = Replace(s, "(", "")
        s = Replace(s, ")", "")
        s = Replace(s, ChrW(&HFF0C), ",")
        parts = Split(s, ",")
        If UBound(parts) <> 2 Then Exit Function
        For i = 0 To 2
            If Not IsNumeric(Trim$(parts(i))) Then Exit Function
            number = CDbl(Trim$(parts(i)))
            If number < 0 Or number > 255 Or number <> Fix(number) Then Exit Function
            channel(i) = CLng(number)
        Next i
    End If
    value = RGB(channel(0), channel(1), channel(2))
    ParseColor = True
Invalid:
End Function

Private Function HexColor(ByVal value As Long) As String
    HexColor = "#" & Right$("0" & Hex$(value And &HFF&), 2) & _
        Right$("0" & Hex$((value \ 256) And &HFF&), 2) & _
        Right$("0" & Hex$((value \ 65536) And &HFF&), 2)
End Function
