' Name:         Proper Case Project
' Purpose:      Displays the name using proper case.
' Programmer:   <your name> on <current date>

Option Explicit On
Option Strict On
Option Infer Off

Public Class frmMain

    Private Sub btnProper_Click(sender As Object, e As EventArgs) Handles btnProper.Click

        Dim Userinput As String = txtName.Text
        Dim intSpaceIndex As Integer
        Dim Length As Integer
        Dim test As String = ""

        Userinput = Userinput.Trim 'Removes all the leading spaces and ending spaces 

        intSpaceIndex = Userinput.IndexOf(" ") ' takes the position of the first space in the user's input 

        Length = Userinput.Length - intSpaceIndex ' The length of the string minus where the space start is how much many characters are remaining


        Do Until Length = 0
            test = test + Userinput(0 + 1)
            lblName.Text = test.ToString
            Length = Length - 1
        Loop










































    End Sub


    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub txtName_Enter(sender As Object, e As EventArgs) Handles txtName.Enter
        txtName.SelectAll()
    End Sub

    Private Sub txtName_TextChanged(sender As Object, e As EventArgs) Handles txtName.TextChanged
        lblName.Text = String.Empty
    End Sub


End Class
