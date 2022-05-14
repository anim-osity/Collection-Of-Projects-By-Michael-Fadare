' Name:         Games Project
' Purpose:      Display all records and records meeting specific criteria.
' Programmer:   <your name> on <current date>



Public Class frmMain

    Dim tb As New DataTable("Table")

    Dim original As New DataTable("Table")

    Dim Counter As New Integer



    Private Sub frmMain_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        'TODO: This line of code loads data into the 'GaloreDataSet.Games' table. You can move, or remove it, as needed.
        Me.GamesTableAdapter.Fill(Me.GaloreDataSet.Games)


        tb.Columns.Add("ID", GetType(Integer))
        tb.Columns.Add("Title", GetType(String))
        tb.Columns.Add("Platform", GetType(String))
        tb.Columns.Add("Rating", GetType(String))
        tb.Columns.Add("Price", GetType(Decimal))
        tb.Columns.Add("NewUsed", GetType(String))
        tb.Columns.Add("Quantity", GetType(Integer))

        original.Columns.Add("ID", GetType(Integer))
        original.Columns.Add("Title", GetType(String))
        original.Columns.Add("Platform", GetType(String))
        original.Columns.Add("Rating", GetType(String))
        original.Columns.Add("Price", GetType(Decimal))
        original.Columns.Add("NewUsed", GetType(String))
        original.Columns.Add("Quantity", GetType(Integer))


        For yes As Integer = 0 To GamesDataGridView.RowCount - 1

            Dim ID As Integer = Integer.Parse(GamesDataGridView.Rows(yes).Cells(0).Value)
            Dim Title As String = (GamesDataGridView.Rows(yes).Cells(1).Value)
            Dim Platform As String = (GamesDataGridView.Rows(yes).Cells(2).Value)
            Dim rating As String = (GamesDataGridView.Rows(yes).Cells(3).Value)
            Dim Price As Decimal = Decimal.Parse(GamesDataGridView.Rows(yes).Cells(4).Value)
            Dim NewUsed As String = (GamesDataGridView.Rows(yes).Cells(5).Value)
            Dim Quantity As Integer = Integer.Parse((GamesDataGridView.Rows(yes).Cells(6).Value))

            original.Rows.Add(ID, Title, Platform, rating, Price, NewUsed, Quantity)

        Next yes

    End Sub

    Private Sub btnExit_Click(sender As Object, e As EventArgs) Handles btnExit.Click
        Me.Close()
    End Sub



    Private Sub btnDisplay_Click(sender As Object, e As EventArgs) Handles btnDisplay.Click

        Dim col As Collection
        col = New Collection

        Dim How As Integer = 1
        Dim Neww As String = GamesDataGridView.Rows(0).Cells(5).Value
        Dim Used As String = GamesDataGridView.Rows(8).Cells(5).Value




        For i = 0 To 1000
            Dim xx As New DataTable("Table")
            xx = New DataTable("Table")
            col.Add(xx, "test" & i)
        Next i

        col(How).Columns.Add("ID", GetType(Integer))
        col(How).Columns.Add("Title", GetType(String))
        col(How).Columns.Add("Platform", GetType(String))
        col(How).Columns.Add("Rating", GetType(String))
        col(How).Columns.Add("Price", GetType(Decimal))
        col(How).Columns.Add("NewUsed", GetType(String))
        col(How).Columns.Add("Quantity", GetType(Integer))


        If (radAll.Checked) Then
            GamesDataGridView.DataSource = original
        End If


        If (radUsed.Checked) Then

            For yes As Integer = 0 To GamesDataGridView.RowCount - 1

                If (GamesDataGridView.Rows(yes).Cells(5).Value) = Used Then

                    Dim ID As Integer = Integer.Parse(GamesDataGridView.Rows(yes).Cells(0).Value)
                    Dim Title As String = (GamesDataGridView.Rows(yes).Cells(1).Value)
                    Dim Platform As String = (GamesDataGridView.Rows(yes).Cells(2).Value)
                    Dim rating As String = (GamesDataGridView.Rows(yes).Cells(3).Value)
                    Dim Price As Decimal = Decimal.Parse(GamesDataGridView.Rows(yes).Cells(4).Value)
                    Dim NewUsed As String = (GamesDataGridView.Rows(yes).Cells(5).Value)
                    Dim Quantity As Integer = Integer.Parse((GamesDataGridView.Rows(yes).Cells(6).Value))

                    col(How).Rows.Add(ID, Title, Platform, rating, Price, NewUsed, Quantity)

                End If

            Next yes

            GamesDataGridView.DataSource = col(How)
            Counter += 1

        End If




        If (radNew.Checked) Then

            For yes As Integer = 0 To GamesDataGridView.RowCount - 1

                If (GamesDataGridView.Rows(yes).Cells(5).Value) = Neww Then

                    Dim ID As Integer = Integer.Parse(GamesDataGridView.Rows(yes).Cells(0).Value)
                    Dim Title As String = (GamesDataGridView.Rows(yes).Cells(1).Value)
                    Dim Platform As String = (GamesDataGridView.Rows(yes).Cells(2).Value)
                    Dim rating As String = (GamesDataGridView.Rows(yes).Cells(3).Value)
                    Dim Price As Decimal = Decimal.Parse(GamesDataGridView.Rows(yes).Cells(4).Value)
                    Dim NewUsed As String = (GamesDataGridView.Rows(yes).Cells(5).Value)
                    Dim Quantity As Integer = Integer.Parse((GamesDataGridView.Rows(yes).Cells(6).Value))

                    col(How).Rows.Add(ID, Title, Platform, rating, Price, NewUsed, Quantity)

                End If

            Next yes

            GamesDataGridView.DataSource = col(How)
            Counter += 1

        End If


        If (radRating.Checked) Then

            For yes As Integer = 0 To GamesDataGridView.RowCount - 1

                If (GamesDataGridView.Rows(yes).Cells(3).Value) = txtRating.Text.ToUpper.Trim Then

                    Dim ID As Integer = Integer.Parse(GamesDataGridView.Rows(yes).Cells(0).Value)
                    Dim Title As String = (GamesDataGridView.Rows(yes).Cells(1).Value)
                    Dim Platform As String = (GamesDataGridView.Rows(yes).Cells(2).Value)
                    Dim rating As String = (GamesDataGridView.Rows(yes).Cells(3).Value)
                    Dim Price As Decimal = Decimal.Parse(GamesDataGridView.Rows(yes).Cells(4).Value)
                    Dim NewUsed As String = (GamesDataGridView.Rows(yes).Cells(5).Value)
                    Dim Quantity As Integer = Integer.Parse((GamesDataGridView.Rows(yes).Cells(6).Value))

                    col(How).Rows.Add(ID, Title, Platform, rating, Price, NewUsed, Quantity)

                End If

            Next yes

            GamesDataGridView.DataSource = col(How)
            Counter += 1

        End If



        If (radPlatform.Checked) Then

            For yes As Integer = 0 To GamesDataGridView.RowCount - 1

                If (GamesDataGridView.Rows(yes).Cells(2).Value) = txtPlatform.Text.ToUpper.Trim Then

                    Dim ID As Integer = Integer.Parse(GamesDataGridView.Rows(yes).Cells(0).Value)
                    Dim Title As String = (GamesDataGridView.Rows(yes).Cells(1).Value)
                    Dim Platform As String = (GamesDataGridView.Rows(yes).Cells(2).Value)
                    Dim rating As String = (GamesDataGridView.Rows(yes).Cells(3).Value)
                    Dim Price As Decimal = Decimal.Parse(GamesDataGridView.Rows(yes).Cells(4).Value)
                    Dim NewUsed As String = (GamesDataGridView.Rows(yes).Cells(5).Value)
                    Dim Quantity As Integer = Integer.Parse((GamesDataGridView.Rows(yes).Cells(6).Value))

                    col(How).Rows.Add(ID, Title, Platform, rating, Price, NewUsed, Quantity)

                End If

            Next yes

            GamesDataGridView.DataSource = col(How)
            Counter += 1

        End If















































    End Sub

    Private Sub radAll_Click(sender As Object, e As EventArgs) Handles radAll.Click
        GamesTableAdapter.Fill(GaloreDataSet.Games)
    End Sub

    Private Sub radPlatform_CheckedChanged(sender As Object, e As EventArgs) Handles radPlatform.CheckedChanged
        txtPlatform.Text = ""
        GamesDataGridView.DataSource = original
    End Sub
End Class
