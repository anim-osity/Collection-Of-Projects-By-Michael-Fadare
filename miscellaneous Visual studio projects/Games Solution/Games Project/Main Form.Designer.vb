<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class frmMain
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
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
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Dim DataGridViewCellStyle1 As System.Windows.Forms.DataGridViewCellStyle = New System.Windows.Forms.DataGridViewCellStyle()
        Me.GaloreDataSet = New Games_Project.GaloreDataSet()
        Me.GamesBindingSource = New System.Windows.Forms.BindingSource(Me.components)
        Me.GamesTableAdapter = New Games_Project.GaloreDataSetTableAdapters.GamesTableAdapter()
        Me.TableAdapterManager = New Games_Project.GaloreDataSetTableAdapters.TableAdapterManager()
        Me.GamesDataGridView = New System.Windows.Forms.DataGridView()
        Me.DataGridViewTextBoxColumn1 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.DataGridViewTextBoxColumn2 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.DataGridViewTextBoxColumn3 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.DataGridViewTextBoxColumn4 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.DataGridViewTextBoxColumn5 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.DataGridViewTextBoxColumn6 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.DataGridViewTextBoxColumn7 = New System.Windows.Forms.DataGridViewTextBoxColumn()
        Me.GroupBox1 = New System.Windows.Forms.GroupBox()
        Me.radAll = New System.Windows.Forms.RadioButton()
        Me.radUsed = New System.Windows.Forms.RadioButton()
        Me.radNew = New System.Windows.Forms.RadioButton()
        Me.txtRating = New System.Windows.Forms.TextBox()
        Me.radRating = New System.Windows.Forms.RadioButton()
        Me.txtPlatform = New System.Windows.Forms.TextBox()
        Me.radPlatform = New System.Windows.Forms.RadioButton()
        Me.btnExit = New System.Windows.Forms.Button()
        Me.btnDisplay = New System.Windows.Forms.Button()
        CType(Me.GaloreDataSet, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.GamesBindingSource, System.ComponentModel.ISupportInitialize).BeginInit()
        CType(Me.GamesDataGridView, System.ComponentModel.ISupportInitialize).BeginInit()
        Me.GroupBox1.SuspendLayout()
        Me.SuspendLayout()
        '
        'GaloreDataSet
        '
        Me.GaloreDataSet.DataSetName = "GaloreDataSet"
        Me.GaloreDataSet.SchemaSerializationMode = System.Data.SchemaSerializationMode.IncludeSchema
        '
        'GamesBindingSource
        '
        Me.GamesBindingSource.DataMember = "Games"
        Me.GamesBindingSource.DataSource = Me.GaloreDataSet
        '
        'GamesTableAdapter
        '
        Me.GamesTableAdapter.ClearBeforeFill = True
        '
        'TableAdapterManager
        '
        Me.TableAdapterManager.BackupDataSetBeforeUpdate = False
        Me.TableAdapterManager.GamesTableAdapter = Me.GamesTableAdapter
        Me.TableAdapterManager.UpdateOrder = Games_Project.GaloreDataSetTableAdapters.TableAdapterManager.UpdateOrderOption.InsertUpdateDelete
        '
        'GamesDataGridView
        '
        Me.GamesDataGridView.AllowUserToAddRows = False
        Me.GamesDataGridView.AllowUserToDeleteRows = False
        Me.GamesDataGridView.AutoGenerateColumns = False
        Me.GamesDataGridView.AutoSizeColumnsMode = System.Windows.Forms.DataGridViewAutoSizeColumnsMode.Fill
        Me.GamesDataGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize
        Me.GamesDataGridView.Columns.AddRange(New System.Windows.Forms.DataGridViewColumn() {Me.DataGridViewTextBoxColumn1, Me.DataGridViewTextBoxColumn2, Me.DataGridViewTextBoxColumn3, Me.DataGridViewTextBoxColumn4, Me.DataGridViewTextBoxColumn5, Me.DataGridViewTextBoxColumn6, Me.DataGridViewTextBoxColumn7})
        Me.GamesDataGridView.DataSource = Me.GamesBindingSource
        Me.GamesDataGridView.Location = New System.Drawing.Point(16, 2)
        Me.GamesDataGridView.Name = "GamesDataGridView"
        Me.GamesDataGridView.ReadOnly = True
        Me.GamesDataGridView.RowHeadersVisible = False
        Me.GamesDataGridView.Size = New System.Drawing.Size(574, 309)
        Me.GamesDataGridView.TabIndex = 2
        '
        'DataGridViewTextBoxColumn1
        '
        Me.DataGridViewTextBoxColumn1.DataPropertyName = "ID"
        Me.DataGridViewTextBoxColumn1.HeaderText = "ID"
        Me.DataGridViewTextBoxColumn1.Name = "DataGridViewTextBoxColumn1"
        Me.DataGridViewTextBoxColumn1.ReadOnly = True
        '
        'DataGridViewTextBoxColumn2
        '
        Me.DataGridViewTextBoxColumn2.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.AllCells
        Me.DataGridViewTextBoxColumn2.DataPropertyName = "Title"
        Me.DataGridViewTextBoxColumn2.HeaderText = "Title"
        Me.DataGridViewTextBoxColumn2.Name = "DataGridViewTextBoxColumn2"
        Me.DataGridViewTextBoxColumn2.ReadOnly = True
        Me.DataGridViewTextBoxColumn2.Width = 55
        '
        'DataGridViewTextBoxColumn3
        '
        Me.DataGridViewTextBoxColumn3.DataPropertyName = "Platform"
        Me.DataGridViewTextBoxColumn3.HeaderText = "Platform"
        Me.DataGridViewTextBoxColumn3.Name = "DataGridViewTextBoxColumn3"
        Me.DataGridViewTextBoxColumn3.ReadOnly = True
        '
        'DataGridViewTextBoxColumn4
        '
        Me.DataGridViewTextBoxColumn4.DataPropertyName = "Rating"
        Me.DataGridViewTextBoxColumn4.HeaderText = "Rating"
        Me.DataGridViewTextBoxColumn4.Name = "DataGridViewTextBoxColumn4"
        Me.DataGridViewTextBoxColumn4.ReadOnly = True
        '
        'DataGridViewTextBoxColumn5
        '
        Me.DataGridViewTextBoxColumn5.DataPropertyName = "Price"
        Me.DataGridViewTextBoxColumn5.HeaderText = "Price"
        Me.DataGridViewTextBoxColumn5.Name = "DataGridViewTextBoxColumn5"
        Me.DataGridViewTextBoxColumn5.ReadOnly = True
        '
        'DataGridViewTextBoxColumn6
        '
        Me.DataGridViewTextBoxColumn6.AutoSizeMode = System.Windows.Forms.DataGridViewAutoSizeColumnMode.ColumnHeader
        Me.DataGridViewTextBoxColumn6.DataPropertyName = "NewUsed"
        DataGridViewCellStyle1.Alignment = System.Windows.Forms.DataGridViewContentAlignment.MiddleCenter
        Me.DataGridViewTextBoxColumn6.DefaultCellStyle = DataGridViewCellStyle1
        Me.DataGridViewTextBoxColumn6.HeaderText = "New/Used"
        Me.DataGridViewTextBoxColumn6.Name = "DataGridViewTextBoxColumn6"
        Me.DataGridViewTextBoxColumn6.ReadOnly = True
        Me.DataGridViewTextBoxColumn6.Width = 87
        '
        'DataGridViewTextBoxColumn7
        '
        Me.DataGridViewTextBoxColumn7.DataPropertyName = "Quantity"
        Me.DataGridViewTextBoxColumn7.HeaderText = "Quantity"
        Me.DataGridViewTextBoxColumn7.Name = "DataGridViewTextBoxColumn7"
        Me.DataGridViewTextBoxColumn7.ReadOnly = True
        '
        'GroupBox1
        '
        Me.GroupBox1.Controls.Add(Me.radAll)
        Me.GroupBox1.Controls.Add(Me.radUsed)
        Me.GroupBox1.Controls.Add(Me.radNew)
        Me.GroupBox1.Controls.Add(Me.txtRating)
        Me.GroupBox1.Controls.Add(Me.radRating)
        Me.GroupBox1.Controls.Add(Me.txtPlatform)
        Me.GroupBox1.Controls.Add(Me.radPlatform)
        Me.GroupBox1.Location = New System.Drawing.Point(619, 13)
        Me.GroupBox1.Name = "GroupBox1"
        Me.GroupBox1.Size = New System.Drawing.Size(94, 227)
        Me.GroupBox1.TabIndex = 3
        Me.GroupBox1.TabStop = False
        '
        'radAll
        '
        Me.radAll.AutoSize = True
        Me.radAll.Checked = True
        Me.radAll.Location = New System.Drawing.Point(7, 22)
        Me.radAll.Name = "radAll"
        Me.radAll.Size = New System.Drawing.Size(39, 19)
        Me.radAll.TabIndex = 0
        Me.radAll.TabStop = True
        Me.radAll.Text = "&All"
        Me.radAll.UseVisualStyleBackColor = True
        '
        'radUsed
        '
        Me.radUsed.AutoSize = True
        Me.radUsed.Location = New System.Drawing.Point(9, 198)
        Me.radUsed.Name = "radUsed"
        Me.radUsed.Size = New System.Drawing.Size(51, 19)
        Me.radUsed.TabIndex = 6
        Me.radUsed.Text = "&Used"
        Me.radUsed.UseVisualStyleBackColor = True
        '
        'radNew
        '
        Me.radNew.AutoSize = True
        Me.radNew.Location = New System.Drawing.Point(9, 170)
        Me.radNew.Name = "radNew"
        Me.radNew.Size = New System.Drawing.Size(49, 19)
        Me.radNew.TabIndex = 5
        Me.radNew.Text = "&New"
        Me.radNew.UseVisualStyleBackColor = True
        '
        'txtRating
        '
        Me.txtRating.Location = New System.Drawing.Point(7, 134)
        Me.txtRating.Name = "txtRating"
        Me.txtRating.Size = New System.Drawing.Size(38, 23)
        Me.txtRating.TabIndex = 4
        '
        'radRating
        '
        Me.radRating.AutoSize = True
        Me.radRating.Location = New System.Drawing.Point(7, 110)
        Me.radRating.Name = "radRating"
        Me.radRating.Size = New System.Drawing.Size(59, 19)
        Me.radRating.TabIndex = 3
        Me.radRating.Text = "&Rating"
        Me.radRating.UseVisualStyleBackColor = True
        '
        'txtPlatform
        '
        Me.txtPlatform.Location = New System.Drawing.Point(7, 74)
        Me.txtPlatform.Name = "txtPlatform"
        Me.txtPlatform.Size = New System.Drawing.Size(38, 23)
        Me.txtPlatform.TabIndex = 2
        '
        'radPlatform
        '
        Me.radPlatform.AutoSize = True
        Me.radPlatform.Location = New System.Drawing.Point(7, 50)
        Me.radPlatform.Name = "radPlatform"
        Me.radPlatform.Size = New System.Drawing.Size(71, 19)
        Me.radPlatform.TabIndex = 1
        Me.radPlatform.Text = "&Platform"
        Me.radPlatform.UseVisualStyleBackColor = True
        '
        'btnExit
        '
        Me.btnExit.Location = New System.Drawing.Point(619, 288)
        Me.btnExit.Name = "btnExit"
        Me.btnExit.Size = New System.Drawing.Size(75, 23)
        Me.btnExit.TabIndex = 1
        Me.btnExit.Text = "E&xit"
        Me.btnExit.UseVisualStyleBackColor = True
        '
        'btnDisplay
        '
        Me.btnDisplay.Location = New System.Drawing.Point(619, 251)
        Me.btnDisplay.Name = "btnDisplay"
        Me.btnDisplay.Size = New System.Drawing.Size(75, 23)
        Me.btnDisplay.TabIndex = 0
        Me.btnDisplay.Text = "&Display"
        Me.btnDisplay.UseVisualStyleBackColor = True
        '
        'frmMain
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(7.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.ClientSize = New System.Drawing.Size(729, 344)
        Me.Controls.Add(Me.btnDisplay)
        Me.Controls.Add(Me.btnExit)
        Me.Controls.Add(Me.GroupBox1)
        Me.Controls.Add(Me.GamesDataGridView)
        Me.Font = New System.Drawing.Font("Segoe UI", 9.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.MaximizeBox = False
        Me.Name = "frmMain"
        Me.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen
        Me.Text = "Games Galore"
        CType(Me.GaloreDataSet, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.GamesBindingSource, System.ComponentModel.ISupportInitialize).EndInit()
        CType(Me.GamesDataGridView, System.ComponentModel.ISupportInitialize).EndInit()
        Me.GroupBox1.ResumeLayout(False)
        Me.GroupBox1.PerformLayout()
        Me.ResumeLayout(False)

    End Sub

    Friend WithEvents GaloreDataSet As GaloreDataSet
    Friend WithEvents GamesBindingSource As BindingSource
    Friend WithEvents GamesTableAdapter As GaloreDataSetTableAdapters.GamesTableAdapter
    Friend WithEvents TableAdapterManager As GaloreDataSetTableAdapters.TableAdapterManager
    Friend WithEvents GamesDataGridView As DataGridView
    Friend WithEvents GroupBox1 As GroupBox
    Friend WithEvents radUsed As RadioButton
    Friend WithEvents radNew As RadioButton
    Friend WithEvents txtRating As TextBox
    Friend WithEvents radRating As RadioButton
    Friend WithEvents txtPlatform As TextBox
    Friend WithEvents radPlatform As RadioButton
    Friend WithEvents btnExit As Button
    Friend WithEvents DataGridViewTextBoxColumn1 As DataGridViewTextBoxColumn
    Friend WithEvents DataGridViewTextBoxColumn2 As DataGridViewTextBoxColumn
    Friend WithEvents DataGridViewTextBoxColumn3 As DataGridViewTextBoxColumn
    Friend WithEvents DataGridViewTextBoxColumn4 As DataGridViewTextBoxColumn
    Friend WithEvents DataGridViewTextBoxColumn5 As DataGridViewTextBoxColumn
    Friend WithEvents DataGridViewTextBoxColumn6 As DataGridViewTextBoxColumn
    Friend WithEvents DataGridViewTextBoxColumn7 As DataGridViewTextBoxColumn
    Friend WithEvents radAll As RadioButton
    Friend WithEvents btnDisplay As Button
End Class
