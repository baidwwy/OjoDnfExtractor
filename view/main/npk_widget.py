# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'npk_widget.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NPKWidget(object):
    def setupUi(self, NPKWidget):
        NPKWidget.setObjectName("NPKWidget")
        NPKWidget.resize(588, 356)
        self.gridLayout_3 = QtWidgets.QGridLayout(NPKWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(NPKWidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_files = QtWidgets.QTableWidget(self.groupBox_2)
        self.tw_files.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tw_files.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_files.setObjectName("tw_files")
        self.tw_files.setColumnCount(2)
        self.tw_files.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_files.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_files.setHorizontalHeaderItem(1, item)
        self.tw_files.horizontalHeader().setStretchLastSection(True)
        self.tw_files.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tw_files, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 2, 1)
        self.groupBox = QtWidgets.QGroupBox(NPKWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cb_replay = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_replay.sizePolicy().hasHeightForWidth())
        self.cb_replay.setSizePolicy(sizePolicy)
        self.cb_replay.setObjectName("cb_replay")
        self.gridLayout_2.addWidget(self.cb_replay, 2, 1, 1, 1)
        self.pb_play = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_play.sizePolicy().hasHeightForWidth())
        self.pb_play.setSizePolicy(sizePolicy)
        self.pb_play.setObjectName("pb_play")
        self.gridLayout_2.addWidget(self.pb_play, 0, 0, 1, 1)
        self.cb_loop = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_loop.sizePolicy().hasHeightForWidth())
        self.cb_loop.setSizePolicy(sizePolicy)
        self.cb_loop.setObjectName("cb_loop")
        self.gridLayout_2.addWidget(self.cb_loop, 2, 0, 1, 1)
        self.pb_pause = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_pause.sizePolicy().hasHeightForWidth())
        self.pb_pause.setSizePolicy(sizePolicy)
        self.pb_pause.setObjectName("pb_pause")
        self.gridLayout_2.addWidget(self.pb_pause, 0, 1, 1, 1)
        self.pb_stop = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_stop.sizePolicy().hasHeightForWidth())
        self.pb_stop.setSizePolicy(sizePolicy)
        self.pb_stop.setObjectName("pb_stop")
        self.gridLayout_2.addWidget(self.pb_stop, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(NPKWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pb_extract = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_extract.sizePolicy().hasHeightForWidth())
        self.pb_extract.setSizePolicy(sizePolicy)
        self.pb_extract.setObjectName("pb_extract")
        self.gridLayout_4.addWidget(self.pb_extract, 3, 1, 1, 1)
        self.pb_add = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy)
        self.pb_add.setObjectName("pb_add")
        self.gridLayout_4.addWidget(self.pb_add, 1, 1, 1, 1)
        self.pb_load_img = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_load_img.sizePolicy().hasHeightForWidth())
        self.pb_load_img.setSizePolicy(sizePolicy)
        self.pb_load_img.setObjectName("pb_load_img")
        self.gridLayout_4.addWidget(self.pb_load_img, 0, 1, 1, 2)
        self.pb_remove = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_remove.sizePolicy().hasHeightForWidth())
        self.pb_remove.setSizePolicy(sizePolicy)
        self.pb_remove.setObjectName("pb_remove")
        self.gridLayout_4.addWidget(self.pb_remove, 1, 2, 1, 1)
        self.pb_replace = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_replace.sizePolicy().hasHeightForWidth())
        self.pb_replace.setSizePolicy(sizePolicy)
        self.pb_replace.setObjectName("pb_replace")
        self.gridLayout_4.addWidget(self.pb_replace, 3, 2, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.retranslateUi(NPKWidget)
        QtCore.QMetaObject.connectSlotsByName(NPKWidget)

    def retranslateUi(self, NPKWidget):
        _translate = QtCore.QCoreApplication.translate
        NPKWidget.setWindowTitle(_translate("NPKWidget", "NPK_Widget"))
        self.groupBox_2.setTitle(_translate("NPKWidget", "文件列表"))
        item = self.tw_files.horizontalHeaderItem(0)
        item.setText(_translate("NPKWidget", "文件尺寸"))
        item = self.tw_files.horizontalHeaderItem(1)
        item.setText(_translate("NPKWidget", "文件名"))
        self.groupBox.setTitle(_translate("NPKWidget", "音效控制"))
        self.cb_replay.setText(_translate("NPKWidget", "重新播放"))
        self.pb_play.setText(_translate("NPKWidget", "播放"))
        self.cb_loop.setText(_translate("NPKWidget", "循环播放"))
        self.pb_pause.setText(_translate("NPKWidget", "暂停"))
        self.pb_stop.setText(_translate("NPKWidget", "停止"))
        self.groupBox_3.setTitle(_translate("NPKWidget", "文件操作"))
        self.pb_extract.setText(_translate("NPKWidget", "提取文件"))
        self.pb_add.setText(_translate("NPKWidget", "添加文件"))
        self.pb_load_img.setText(_translate("NPKWidget", "加载IMG文件"))
        self.pb_remove.setText(_translate("NPKWidget", "移除文件"))
        self.pb_replace.setText(_translate("NPKWidget", "替换文件"))
