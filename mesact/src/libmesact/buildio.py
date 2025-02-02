import os
from datetime import datetime

from libmesact import firmware

'''
	{'Home and Limit':[
		{'Joint 0':['Joint 0 Plus Home', 'Joint 0 Minus Home', 'Joint 0 Plus Minus Home']},
		{'Joint 1':['Joint 1 Plus Home', 'Joint 1 Minus Home', 'Joint 1 Plus Minus Home']},
		{'Joint 2':['Joint 2 Plus Home', 'Joint 2 Minus Home', 'Joint 2 Plus Minus Home']},
		{'Joint 3':['Joint 3 Plus Home', 'Joint 3 Minus Home', 'Joint 3 Plus Minus Home']},
		{'Joint 4':['Joint 4 Plus Home', 'Joint 4 Minus Home', 'Joint 4 Plus Minus Home']},
		{'Joint 5':['Joint 5 Plus Home', 'Joint 5 Minus Home', 'Joint 5 Plus Minus Home']},
		{'Joint 6':['Joint 6 Plus Home', 'Joint 6 Minus Home', 'Joint 6 Plus Minus Home']},
		{'Joint 7':['Joint 7 Plus Home', 'Joint 7 Minus Home', 'Joint 7 Plus Minus Home']},
		{'Joint 8':['Joint 8 Plus Home', 'Joint 8 Minus Home', 'Joint 8 Plus Minus Home']}]},
'''
INPUTS = {
	'Joint 0 Home':'net joint-0-home joint.0.home-sw-in <=',
	'Joint 1 Home':'net joint-1-home joint.1.home-sw-in <=',
	'Joint 2 Home':'net joint-2-home joint.2.home-sw-in <=',
	'Joint 3 Home':'net joint-3-home joint.3.home-sw-in <=',
	'Joint 4 Home':'net joint-4-home joint.4.home-sw-in <=',
	'Joint 5 Home':'net joint-5-home joint.5.home-sw-in <=',
	'Joint 6 Home':'net joint-6-home joint.6.home-sw-in <=',
	'Joint 7 Home':'net joint-7-home joint.7.home-sw-in <=',
	'Joint 8 Home':'net joint-8-home joint.8.home-sw-in <=',
	'Home All':'net home-all halui.home-all <=',

	'Joint 0 Plus':'net pos-limit-joint-0 joint.0.pos-lim-sw-in <=',
	'Joint 0 Minus':'net neg-limit-joint-0 joint.0.neg-lim-sw-in <=',
	'Joint 0 Both':'net both-limit-joint-0 joint.0.pos-lim-sw-in\n'
		'net both-limit-joint-0 joint.0.neg-lim-sw-in <=',
	'Joint 1 Plus':'net pos-limit-joint-1 joint.1.pos-lim-sw-in <=',
	'Joint 1 Minus':'net neg-limit-joint-1 joint.1.neg-lim-sw-in <=',
	'Joint 1 Both':'net both-limit-joint-1 joint.1.pos-lim-sw-in\n'
		'net both-limit-joint-1 joint.1.neg-lim-sw-in <=',
	'Joint 2 Plus':'net pos-limit-joint-2 joint.2.pos-lim-sw-in <=',
	'Joint 2 Minus':'net neg-limit-joint-2 joint.2.neg-lim-sw-in <=',
	'Joint 2 Both':'net both-limit-joint-2 joint.2.pos-lim-sw-in\n'
		'net both-limit-joint-2 joint.2.neg-lim-sw-in <=',
	'Joint 3 Plus':'net pos-limit-joint-3 joint.3.pos-lim-sw-in <=',
	'Joint 3 Minus':'net neg-limit-joint-3 joint.3.neg-lim-sw-in <=',
	'Joint 3 Both':'net both-limit-joint-3 joint.3.pos-lim-sw-in\n'
		'net both-limit-joint-3 joint..neg-lim-sw-in <=',
	'Joint 4 Plus':'net pos-limit-joint-4 joint.4.pos-lim-sw-in <=',
	'Joint 4 Minus':'net neg-limit-joint-4 joint.4.neg-lim-sw-in <=',
	'Joint 4 Both':'net both-limit-joint-4 joint.4.pos-lim-sw-in\n'
		'net both-limit-joint-4 joint.4.neg-lim-sw-in <=',
	'Joint 5 Plus':'net pos-limit-joint-5 joint.5.pos-lim-sw-in <=',
	'Joint 5 Minus':'net neg-limit-joint-5 joint.5.neg-lim-sw-in <=',
	'Joint 5 Both':'net both-limit-joint-5 joint.5.pos-lim-sw-in\n'
		'net both-limit-joint-5 joint.5.neg-lim-sw-in <=',
	'Joint 6 Plus':'net pos-limit-joint-6 joint.6.pos-lim-sw-in <=',
	'Joint 6 Minus':'net neg-limit-joint-6 joint.6.neg-lim-sw-in <=',
	'Joint 6 Both':'net both-limit-joint-6 joint.6.pos-lim-sw-in\n'
		'net both-limit-joint-6 joint.6.neg-lim-sw-in <=',
	'Joint 7 Plus':'net pos-limit-joint-7 joint.7.pos-lim-sw-in <=',
	'Joint 7 Minus':'net neg-limit-joint-7 joint.7.neg-lim-sw-in <=',
	'Joint 7 Both':'net both-limit-joint-7 joint.7.pos-lim-sw-in\n'
		'net both-limit-joint-7 joint.7.neg-lim-sw-in <=',
	'Joint 8 Plus':'net pos-limit-joint-8 joint.8.pos-lim-sw-in <=',
	'Joint 8 Minus':'net neg-limit-joint-8 joint.8.neg-lim-sw-in <=',
	'Joint 8 Both':'net both-limit-joint-8 joint.8.pos-lim-sw-in\n'
		'net both-limit-joint-8 joint.8.neg-lim-sw-in <=',

	'Joint 0 Plus Home':'net plus-home-joint-0 joint.0.pos-lim-sw-in\n'
		'net plus-home-joint-0 joint.0.home-sw-in <=',
	'Joint 0 Minus Home':'net minus-home-joint-0 joint.0.neg-lim-sw-in\n'
		'net minus-home-joint-0 joint.0.home-sw-in <=',
	'Joint 0 Plus Minus Home':'net plus-minus-home-joint-0 joint.0.pos-lim-sw-in\n'
		'net plus-minus-home-joint-0 joint.0.neg-lim-sw-in\n'
		'net plus-minus-home-joint-0 joint.0.home-sw-in <=',

	'Joint 1 Plus Home':'net plus-home-joint-1 joint.1.pos-lim-sw-in\n'
		'net plus-home-joint-1 joint.1.home-sw-in <=',
	'Joint 1 Minus Home':'net minus-home-joint-1 joint.1.neg-lim-sw-in\n'
		'net minus-home-joint-1 joint.1.home-sw-in <=',
	'Joint 1 Plus Minus Home':'net plus-minus-home-joint-1 joint.1.pos-lim-sw-in\n'
		'net plus-minus-home-joint-1 joint.1.neg-lim-sw-in\n'
		'net plus-minus-home-joint-1 joint.1.home-sw-in <=',

	'Joint 2 Plus Home':'net plus-home-joint-2 joint.2.pos-lim-sw-in\n'
		'net plus-home-joint-2 joint.2.home-sw-in <=',
	'Joint 2 Minus Home':'net minus-home-joint-2 joint.2.neg-lim-sw-in\n'
		'net minus-home-joint-2 joint.2.home-sw-in <=',
	'Joint 2 Plus Minus Home':'net plus-minus-home-joint-2 joint.2.pos-lim-sw-in\n'
		'net plus-minus-home-joint-2 joint.2.neg-lim-sw-in\n'
		'net plus-minus-home-joint-2 joint.2.home-sw-in <=',

	'Joint 3 Plus Home':'net plus-home-joint-3 joint.3.pos-lim-sw-in\n'
		'net plus-home-joint-3 joint.3.home-sw-in <=',
	'Joint 3 Minus Home':'net minus-home-joint-3 joint.3.neg-lim-sw-in\n'
		'net minus-home-joint-3 joint.3.home-sw-in <=',
	'Joint 3 Plus Minus Home':'net plus-minus-home-joint-3 joint.3.pos-lim-sw-in\n'
		'net plus-minus-home-joint-3 joint.3.neg-lim-sw-in\n'
		'net plus-minus-home-joint-3 joint.3.home-sw-in <=',

	'Joint 4 Plus Home':'net plus-home-joint-4 joint.4.pos-lim-sw-in\n'
		'net plus-home-joint-4 joint.4.home-sw-in <=',
	'Joint 4 Minus Home':'net minus-home-joint-4 joint.4.neg-lim-sw-in\n'
		'net minus-home-joint-4 joint.4.home-sw-in <=',
	'Joint 4 Plus Minus Home':'net plus-minus-home-joint-4 joint.4.pos-lim-sw-in\n'
		'net plus-minus-home-joint-4 joint.4.neg-lim-sw-in\n'
		'net plus-minus-home-joint-4 joint.4.home-sw-in <=',

	'Joint 5 Plus Home':'net plus-home-joint-5 joint.5.pos-lim-sw-in\n'
		'net plus-home-joint-5 joint.5.home-sw-in <=',
	'Joint 5 Minus Home':'net minus-home-joint-5 joint.5.neg-lim-sw-in\n'
		'net minus-home-joint-5 joint.5.home-sw-in <=',
	'Joint 5 Plus Minus Home':'net plus-minus-home-joint-5 joint.5.pos-lim-sw-in\n'
		'net plus-minus-home-joint-5 joint.5.neg-lim-sw-in\n'
		'net plus-minus-home-joint-5 joint.5.home-sw-in <=',

	'Joint 6 Plus Home':'net plus-home-joint-6 joint.6.pos-lim-sw-in\n'
		'net plus-home-joint-6 joint.6.home-sw-in <=',
	'Joint 6 Minus Home':'net minus-home-joint-6 joint.6.neg-lim-sw-in\n'
		'net minus-home-joint-6 joint.6.home-sw-in <=',
	'Joint 6 Plus Minus Home':'net plus-minus-home-joint-6 joint.6.pos-lim-sw-in\n'
		'net plus-minus-home-joint-6 joint.6.neg-lim-sw-in\n'
		'net plus-minus-home-joint-6 joint.6.home-sw-in <=',

	'Joint 7 Plus Home':'net plus-home-joint-7 joint.7.pos-lim-sw-in\n'
		'net plus-home-joint-7 joint.7.home-sw-in <=',
	'Joint 7 Minus Home':'net minus-home-joint-7 joint.7.neg-lim-sw-in\n'
		'net minus-home-joint-7 joint.7.home-sw-in <=',
	'Joint 7 Plus Minus Home':'net plus-minus-home-joint-7 joint.7.pos-lim-sw-in\n'
		'net plus-minus-home-joint-7 joint.7.neg-lim-sw-in\n'
		'net plus-minus-home-joint-7 joint.7.home-sw-in <=',

	'Joint 8 Plus Home':'net plus-home-joint-8 joint.8.pos-lim-sw-in\n'
		'net plus-home-joint-8 joint.8.home-sw-in <=',
	'Joint 8 Minus Home':'net minus-home-joint-8 joint.8.neg-lim-sw-in\n'
		'net minus-home-joint-8 joint.8.home-sw-in <=',
	'Joint 8 Plus Minus Home':'net plus-minus-home-joint-8 joint.8.pos-lim-sw-in\n'
		'net plus-minus-home-joint-8 joint.8.neg-lim-sw-in\n'
		'net plus-minus-home-joint-8 joint.8.home-sw-in <=',

	'Jog X Plus':'net jog-x-plus halui.axis.x.plus <=',
	'Jog X Minus':'net jog-x-minus halui.axis.x.minus <=',
	'Jog X Enable':'net jog-x-enable axis.x.jog-enable <=',
	'Jog Y Plus':'net jog-y-plus halui.axis.y.plus <=',
	'Jog Y Minus':'net jog-y-minus halui.axis.y.minus <=',
	'Jog Y Enable':'net jog-y-enable axis.y.jog-enable <=',
	'Jog Z Plus':'net jog-z-plus halui.axis.z.plus <=',
	'Jog Z Minus':'net jog-z-minus halui.axis.z.minus <=',
	'Jog Z Enable':'net jog-z-enable axis.z.jog-enable <=',
	'Jog A Plus':'net jog-a-plus halui.axis.a.plus <=',
	'Jog A Minus':'net jog-a-minus halui.axis.a.minus <=',
	'Jog A Enable':'net jog-a-enable axis.a.jog-enable <=',
	'Jog B Plus':'net jog-b-plus halui.axis.b.plus <=',
	'Jog B Minus':'net jog-b-minus halui.axis.b.minus <=',
	'Jog B Enable':'net jog-b-enable axis.b.jog-enable <=',
	'Jog C Plus':'net jog-c-plus halui.axis.c.plus <=',
	'Jog C Minus':'net jog-c-minus halui.axis.c.minus <=',
	'Jog C Enable':'net jog-c-enable axis.c.jog-enable <=',
	'Jog U Plus':'net jog-u-plus halui.axis.u.plus <=',
	'Jog U Minus':'net jog-u-minus halui.axis.u.minus <=',
	'Jog U Enable':'net jog-u-enable axis.u.jog-enable <=',
	'Jog V Plus':'net jog-v-plus halui.axis.v.plus <=',
	'Jog V Minus':'net jog-v-minus halui.axis.v.minus <=',
	'Jog V Enable':'net jog-v-enable axis.v.jog-enable <=',
	'Jog W Plus':'net jog-w-plus halui.axis.w.plus <=',
	'Jog W Minus':'net jog-w-minus halui.axis.w.minus <=',
	'Jog W Enable':'net jog-w-enable axis.w.jog-enable <=',

	'Probe Input':'net probe-input motion.probe-input <=',
	'Digital 0':'net digital-0-input motion.digital-in-00 <=',
	'Digital 1':'net digital-1-input motion.digital-in-01 <=',
	'Digital 2':'net digital-2-input motion.digital-in-02 <=',
	'Digital 3':'net digital-3-input motion.digital-in-03 <=',

	'Flood':'net coolant-flood iocontrol.0.coolant-flood <=',
	'Mist':'net coolant-mist iocontrol.0.coolant-mist <=',
	'Lube Level':'net lube-level iocontrol.0.lube_level <=',
	'Tool Changed':'net tool-changed iocontrol.0.tool-changed <=',
	'Tool Prepared':'net tool-prepared iocontrol.0.tool-prepared <=',
	'Tool Changer Fault':'iocontrol.0.toolchanger-fault <=',
	'Spindle Amp Fault':'spindle.0.amp-fault-in <=',
	'Spindle Inhibit':'spindle.0.inhibit <=',
	'Spindle Oriented':'spindle.0.is-oriented <=',
	'Spindle Orient Fault':'spindle.0.orient-fault <='
	}
{'Spindle':['Spindle Amp Fault', 'Spindle Inhibit', 'Spindle Oriented', 'Spindle Orient Fault']},

