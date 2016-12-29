# coding=utf-8
import sys
import time

class Tail():
    def __init__(self, file_name, callback=sys.stdout.write):
        self.file_name = sys.argv[1]
        self.callback = callback
    def follow(self, n=10):
        if  len(sys.argv) == 3 and int(sys.argv[2]) > 0:
            n = int(sys.argv[2])
        try:
            while True:
                with open(self.file_name) as self._file:
                    self._file.seek(0, 2)
                    self.file_length = self._file.tell()
                    BLOCK_SIZE = 1024
                    totail_line_wanted = n
                    newline_character_num = n+1
                    block_number = -1
                    blocks = []
                    block_end_byte = self.file_length
                    #print self.file_length
                    while (newline_character_num > 0) and (block_end_byte > 0):
                        if (block_end_byte - BLOCK_SIZE > 0):
                            self._file.seek(block_number * BLOCK_SIZE, 2)
                            blocks.append(self._file.read(BLOCK_SIZE))
                        else:
                            self._file.seek(0, 0)
                            blocks.append(self._file.read(block_end_byte))
                        lines_found = blocks[-1].count('\n')
                        newline_character_num -= lines_found
                        block_end_byte -= BLOCK_SIZE
                        block_number -= 1
                    all_read_text = ''.join(reversed(blocks))
                    self.callback( '\n'.join(all_read_text.splitlines()[-totail_line_wanted:])) 
                    print '\n'
                    time.sleep(1)
        except Exception, e:
            print "Error"
            print e

if __name__ == '__main__':
    py_tail = Tail('est.txt')
    py_tail.follow()
