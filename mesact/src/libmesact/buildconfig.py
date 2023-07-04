import os, traceback

from libmesact import settings

from libmesact import check
from libmesact import buildini
from libmesact import buildhal
from libmesact import buildio
from libmesact import buildmisc
from libmesact import buildss
from libmesact import utilities

def build(parent):
	if parent.backupCB.isChecked():
		utilities.backupFiles(parent)

	# check for linuxcnc paths
	if not os.path.exists(os.path.expanduser('~/linuxcnc')):
		try:
			os.mkdir(os.path.expanduser('~/linuxcnc'))
		except OSError:
			parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')

	if not os.path.exists(os.path.expanduser('~/linuxcnc/configs')):
		try:
			os.mkdir(os.path.expanduser('~/linuxcnc/configs'))
		except OSError:
			parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')

	if not os.path.exists(os.path.expanduser('~/linuxcnc/nc_files')):
		try:
			os.mkdir(os.path.expanduser('~/linuxcnc/nc_files'))
		except OSError:
			parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')

	if parent.subroutineCB.isChecked():
		if not os.path.exists(os.path.expanduser('~/linuxcnc/subroutines')):
			try:
				os.mkdir(os.path.expanduser('~/linuxcnc/subroutines'))
			except OSError:
				parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')

	# set boards
	parent.main_board = parent.boardCB.currentData()
	parent.p1_board = parent.daughterCB_0.currentData()
	parent.p2_board = parent.daughterCB_1.currentData()

	iniFile = os.path.join(parent.configPath, parent.configNameUnderscored + '.ini')
	if os.path.exists(iniFile):
		parent.updateini.update(parent, iniFile)
	else:
		buildini.build(parent)

	buildhal.build(parent)
	buildio.build(parent)
	buildmisc.build(parent)
	#buildss.build(parent)




