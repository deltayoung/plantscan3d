# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/fboudon/Develop/vplants/branches/treeeditor3d/src/vplants/treeeditor3d/editor.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(713, 551)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.mtgeditor = GLMTGEditor(self.centralwidget)
        self.mtgeditor.setObjectName(_fromUtf8("mtgeditor"))
        self.gridLayout.addWidget(self.mtgeditor, 0, 0, 4, 6)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)
        self.visibilityEnabled = QtGui.QCheckBox(self.centralwidget)
        self.visibilityEnabled.setText(_fromUtf8(""))
        self.visibilityEnabled.setChecked(False)
        self.visibilityEnabled.setObjectName(_fromUtf8("visibilityEnabled"))
        self.gridLayout.addWidget(self.visibilityEnabled, 1, 6, 1, 1)
        self.backVisibilitySlider = QtGui.QSlider(self.centralwidget)
        self.backVisibilitySlider.setEnabled(False)
        self.backVisibilitySlider.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.backVisibilitySlider.setMaximum(100)
        self.backVisibilitySlider.setProperty("value", 100)
        self.backVisibilitySlider.setInvertedControls(True)
        self.backVisibilitySlider.setObjectName(_fromUtf8("backVisibilitySlider"))
        self.gridLayout.addWidget(self.backVisibilitySlider, 2, 6, 1, 1)
        self.frontVisibilitySlider = QtGui.QSlider(self.centralwidget)
        self.frontVisibilitySlider.setEnabled(False)
        self.frontVisibilitySlider.setOrientation(QtCore.Qt.Vertical)
        self.frontVisibilitySlider.setObjectName(_fromUtf8("frontVisibilitySlider"))
        self.gridLayout.addWidget(self.frontVisibilitySlider, 3, 6, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.pointSizeSlider = QtGui.QSlider(self.centralwidget)
        self.pointSizeSlider.setMinimum(1)
        self.pointSizeSlider.setMaximum(10)
        self.pointSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pointSizeSlider.setObjectName(_fromUtf8("pointSizeSlider"))
        self.gridLayout.addWidget(self.pointSizeSlider, 4, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)
        self.pointFilterSlider = QtGui.QSlider(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointFilterSlider.sizePolicy().hasHeightForWidth())
        self.pointFilterSlider.setSizePolicy(sizePolicy)
        self.pointFilterSlider.setMaximum(1000)
        self.pointFilterSlider.setOrientation(QtCore.Qt.Horizontal)
        self.pointFilterSlider.setObjectName(_fromUtf8("pointFilterSlider"))
        self.gridLayout.addWidget(self.pointFilterSlider, 4, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 4, 1, 1)
        self.nodeSizeSlider = QtGui.QSlider(self.centralwidget)
        self.nodeSizeSlider.setMinimum(1)
        self.nodeSizeSlider.setMaximum(10)
        self.nodeSizeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.nodeSizeSlider.setObjectName(_fromUtf8("nodeSizeSlider"))
        self.gridLayout.addWidget(self.nodeSizeSlider, 4, 5, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuExport_MTG = QtGui.QMenu(self.menuFile)
        self.menuExport_MTG.setObjectName(_fromUtf8("menuExport_MTG"))
        self.menuExport_View = QtGui.QMenu(self.menuFile)
        self.menuExport_View.setObjectName(_fromUtf8("menuExport_View"))
        self.menuExport_Points = QtGui.QMenu(self.menuFile)
        self.menuExport_Points.setObjectName(_fromUtf8("menuExport_Points"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuProcess = QtGui.QMenu(self.menubar)
        self.menuProcess.setObjectName(_fromUtf8("menuProcess"))
        self.menuRadius = QtGui.QMenu(self.menuProcess)
        self.menuRadius.setObjectName(_fromUtf8("menuRadius"))
        self.menuAdd_Root = QtGui.QMenu(self.menuProcess)
        self.menuAdd_Root.setObjectName(_fromUtf8("menuAdd_Root"))
        self.menuReconstruction = QtGui.QMenu(self.menuProcess)
        self.menuReconstruction.setObjectName(_fromUtf8("menuReconstruction"))
        self.menuContraction = QtGui.QMenu(self.menuProcess)
        self.menuContraction.setObjectName(_fromUtf8("menuContraction"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuLoad = QtGui.QMenu(self.menubar)
        self.menuLoad.setObjectName(_fromUtf8("menuLoad"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNodesInfo = QtGui.QAction(MainWindow)
        self.actionNodesInfo.setObjectName(_fromUtf8("actionNodesInfo"))
        self.actionImportPoints = QtGui.QAction(MainWindow)
        self.actionImportPoints.setObjectName(_fromUtf8("actionImportPoints"))
        self.actionOpenMTG = QtGui.QAction(MainWindow)
        self.actionOpenMTG.setObjectName(_fromUtf8("actionOpenMTG"))
        self.actionSaveMTG = QtGui.QAction(MainWindow)
        self.actionSaveMTG.setObjectName(_fromUtf8("actionSaveMTG"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionViewMTG = QtGui.QAction(MainWindow)
        self.actionViewMTG.setCheckable(True)
        self.actionViewMTG.setObjectName(_fromUtf8("actionViewMTG"))
        self.actionViewPoints = QtGui.QAction(MainWindow)
        self.actionViewPoints.setCheckable(True)
        self.actionViewPoints.setObjectName(_fromUtf8("actionViewPoints"))
        self.actionAdjustView = QtGui.QAction(MainWindow)
        self.actionAdjustView.setObjectName(_fromUtf8("actionAdjustView"))
        self.actionViewControlPoints = QtGui.QAction(MainWindow)
        self.actionViewControlPoints.setCheckable(True)
        self.actionViewControlPoints.setObjectName(_fromUtf8("actionViewControlPoints"))
        self.actionRefreshView = QtGui.QAction(MainWindow)
        self.actionRefreshView.setObjectName(_fromUtf8("actionRefreshView"))
        self.actionContract = QtGui.QAction(MainWindow)
        self.actionContract.setEnabled(False)
        self.actionContract.setObjectName(_fromUtf8("actionContract"))
        self.actionCreateSkeleton = QtGui.QAction(MainWindow)
        self.actionCreateSkeleton.setEnabled(False)
        self.actionCreateSkeleton.setObjectName(_fromUtf8("actionCreateSkeleton"))
        self.actionExportGeom = QtGui.QAction(MainWindow)
        self.actionExportGeom.setObjectName(_fromUtf8("actionExportGeom"))
        self.actionViewContractedPoints = QtGui.QAction(MainWindow)
        self.actionViewContractedPoints.setCheckable(True)
        self.actionViewContractedPoints.setObjectName(_fromUtf8("actionViewContractedPoints"))
        self.actionImportContractedPoints = QtGui.QAction(MainWindow)
        self.actionImportContractedPoints.setEnabled(False)
        self.actionImportContractedPoints.setObjectName(_fromUtf8("actionImportContractedPoints"))
        self.actionExportContractedPoints = QtGui.QAction(MainWindow)
        self.actionExportContractedPoints.setEnabled(False)
        self.actionExportContractedPoints.setObjectName(_fromUtf8("actionExportContractedPoints"))
        self.actionView3DModel = QtGui.QAction(MainWindow)
        self.actionView3DModel.setCheckable(True)
        self.actionView3DModel.setObjectName(_fromUtf8("actionView3DModel"))
        self.actionComputeRadius = QtGui.QAction(MainWindow)
        self.actionComputeRadius.setObjectName(_fromUtf8("actionComputeRadius"))
        self.actionAverageRadius = QtGui.QAction(MainWindow)
        self.actionAverageRadius.setObjectName(_fromUtf8("actionAverageRadius"))
        self.actionFilterRadius = QtGui.QAction(MainWindow)
        self.actionFilterRadius.setObjectName(_fromUtf8("actionFilterRadius"))
        self.actionCheckMTG = QtGui.QAction(MainWindow)
        self.actionCheckMTG.setObjectName(_fromUtf8("actionCheckMTG"))
        self.actionExportNodeList = QtGui.QAction(MainWindow)
        self.actionExportNodeList.setObjectName(_fromUtf8("actionExportNodeList"))
        self.actionUndo = QtGui.QAction(MainWindow)
        self.actionUndo.setEnabled(False)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))
        self.actionPuu1 = QtGui.QAction(MainWindow)
        self.actionPuu1.setObjectName(_fromUtf8("actionPuu1"))
        self.actionPuu3 = QtGui.QAction(MainWindow)
        self.actionPuu3.setObjectName(_fromUtf8("actionPuu3"))
        self.actionCherry = QtGui.QAction(MainWindow)
        self.actionCherry.setObjectName(_fromUtf8("actionCherry"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveSnapshot = QtGui.QAction(MainWindow)
        self.actionSaveSnapshot.setObjectName(_fromUtf8("actionSaveSnapshot"))
        self.actionRevolveAroundScene = QtGui.QAction(MainWindow)
        self.actionRevolveAroundScene.setObjectName(_fromUtf8("actionRevolveAroundScene"))
        self.actionShowAll = QtGui.QAction(MainWindow)
        self.actionShowAll.setObjectName(_fromUtf8("actionShowAll"))
        self.actionReorient = QtGui.QAction(MainWindow)
        self.actionReorient.setObjectName(_fromUtf8("actionReorient"))
        self.actionXuReconstruction = QtGui.QAction(MainWindow)
        self.actionXuReconstruction.setObjectName(_fromUtf8("actionXuReconstruction"))
        self.actionRootBottom = QtGui.QAction(MainWindow)
        self.actionRootBottom.setObjectName(_fromUtf8("actionRootBottom"))
        self.actionRootTop = QtGui.QAction(MainWindow)
        self.actionRootTop.setObjectName(_fromUtf8("actionRootTop"))
        self.actionSubSampling = QtGui.QAction(MainWindow)
        self.actionSubSampling.setObjectName(_fromUtf8("actionSubSampling"))
        self.actionTest = QtGui.QAction(MainWindow)
        self.actionTest.setObjectName(_fromUtf8("actionTest"))
        self.actionRedo = QtGui.QAction(MainWindow)
        self.actionRedo.setEnabled(False)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))
        self.actionEuclidianContraction = QtGui.QAction(MainWindow)
        self.actionEuclidianContraction.setObjectName(_fromUtf8("actionEuclidianContraction"))
        self.actionRiemannianContraction = QtGui.QAction(MainWindow)
        self.actionRiemannianContraction.setObjectName(_fromUtf8("actionRiemannianContraction"))
        self.actionAngleEstimation = QtGui.QAction(MainWindow)
        self.actionAngleEstimation.setObjectName(_fromUtf8("actionAngleEstimation"))
        self.actionAs_nothing = QtGui.QAction(MainWindow)
        self.actionAs_nothing.setObjectName(_fromUtf8("actionAs_nothing"))
        self.actionAs_picture = QtGui.QAction(MainWindow)
        self.actionAs_picture.setObjectName(_fromUtf8("actionAs_picture"))
        self.actionExportPoints = QtGui.QAction(MainWindow)
        self.actionExportPoints.setObjectName(_fromUtf8("actionExportPoints"))
        self.actionOpen_Project = QtGui.QAction(MainWindow)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionSave_Project = QtGui.QAction(MainWindow)
        self.actionSave_Project.setObjectName(_fromUtf8("actionSave_Project"))
        self.actionTagScale = QtGui.QAction(MainWindow)
        self.actionTagScale.setObjectName(_fromUtf8("actionTagScale"))
        self.menuExport_MTG.addAction(self.actionExportNodeList)
        self.menuExport_View.addAction(self.actionExportGeom)
        self.menuExport_View.addAction(self.actionSaveSnapshot)
        self.menuExport_Points.addAction(self.actionExportPoints)
        self.menuExport_Points.addAction(self.actionExportContractedPoints)
        self.menuFile.addAction(self.actionOpen_Project)
        self.menuFile.addAction(self.actionSave_Project)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpenMTG)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveMTG)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImportPoints)
        self.menuFile.addAction(self.actionImportContractedPoints)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport_MTG.menuAction())
        self.menuFile.addAction(self.menuExport_View.menuAction())
        self.menuFile.addAction(self.menuExport_Points.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionViewMTG)
        self.menuView.addAction(self.actionViewControlPoints)
        self.menuView.addAction(self.actionViewPoints)
        self.menuView.addAction(self.actionViewContractedPoints)
        self.menuView.addAction(self.actionView3DModel)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionRefreshView)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionAdjustView)
        self.menuRadius.addAction(self.actionComputeRadius)
        self.menuRadius.addSeparator()
        self.menuRadius.addAction(self.actionAverageRadius)
        self.menuRadius.addAction(self.actionFilterRadius)
        self.menuAdd_Root.addAction(self.actionRootBottom)
        self.menuAdd_Root.addAction(self.actionRootTop)
        self.menuReconstruction.addAction(self.actionXuReconstruction)
        self.menuReconstruction.addAction(self.actionCreateSkeleton)
        self.menuContraction.addAction(self.actionEuclidianContraction)
        self.menuContraction.addAction(self.actionRiemannianContraction)
        self.menuContraction.addAction(self.actionContract)
        self.menuProcess.addAction(self.menuAdd_Root.menuAction())
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.actionSubSampling)
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.menuContraction.menuAction())
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.menuReconstruction.menuAction())
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.menuRadius.menuAction())
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.actionAngleEstimation)
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.actionCheckMTG)
        self.menuProcess.addSeparator()
        self.menuProcess.addAction(self.actionTagScale)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionRevolveAroundScene)
        self.menuEdit.addAction(self.actionShowAll)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionReorient)
        self.menuLoad.addAction(self.actionPuu1)
        self.menuLoad.addAction(self.actionPuu3)
        self.menuLoad.addAction(self.actionCherry)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuLoad.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.visibilityEnabled, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.frontVisibilitySlider.setEnabled)
        QtCore.QObject.connect(self.visibilityEnabled, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.backVisibilitySlider.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MTG Editor", None))
        self.label_3.setText(_translate("MainWindow", "Clip", None))
        self.label.setText(_translate("MainWindow", "PointSize", None))
        self.label_2.setText(_translate("MainWindow", "PointFilter", None))
        self.label_4.setText(_translate("MainWindow", "NodeSize", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuExport_MTG.setTitle(_translate("MainWindow", "Export MTG", None))
        self.menuExport_View.setTitle(_translate("MainWindow", "Export View", None))
        self.menuExport_Points.setTitle(_translate("MainWindow", "Export Points", None))
        self.menuView.setTitle(_translate("MainWindow", "View", None))
        self.menuProcess.setTitle(_translate("MainWindow", "Process", None))
        self.menuRadius.setTitle(_translate("MainWindow", "Radius", None))
        self.menuAdd_Root.setTitle(_translate("MainWindow", "Add Root", None))
        self.menuReconstruction.setTitle(_translate("MainWindow", "Reconstruction", None))
        self.menuContraction.setTitle(_translate("MainWindow", "Contraction", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.menuLoad.setTitle(_translate("MainWindow", "Load", None))
        self.actionNodesInfo.setText(_translate("MainWindow", "Import Debug Info", None))
        self.actionImportPoints.setText(_translate("MainWindow", "Import Points", None))
        self.actionImportPoints.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionOpenMTG.setText(_translate("MainWindow", "Open MTG", None))
        self.actionOpenMTG.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionSaveMTG.setText(_translate("MainWindow", "Save MTG as", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionViewMTG.setText(_translate("MainWindow", "MTG", None))
        self.actionViewPoints.setText(_translate("MainWindow", "Points", None))
        self.actionAdjustView.setText(_translate("MainWindow", "Adjust View", None))
        self.actionViewControlPoints.setText(_translate("MainWindow", "Control Points", None))
        self.actionRefreshView.setText(_translate("MainWindow", "Refresh View", None))
        self.actionContract.setText(_translate("MainWindow", "Preuksakarn et al.", None))
        self.actionCreateSkeleton.setText(_translate("MainWindow", "Preuksakarn et al.", None))
        self.actionExportGeom.setText(_translate("MainWindow", "As PlantGL file", None))
        self.actionViewContractedPoints.setText(_translate("MainWindow", "Contracted Points", None))
        self.actionImportContractedPoints.setText(_translate("MainWindow", "Import Contracted Points", None))
        self.actionExportContractedPoints.setText(_translate("MainWindow", "Export Contracted Points", None))
        self.actionView3DModel.setText(_translate("MainWindow", "3D Model", None))
        self.actionComputeRadius.setText(_translate("MainWindow", "Computing", None))
        self.actionAverageRadius.setText(_translate("MainWindow", "Averaging", None))
        self.actionFilterRadius.setText(_translate("MainWindow", "Filtering", None))
        self.actionCheckMTG.setText(_translate("MainWindow", "CheckMTG", None))
        self.actionExportNodeList.setText(_translate("MainWindow", "As Node List", None))
        self.actionUndo.setText(_translate("MainWindow", "Undo", None))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z", None))
        self.actionPuu1.setText(_translate("MainWindow", "puu1", None))
        self.actionPuu1.setShortcut(_translate("MainWindow", "Ctrl+1", None))
        self.actionPuu3.setText(_translate("MainWindow", "puu3", None))
        self.actionPuu3.setShortcut(_translate("MainWindow", "Ctrl+3", None))
        self.actionCherry.setText(_translate("MainWindow", "cherry", None))
        self.actionCherry.setShortcut(_translate("MainWindow", "Ctrl+9", None))
        self.actionSave.setText(_translate("MainWindow", "Save MTG", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionSaveSnapshot.setText(_translate("MainWindow", "As snapshot", None))
        self.actionRevolveAroundScene.setText(_translate("MainWindow", "Revolve Around Scene", None))
        self.actionShowAll.setText(_translate("MainWindow", "Show All", None))
        self.actionReorient.setText(_translate("MainWindow", "Swap Y and Z", None))
        self.actionXuReconstruction.setText(_translate("MainWindow", "Xu et al.", None))
        self.actionRootBottom.setText(_translate("MainWindow", "Bottom", None))
        self.actionRootTop.setText(_translate("MainWindow", "Top", None))
        self.actionSubSampling.setText(_translate("MainWindow", "Sub-Sampling", None))
        self.actionTest.setText(_translate("MainWindow", "test", None))
        self.actionRedo.setText(_translate("MainWindow", "Redo", None))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Y", None))
        self.actionEuclidianContraction.setText(_translate("MainWindow", "Euclidian Contraction", None))
        self.actionRiemannianContraction.setText(_translate("MainWindow", "Riemannian Contraction", None))
        self.actionAngleEstimation.setText(_translate("MainWindow", "Angle Estimation", None))
        self.actionAs_nothing.setText(_translate("MainWindow", "As nothing", None))
        self.actionAs_picture.setText(_translate("MainWindow", "As picture", None))
        self.actionExportPoints.setText(_translate("MainWindow", "Export Current Points", None))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project", None))
        self.actionSave_Project.setText(_translate("MainWindow", "Save Project", None))
        self.actionTagScale.setText(_translate("MainWindow", "Tag Scale", None))

from mtgeditorwidget import GLMTGEditor
