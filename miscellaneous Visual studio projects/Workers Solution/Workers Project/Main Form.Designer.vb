﻿<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class frmMain
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.btnExit = New System.Windows.Forms.Button()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.txtName = New System.Windows.Forms.TextBox()
        Me.btnAdd = New System.Windows.Forms.Button()
        Me.lstWorkers = New System.Windows.Forms.ListBox()
        Me.Filename = New System.Windows.Forms.Label()
        Me.txtFilename = New System.Windows.Forms.TextBox()
        Me.SuspendLayout()
        '
        'btnExit
        '
        Me.btnExit.Location = New System.Drawing.Point(210, 119)
        Me.btnExit.Name = "btnExit"
        Me.btnExit.Size = New System.Drawing.Size(75, 23)
        Me.btnExit.TabIndex = 6
        Me.btnExit.Text = "E&xit"
        Me.btnExit.UseVisualStyleBackColor = True
        '
        'Label2
        '
        Me.Label2.AutoSize = True
        Me.Label2.Location = New System.Drawing.Point(16, 28)
        Me.Label2.Name = "Label2"
        Me.Label2.Size = New System.Drawing.Size(42, 15)
        Me.Label2.TabIndex = 0
        Me.Label2.Text = "&Name:"
        '
        'txtName
        '
        Me.txtName.Location = New System.Drawing.Point(64, 25)
        Me.txtName.Name = "txtName"
        Me.txtName.Size = New System.Drawing.Size(221, 23)
        Me.txtName.TabIndex = 1
        '
        'btnAdd
        '
        Me.btnAdd.Location = New System.Drawing.Point(210, 90)
        Me.btnAdd.Name = "btnAdd"
        Me.btnAdd.Size = New System.Drawing.Size(75, 23)
        Me.btnAdd.TabIndex = 5
        Me.btnAdd.Text = "&Add to list"
        Me.btnAdd.UseVisualStyleBackColor = True
        '
        'lstWorkers
        '
        Me.lstWorkers.FormattingEnabled = True
        Me.lstWorkers.ItemHeight = 15
        Me.lstWorkers.Location = New System.Drawing.Point(19, 88)
        Me.lstWorkers.Name = "lstWorkers"
        Me.lstWorkers.SelectionMode = System.Windows.Forms.SelectionMode.None
        Me.lstWorkers.Size = New System.Drawing.Size(160, 94)
        Me.lstWorkers.TabIndex = 4
        '
        'Filename
        '
        Me.Filename.AutoSize = True
        Me.Filename.Location = New System.Drawing.Point(17, 61)
        Me.Filename.Name = "Filename"
        Me.Filename.Size = New System.Drawing.Size(58, 15)
        Me.Filename.TabIndex = 2
        Me.Filename.Text = "&Filename:"
        '
        'txtFilename
        '
        Me.txtFilename.Location = New System.Drawing.Point(81, 58)
        Me.txtFilename.Name = "txtFilename"
        Me.txtFilename.Size = New System.Drawing.Size(204, 23)
        Me.txtFilename.TabIndex = 3
        '
        'frmMain
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(306, 194)
        Me.Controls.Add(Me.txtFilename)
        Me.Controls.Add(Me.Filename)
        Me.Controls.Add(Me.lstWorkers)
        Me.Controls.Add(Me.btnAdd)
        Me.Controls.Add(Me.txtName)
        Me.Controls.Add(Me.Label2)
        Me.Controls.Add(Me.btnExit)
        Me.Font = New System.Drawing.Font("Segoe UI", 9.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.MaximizeBox = False
        Me.Name = "frmMain"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Restaurant Workers"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents btnExit As Button
    Friend WithEvents Label2 As Label
    Friend WithEvents txtName As TextBox
    Friend WithEvents btnAdd As Button
    Friend WithEvents lstWorkers As ListBox
    Friend WithEvents Filename As Label
    Friend WithEvents txtFilename As TextBox
End Class