OUTPUTS = {
'Motion Enable': 'net motion-enable =>',
'Coolant Flood': 'net flood-output iocontrol.0.coolant-flood =>',
'Coolant Mist': 'net mist-output iocontrol.0.coolant-mist =>',
'Spindle On': 'net spindle-on =>',
'Spindle CW': 'net spindle-cw spindle.0.forward =>',
'Spindle CCW': 'net spindle-ccw spindle.0.reverse =>',
'Spindle Brake': 'net spindle-brake spindle.0.brake =>',
'E-Stop Out': 'net estop-loopback =>',
'Digital Out 0': 'net digital-out-0 motion.digital-out-00 =>',
'Digital Out 1': 'net digital-out-1 motion.digital-out-01 =>',
'Digital Out 2': 'net digital-out-2 motion.digital-out-02 =>',
'Digital Out 3': 'net digital-out-3 motion.digital-out-03 =>',
'Joint 0 Amp Enable': 'net joint-0-enable joint.0.amp-enable-out =>',
'Joint 1 Amp Enable': 'net joint-1-enable joint.1.amp-enable-out =>',
'Joint 2 Amp Enable': 'net joint-2-enable joint.2.amp-enable-out =>',
'Joint 3 Amp Enable': 'net joint-3-enable joint.3.amp-enable-out =>',
'Joint 4 Amp Enable': 'net joint-4-enable joint.4.amp-enable-out =>',
'Joint 5 Amp Enable': 'net joint-5-enable joint.5.amp-enable-out =>',
'Joint 6 Amp Enable': 'net joint-6-enable joint.6.amp-enable-out =>',
'Joint 7 Amp Enable': 'net joint-7-enable joint.7.amp-enable-out =>',
'Joint 8 Amp Enable': 'net joint-8-enable joint.8.amp-enable-out =>',
}


