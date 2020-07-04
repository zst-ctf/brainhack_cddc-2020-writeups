# Secret Code
Gate 4

## Challenge 

What is the SECRET CODE?

MD5("SecretCode"): 8c42eab77b666be3be6a9544146bf703

## Solution

Decompile in Ghidra, we see some integers.


	void check(uint param_1)
	{
	  local_20 = *(int *)(in_GS_OFFSET + 0x14);
	  local_37 = 0x43444443;
	  local_33 = 0x457b3032;
	  local_2f = 0x567a7135;
	  local_2b = 0x7a347036;
	  local_27 = 0x6b653b5a;
	  local_23 = 0x7d73;
	  local_21 = 0;
	  if ((param_1 + 0x33e0f923 ^ 0x23eec421 | (uint)(0xcc1f06dc < param_1) - 1) == 0) {
	    local_41 = 0;
	    while (local_41 < 0xe) {
	      *(byte *)((int)&local_33 + (uint)local_41 + 3) =
	           local_41 ^ *(byte *)((int)&local_33 + (uint)local_41 + 3);
           // local_33[local_41 + 3] =
	           local_41 ^ local_33[local_41 + 3];
	      local_41 = local_41 + 1;
	    }
	    puts((char *)&local_37);
	  }
	  if (local_20 != *(int *)(in_GS_OFFSET + 0x14)) {
	    __stack_chk_fail_local();
	  }
	  return;
	}


Basically it has some text which then goes through an XOR cipher

Extract out the text

	>>> a = [0x43444443, 0x457b3032, 0x567a7135, 0x7a347036, 0x6b653b5a, 0x7d73]

	>>> import struct

	>>> list(map(lambda x: struct.pack('<I', x), a))
	[b'CDDC', b'20{E', b'5qzV', b'6p4z', b'Z;ek', b's}\x00\x00']

	>>> b''.join(b)
	b'CDDC20{E5qzV6p4zZ;eks}\x00\x00'


Undo the XOR cipher

	flag = list(b'20{E5qzV6p4zZ;eks}')
	for i in reversed(range(0xe)):
		flag[i+3] ^= i

	print(flag)
	print("CDDC" + ''.join(map(chr, flag)))

## Flag

	CDDC20{E4syR3v3rS1ng~}
