# -*- coding: UTF-8 -*-

import struct


global table_file, count

count = 0
table_file = open("gbk_to_utf8.c", "w+")
table_file.write("static const unsigned short gbkUcs2Tab[][2]={\n")

for i in range(65536):
    hi_byte = i >> 8
    lo_byte = i & 0xff
    hz = struct.pack('<BB', hi_byte, lo_byte)
    try:
        hz = hz.decode(encoding='gb2312')   # 按GB2312解码
        if len(hz) == 1:
            code_gb2312 = hz.encode(encoding='gb2312')
            gb_val = code_gb2312[0] * 256 + code_gb2312[1]
            str = '\t{' + hex(gb_val) + ', ' + hex(ord(hz)) + '}, //' + hz + '\n'
            print(str, end='')
            table_file.write(str)
            count+=1
    except UnicodeError as unierr:
        pass

print('valid num %d' % count)
table_file.write("};\n")
table_file.close()