'''
<pcw-home> I think  may help
mesaflash --device 7i92t --addr 10.10.10.10 --readhmid --dbname1 7i77
<pcw-home> The sserial channels are typically just in sequence:
<pcw-home> 7I76+7I76 0,1 on first 7I76, 2,3 on second
<pcw-home> 7I77+7I77 0,1,2 on first 7I77 3,4,5 on second
<pcw-home> 7I76+7I77, 0,1 on 7I76, 2,3,4 on 7I77

<pcw--home> the field I/O is always on the lower channels (relative to analog on the 7I77 or expansion on the 7I76)

hm2_7i76e.0.7i76.0.0.input-00
hm2_7i76e.0.7i76.0.0.input-00-not
hm2_7i76e.0.7i76.0.0.output-00
hm2_7i76e.0.7i76.0.0.spindir
hm2_7i76e.0.7i76.0.0.spinena
hm2_7i76e.0.7i76.0.0.spinout

7i92
hm2_7i92.0.7i76.0.0.input-00
hm2_7i92.0.7i76.0.0.input-00-not
hm2_7i92.0.7i76.0.0.output-00
hm2_7i92.0.7i76.0.0.spindir
hm2_7i92.0.7i76.0.0.spinena
hm2_7i92.0.7i76.0.0.spinout

7i92t P1
hm2_7i92.0.7i76.0.2.input-00
hm2_7i92.0.7i76.0.2.input-00-not
hm2_7i92.0.7i76.0.2.output-00
hm2_7i92.0.7i76.0.2.spindir
hm2_7i92.0.7i76.0.2.spinena
hm2_7i92.0.7i76.0.2.spinout
hm2_7i92.0.7i77.0.3.input-00

7i92t P2
hm2_7i92.0.7i76.0.0.input-00
hm2_7i92.0.7i76.0.0.input-00-not
hm2_7i92.0.7i76.0.0.output-00
hm2_7i92.0.7i76.0.0.spindir
hm2_7i92.0.7i76.0.0.spinena
hm2_7i92.0.7i76.0.0.spinout
hm2_7i92.0.7i77.0.0.input-00

hm2_7i95.0.inmux.00.input-00
hm2_7i95.0.inmux.00.input-00-not
hm2_7i95.0.inmux.00.input-00-slow

hm2_7i96.0.gpio.000.in
hm2_7i96.0.gpio.000.in_not

hm2_7i96s.0.inm.00.input-01
hm2_7i96s.0.inm.00.input-01-not
hm2_7i96s.0.inm.00.input-00-slow
hm2_7i96s.0.ssr.00.out-00 - 03
hm2_7i96s.0.outm.00.out-04 - 05

hm2_7i96s.0.7i76.0.1.input-00
hm2_7i96s.0.7i76.0.1.input-00-not
hm2_7i96s.0.7i76.0.1.output-00

hm2_7i97.0.inmux.00.input-00
hm2_7i97.0.inmux.00.input-00-not
hm2_7i97.0.inmux.00.input-00-slow
'''

