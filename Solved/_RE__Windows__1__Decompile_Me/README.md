# [RE (Windows)-1] Decompile Me
RE

## Challenge 
DESCRIPTION
Hello py2exe, nice to meet you!

MD5("DecompileMe.zip"): 3805ccecd327d3cfcfdcc12c1ce7891b

ATTACHED FILES
DecompileMe.zip

## Solution

Decompile exe to pyc, then pyc to py
	
	pip install unpy2exe
	unpy2exe DecompileMe.exe

	pip install uncompyle6
	uncompyle6 DecompileMe.py.pyc > out.py


		# uncompyle6 version 3.7.2
		# Python bytecode 2.7 (62211)
		# Decompiled from: Python 2.7.16 (default, Oct 10 2019, 22:02:15) 
		# [GCC 8.3.0]
		# Embedded file name: DecompileMe.py
		# Compiled at: 2020-07-03 13:02:16
		import ctypes
		FLAG = 'CDDC20'
		FLAG += '{'
		FLAG += 'N'
		FLAG += 'i'
		FLAG += 'C'
		FLAG += 'e'
		FLAG += '-'
		FLAG += '2'
		FLAG += '-'
		FLAG += 'M'
		FLAG += 'e'
		FLAG += 'e'
		FLAG += 'T'
		FLAG += '-'
		FLAG += 'p'
		FLAG += 'y'
		FLAG += '2'
		FLAG += 'e'
		FLAG += 'x'
		FLAG += 'e'
		FLAG += '~'
		FLAG += ':'
		FLAG += 'D'
		FLAG += '}'
		ctypes.windll.user32.MessageBoxA(0, 'Hello py2exe!', 'DecompileMe', 0)


## Flag

	CDDC20{NiCe-2-MeeT-py2exe~:D}