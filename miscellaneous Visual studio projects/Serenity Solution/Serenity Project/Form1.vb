Imports System.IO

Public Class Form1

    Dim CheckInformation As New CheckInformation


    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        Dim CheckNumber As Integer = txtCheckNumber.Text
        Dim CheckDate As String = txtCheckDate.Text
        Dim CheckAmount As Double = txtCheckAmount.Text

        Dim Amount As String = CStr(CheckAmount)
        Dim Number As String = CStr(CheckNumber)




        File.AppendAllText("Checks.txt", CheckInformation.Write(Amount, Number, CheckDate))


    End Sub



    Private Sub frmMain_FormClosing(sender As Object, e As System.Windows.Forms.FormClosingEventArgs) Handles MyBase.FormClosing

    End Sub


    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Me.Close()
    End Sub

    Private Sub txtCheckAmount_KeyPress(sender As Object, e As KeyPressEventArgs) Handles txtCheckAmount.KeyPress

        If Asc(e.KeyChar) <> 8 Then
            If Asc(e.KeyChar) < 46 Or Asc(e.KeyChar) > 57 Or (Asc(e.KeyChar) < 48 And Asc(e.KeyChar) > 46) Then
                e.Handled = True
            End If

            If (txtCheckAmount.Text.IndexOf(".") >= 0 And e.KeyChar = ".") Then e.Handled = True

        End If

        Dim periodt As String = "."

        Dim position As Integer = txtCheckAmount.Text.IndexOf(periodt)

        If (position > 0) Then
            txtCheckAmount.MaxLength = position + 3
        End If

        If (position = -1) Then
            txtCheckAmount.MaxLength = 32767
        End If

    End Sub

    Private Sub txtCheckNumber_KeyPress(sender As Object, e As KeyPressEventArgs) Handles txtCheckNumber.KeyPress

        If Not Char.IsNumber(e.KeyChar) AndAlso Not Char.IsControl(e.KeyChar) Then e.KeyChar = CChar("")
    End Sub
End Class
