with open("test.txt") as f:
    f.seek(0,2)
    #print f.tell()
    lines =10
    BLOCK_SIZE =1024
    totail_line_wanted =lines
    lines_to_go = totail_line_wanted
    block_number = -1
    blocks = []
    block_end_byte = f.tell()
    while lines_to_go  >0 and block_end_byte > 0:
        if (block_number - BLOCK_SIZE > 0):
            f.seek(block_number * BLOCK_SIZE, 2)
            blocks.append(f.read(BLOCK_SIZE))
        else:
            f.seek(0,0)
            blocks.append(f.read(block_end_byte))
        lines_found = blocks[-1].count('\n')
        lines_to_go -= lines_found
        block_end_byte -= BLOCK_SIZE
        block_number -=1 
    all_read_text =''.join(reversed(blocks))
    print  '\n'.join(all_read_text.splitlines()[-totail_line_wanted:])
