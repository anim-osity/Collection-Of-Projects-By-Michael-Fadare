' Name:         Workers Project
' Purpose:      Saves worker names to a sequential access files.
' Programmer:   <your name> on <current date>

Option Explicit On
Option Strict On
Option Infer Off

Public Class frmMain
   Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub

    Private Sub txtName_Enter(sender As Object, e As EventArgs) Handles txtName.Enter
        txtName.SelectAll()
    End Sub

    Private Sub txtFilename_KeyPress(sender As Object, e As KeyPressEventArgs) Handles txtFilename.KeyPress
        Dim allowed As String = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
        For Each c As Char In txtFilename.Text
            If allowed.Contains(c) = False Then
                txtFilename.Text = txtFilename.Text.Remove(txtFilename.SelectionStart - 1, 1)
                txtFilename.Select(txtFilename.Text.Count, 0)
            End If
        Next
    End Sub

    Private Sub frmMain_FormClosing(sender As Object, e As System.Windows.Forms.FormClosingEventArgs) Handles MyBase.FormClosing
        If (txtFilename.Text = String.Empty) Then
            MessageBox.Show("Please provide a filename.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation)
            e.Cancel = True
        End If




















    End Sub














End Class