def build_io(parent):
	filePath = os.path.join(parent.configPath, 'io.hal')
	parent.info_pte.appendPlainText(f'Building {filePath}')
	contents = []
	contents = ['# This file was created with the Mesa Configuration Tool on ']
	contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n')

	# build inputs from qpushbutton menus, check for debounce c0_input_0
	hm2 = ''
	eStops = []
	contents.append('\n# Inputs\n')

	'''
	hm2_7i76e.0.gpio.000.in
	hm2_7i76e.0.gpio.000.in_not

	P2
	hm2_5i25.0.7i77.0.3.input-00
	hm2_5i25.0.7i77.0.3.input-00-not

	P3
	hm2_5i25.0.7i77.0.0.input-00
	hm2_5i25.0.7i77.0.0.input-00-not

	P1
	hm2_7i92.0.7i76.0.2.input-00
	hm2_7i92.0.7i76.0.2.input-00-not

	P2
	hm2_7i92.0.7i76.0.0.input-00
	hm2_7i92.0.7i76.0.0.input-00-not

	P1
	hm2_7i92.0.7i77.0.3.input-00
	hm2_7i92.0.7i77.0.3.input-00-not

	P2
	hm2_7i92.0.7i77.0.0.input-00
	hm2_7i92.0.7i77.0.0.input-00-not

	hm2_7i95.0.inmux.00.input-00
	hm2_7i95.0.inmux.00.input-00-not
	hm2_7i95.0.inmux.00.input-00-slow

	P1
	hm2_7i96s.0.7i76.0.1.input-00 through 31
	hm2_7i96s.0.7i76.0.1.input-00-not

	hm2_7i96s.0.7i76.0.1.output-00 through 15

	hm2_7i96s.0.7i77.0.0.input-00 through 31
	hm2_7i96s.0.7i77.0.0.input-00-not

	hm2_7i96s.0.7i77.0.0.output-00 through 15

	'''

	joint = 0
	ja_dict = {}
	for i in range(3):
		for j in range(6):
			axis = getattr(parent, f'c{i}_axis_{j}').currentData()
			if axis:
				ja_dict[axis.lower()] = joint
				joint += 1

	ports = {'7i76': 2, '7i77': 3}
	underscore_not = ['7i76E', '7i96']

	for i in range(3): # see if tab is visible
		# i == 0 main board, i == 1 daughter card P2, i == 2 daughter card P3 possibly
		if parent.mainTW.isTabVisible(i + 3):
			board = getattr(parent, f'c{i}_JointTW').tabText(0)
			if i == 1 and board in ports: # 7i92 P1 or 5/6i25 P2 so second port
				port = ports[board]
			else: # everything else is port 0
				port = 0

			if parent.hal_name == '7i96s': # check for daughter card
				if parent.daughterCB_0.currentData() == '7i76':
					port = 1
				elif parent.daughterCB_0.currentData() == '7i77':
					port = 0

			for j in range(32):
				key = getattr(parent, f'c{i}_input_{j}').text()
				if key != 'Select':
					if board in underscore_not:
						invert = '_not' if getattr(parent, f'c{i}_input_invert_{j}').isChecked() else ''
					else:
						invert = '-not' if getattr(parent, f'c{i}_input_invert_{j}').isChecked() else ''
					slow = '-slow' if getattr(parent, f'c{i}_input_debounce_{j}').isChecked() else ''

					if board == '7i76':
						hm2 =  f'hm2_{parent.hal_name}.0.7i76.0.{port}.input-{j:02}{invert}'
					if board == '7i77':
						hm2 =  f'hm2_{parent.hal_name}.0.7i77.0.{port}.input-{j:02}{invert}'
					if board == '7i76E':
						hm2 =  f'hm2_7i76e.0.gpio.{j:03}.in{invert}'
					if board == '7i95':
						hm2 =  f'hm2_7i95.0.inmux.00.input-{j:02}{invert}'
					if board == '7i95T':
						hm2 =  f'hm2_7i95.0.inmux.00.input-{j:02}{invert}'
					if board == '7i96':
						hm2 =  f'hm2_7i96.0.gpio.{j:03}.in{invert}'
					if board == '7i96S':
						hm2 = f'hm2_7i96s.0.inm.00.input-{j:02}{invert}'
					if board == '7i97':
						hm2 =  f'hm2_7i97.0.inmux.00.input-{j:02}{invert}'
					if board == '7i97T':
						hm2 =  f'hm2_7i97.0.inmux.00.input-{j:02}{invert}'

					if INPUTS.get(key, False): # return False if key is not in dictionary
						contents.append(f'{INPUTS[key]} {hm2}\n')
					else: # handle special cases
						if key == 'Home All':
							contents.append('\n# Home All Joints\n')
							contents.append('net home-all ' + f'{hm2}\n')
							for i in range(6):
								if getattr(parent, 'axisCB_' + str(i)).currentData():
									contents.append('net home-all ' + f'joint.{j}.home-sw-in\n')
						elif key[0:6] == 'E Stop':
							eStops.append(hm2)
						elif '+ Joint' in key: # Jog axis and joint enable
							axis = key.split()[1].lower()
							if axis in ja_dict:
								joint = ja_dict[axis]
								contents.append(f'net jog-{axis}-enable axis.{axis}.jog-enable <= {hm2}\n')
								contents.append(f'net jog-{axis}-enable joint.{joint}.jog-enable\n')

	#Build E-Stop Chain
	if len(eStops) > 0:
		contents.append('\n# E-Stop Chain\n')
		contents.append(f'loadrt estop_latch count={len(eStops)}\n')
		for i in range(len(eStops)):
			contents.append(f'addf estop-latch.{i} servo-thread\n')
		contents.append('\n# E-Stop Loop\n')
		contents.append('net estop-loopin iocontrol.0.user-enable-out => estop-latch.0.ok-in\n')
		for i in range(len(eStops) - 1):
			contents.append(f'net estop-{i}-out estop-latch.{i}.ok-out => estop-latch.{i+1}.ok-in\n')
		contents.append(f'net estop-loopout estop-latch.{len(eStops)-1}.ok-out => iocontrol.0.emc-enable-in\n')
		contents.append('\n# E-Stop Reset\n')
		contents.append(f'net estop-reset iocontrol.0.user-request-enable\n')
		for i in range(len(eStops)):
			contents.append(f'net estop-reset => estop-latch.{i}.reset\n')
			contents.append(f'net remote-estop{i} estop-latch.{i}.fault-in <= {eStops[i]}\n')

	'''
	hm2_7i96s.0.ssr.00.invert-00
	hm2_7i96s.0.ssr.00.invert-01
	hm2_7i96s.0.ssr.00.invert-02
	hm2_7i96s.0.ssr.00.invert-03
	hm2_7i96s.0.ssr.00.out-00
	hm2_7i96s.0.ssr.00.out-01
	hm2_7i96s.0.ssr.00.out-02
	hm2_7i96s.0.ssr.00.out-03
	hm2_7i96s.0.outm.00.out-04
	hm2_7i96s.0.outm.00.out-05
	hm2_7i96s.0.outm.00.invert-04
	hm2_7i96s.0.outm.00.invert-05

	7i95 and 7i95T
	hm2_7i95.0.ssr.00.out-00
	hm2_7i95.0.ssr.00.invert-00

	7i97 and 7i97T
	hm2_7i97.0.ssr.00.invert-00
	hm2_7i97.0.ssr.00.out-00
	'''

	# build outputs
	contents.append('\n# Outputs\n')
	for i in range(3): # see if tab is visible
		# i == 0 main board, i == 1 daughter card P2, i == 2 daughter card P3 possibly
		if parent.mainTW.isTabVisible(i + 3):
			board = getattr(parent, f'c{i}_JointTW').tabText(0)
			if i == 1 and board in ports: # 7i92 P1 or 5/6i25 P2 so second port
				port = ports[board]
			else: # everything else is port 0
				port = 0

			if parent.hal_name == '7i96s': # check for daughter card
				if parent.daughterCB_0.currentData() == '7i76':
					port = 1
				elif parent.daughterCB_0.currentData() == '7i77':
					port = 0

			for j in range(16):
				key = getattr(parent, f'c{i}_output_{j}').text()
				if key != 'Select':
					if board in underscore_not:
						invert = '_not' if getattr(parent, f'c{i}_output_invert_{j}').isChecked() else ''
					else:
						invert = '-not' if getattr(parent, f'c{i}_output_invert_{j}').isChecked() else ''

					if board == '7i76':
						hm2 =  f'hm2_{parent.hal_name}.0.7i76.0.{port}.output-{j:02}{invert}'
					elif board == '7i77':
						hm2 =  f'hm2_{parent.hal_name}.0.7i77.0.{port}.output-{j:02}{invert}'
					elif board == '7i76E':
						hm2 =  f'hm2_7i76e.0.gpio.{j + 31:03}.out{invert}'
					elif board == '7i95':
						hm2 =  f'hm2_7i95.0.ssr.00.out-{j:02}{invert}'
					elif board == '7i95T':
						hm2 =  f'hm2_7i95.0.ssr.00.out-{j:02}'
						if getattr(parent, f'c0_output_invert_{j}').isChecked():
							hm2 =  f'hm2_7i95.0.ssr.00.invert-{j:02}'
					elif board == '7i96':
						hm2 =  f'hm2_7i96.0.gpio.{j:03}.out{invert}'
					elif board == '7i96S':
						if j in range(4):
							hm2 =  f'hm2_7i96s.0.ssr.00.out-{j:02}\n'
							if getattr(parent, f'c0_output_invert_{j}').isChecked():
								hm2 =  f'setp hm2_7i96s.0.ssr.00.invert-{j:02} True\n'
						if j in range(4,6):
							hm2 =  f'hm2_7i96s.0.outm.00.out-{j:02}\n'
							if getattr(parent, f'c0_output_invert_{j}').isChecked():
								hm2 =  f'setp hm2_7i96s.0.outm.00.invert-{j:02} True\n'
					elif board == '7i97':
						hm2 =  f'hm2_7i97.0.inmux.00.input-{j:02}{invert}'
					elif board == '7i97T':
						if getattr(parent, f'c0_output_invert_{j}').isChecked():
							hm2 =  f'hm2_7i97.0.ssr.00.invert-{j:02}'
						else:
							hm2 =  f'hm2_7i97.0.ssr.00.out-{j:02}'
					if OUTPUTS.get(key, False): # return False if key is not in dictionary
						contents.append(f'{OUTPUTS[key]} {hm2}\n')

	try:
		with open(filePath, 'w') as f:
			f.writelines(contents)
	except OSError:
		parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')

