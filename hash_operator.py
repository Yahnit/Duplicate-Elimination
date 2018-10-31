from itertools import islice
from itertools import zip_longest
import time
class Hash_operator:
    def __init__(self,B):
        self.output_buffer = []
        self.output_file = 'output.txt'
        self.B = B
        self.hash_map = {}
        self.time = 0
    
    def hash( self, d, str ):
        if d == 0: 
            d = 0x01000193
        # Use the FNV algorithm from http://isthe.com/chongo/tech/comp/fnv/ 
        for c in str:
            d = ( (d * 0x01000193) ^ ord(c) ) & 0xffffffff;
        return d

    def write_in_chunks(self, file_object, piece):
        for line in piece:
            file_object.write("%s\n" %(line))

    def grouper(self,iterable, n, fillvalue=None):
        args = [iter(iterable)] * n
        return zip_longest(*args, fillvalue=fillvalue)


    def hash_open(self,R,n,M):
        f = open(R,'r',M)
        o = open(self.output_file, "w+")
        print('Open called')
        input_iterator = iter(f)
        start_time = time.time()
        while True:
            #for piece in self.grouper(f, (M-1)*B, ""): #for every chunk_sized chunk
            #process lines like lines[0], lines[1] , ... , lines[chunk_size-1]"""
                piece = list(islice(input_iterator, self.B))
                #print('(M-1)*B lines read :',piece)
                if not piece:
                    if self.output_buffer != []:
                        self.write_in_chunks(o,self.output_buffer)
                    self.close(f,o)
                    break
                output_chunk = self.Getnext(piece,n,f,o)
                if output_chunk is None:
                    continue
                self.write_in_chunks(o,output_chunk)
                self.output_buffer = []
        self.time = time.time()-start_time

    def Getnext(self, piece, n, f, o):
        #print('GetNext')
        for line in piece:
            line = line.strip()
            hash_value=self.hash(2,line)
            if hash_value not in self.hash_map:
                self.hash_map[hash_value] = 1
                if len(self.output_buffer)>=self.B:
                    return self.output_buffer
                self.output_buffer.append(line)
        return None


    def close(self,ip_file_object,op_file_object):
        print('Closing files now')
        ip_file_object.close()
        op_file_object.close()

    def main(self, R, n, M):
        self.hash_open(R,n,M)

    



        