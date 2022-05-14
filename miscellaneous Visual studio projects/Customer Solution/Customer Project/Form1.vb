Imports System.IO
Public Class Form1

    Dim FirstNamee As String = ""
    Dim LastNamee As String = ""
    Dim Addresss As String = ""
    Dim Cityy As String = ""
    Dim ZIPP As String = ""

    Dim sr As New StreamWriter("customers.txt") ' crates a text file under the name of 'customers'

    ' Each text box's Enter even procedure
    Private Sub FirstName_Enter(sender As Object, e As EventArgs) Handles FirstName.Enter
        FirstNamee = FirstName.Text
    End Sub
    Private Sub LastName_Enter(sender As Object, e As EventArgs) Handles LastName.Enter
        LastNamee = LastName.Text
    End Sub
    Private Sub Address_Enter(sender As Object, e As EventArgs) Handles Address.Enter
        Addresss = Address.Text
    End Sub
    Private Sub City_Enter(sender As Object, e As EventArgs) Handles City.Enter
        Cityy = City.Text
    End Sub
    Private Sub ZIP_Enter(sender As Object, e As EventArgs) Handles ZIP.Enter
        ZIPP = ZIP.Text
    End Sub

    ' Issue is that enter is not working to get the values for each vairable

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click

        Dim Together As String = FirstNamee & " " & LastNamee
        Dim Place As String = Addresss & ", " & Cityy & ", " & ZIPP
        Dim Spaces As Integer = 0


        ' Checks if at least one of the textboxes are empty
        If (FirstName.Text = String.Empty Or LastName.Text = String.Empty Or Address.Text = String.Empty Or City.Text = String.Empty Or ZIP.Text = String.Empty) Then
            MessageBox.Show("One of the textboxes are empty, please double check that all boxes are filled out", "Incomplete information")
        Else

            If (File.Exists("customers.txt")) Then

                sr.WriteLine(Together)
                sr.WriteLine(Place)
                sr.Close()
                lblMessage.Visible = True
                Spaces = 1
            End If

        End If

    End Sub

    Private Sub frmMain_FormClosing(sender As Object, e As System.Windows.Forms.FormClosingEventArgs) Handles MyBase.FormClosing

        If (MessageBox.Show("Are you sure you want to exit?", "", MessageBoxButtons.YesNo) = DialogResult.No) Then ' If the user doesn't want to close, then the form stays open 
            e.Cancel = True

        End If

    End Sub

    Private Sub Form1_TextChanged(sender As Object, e As EventArgs) Handles FirstName.TextChanged, LastName.TextChanged, Address.TextChanged, City.TextChanged, ZIP.TextChanged
        lblMessage.Visible = False ' If any of the textboxes' text are changed then the 'information saved' text disappears 
    End Sub


End Class