def build_ss(parent):
	filePath = os.path.join(parent.configPath, 'sserial.hal')
	if os.path.exists(filePath):
		os.remove(filePath)
	if parent.ssCardCB.currentData():
		ssCard = parent.ssCardCB.currentText()
		if parent.boardCB.currentData() == '7i92t':
			mb = '7i92'
		elif  parent.boardCB.currentData() == '7i97t':
			mb = '7i97'
		else:
			mb = parent.boardCB.currentData()
		parent.info_pte.appendPlainText(f'Building {filePath}')
		contents = []
		contents = ['# This file was created with the Mesa Configuration Tool on ']
		contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
		contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n\n')

		if ssCard == '7i64':
			inputs = 24
			outputs = 24
		elif ssCard == '7i69':
			inputs = 24
			outputs = 24
		elif ssCard == '7i70':
			inputs = 48
			outputs = 0
		elif ssCard == '7i71':
			inputs = 0
			outputs = 48
		elif ssCard == '7i72':
			inputs = 0
			outputs = 48
		elif ssCard == '7i73':
			inputs = 0
			outputs = 0
		elif ssCard == '7i84':
			inputs = 32
			outputs = 16
		elif ssCard == '7i87':
			inputs = 8
			outputs = 0
		else:
			inputs = 0
			outputs = 0

		motherBoards = ['5i25', '7i80db', '7i80hd', '7i92', '7i93', '7i98']
		daughterBoards =['7i76', '7i77', '7i78']

		combiBoards = ['7i76e', '7i95', '7i96', '7i96s', '7i97']
		if ssCard != '7i73' and mb in combiBoards:
			for i in range(inputs):
				if getattr(parent, f'ss{ssCard}in_' + str(i)).text() != 'Select':
					key = getattr(parent, f'ss{ssCard}in_' + str(i)).text()
					contents.append(f'net {ssCard}-in-{i} {INPUTS[key]} hm2_{mb}.0.{ssCard}.0.0.input-{i:02}\n')
			for i in range(outputs):
				if getattr(parent, f'ss{ssCard}out_' + str(i)).text() != 'Select':
					key = getattr(parent, f'ss{ssCard}out_' + str(i)).text()
					if OUTPUTS.get(key, False): # return False if key is not in dictionary
						contents.append(f'{OUTPUTS[key]} hm2_{mb}.0.{ssCard}.0.0.output-{i:02}\n')

		elif ssCard == '7i73':
			for i in range(8):
				if getattr(parent, 'ss7i73key_' + str(i)).text() != 'Select':
					key = getattr(parent, 'ss7i73key_' + str(i)).text()
					contents.append(f'net ss7i73key_{i} {OUTPUTS[key]} hm2_{mb}.0.7i73.0.0.input-{i:02}\n')
			for i in range(8, 16):
				if getattr(parent, 'ss7i73key_' + str(i)).text() != 'Select':
					key = getattr(parent, 'ss7i73key_' + str(i)).text()
					contents.append(f'net ss7i73key_{i} {INPUTS[key]} hm2_{mb}.0.7i73.0.0.input-{i:02}\n')
			for i in range(12):
				if getattr(parent, 'ss7i73lcd_' + str(i)).text() != 'Select':
					key = getattr(parent, 'ss7i73lcd_' + str(i)).text()
					contents.append(f'net ss7i73lcd_{i} {OUTPUTS[key]} hm2_{mb}.0.7i73.0.0.output-{i:02}\n')
			for i in range(16):
				if getattr(parent, 'ss7i73in_' + str(i)).text() != 'Select':
					key = getattr(parent, 'ss7i73in_' + str(i)).text()
					contents.append(f'net ss7i73in_{i} {INPUTS[key]} hm2_{mb}.0.7i73.0.0.input-{i:02}\n')
			for i in range(2):
				if getattr(parent, 'ss7i73out_' + str(i)).text() != 'Select':
					key = getattr(parent, 'ss7i73out_' + str(i)).text()
					contents.append(f'net ss7i73out_{i} {OUTPUTS[key]} hm2_{mb}.0.7i84.0.0.output-{i:02}\n')

		try:
			with open(filePath, 'w') as f:
				f.writelines(contents)
		except OSError:
			parent.info_pte.appendPlainText(f'OS error\n {traceback.print_exc()}')
