from collections import Counter
import heapq
def huffman_encode(s):
    h=[(freq,ch)for ch,freq in Counter(s).items()]
    headpq.heapify(h)
    while len(h)>1:
        freq1,ch1 = heapq.heappop(h)
        freq2,ch2 = heapq.heappop(h)
        heapq.heappush((freq1+freq2,ch1+ch2))
    code = {}
    
    return code








def main():
    s = input()
    code = huffman_encode(s)
    encoded = ''.join(code[ch] for ch in s)
    print(len(code),len(encoded))
    for ch in sorted(code):
        print('{}:{}'.format(ch,code[ch]))
    print(encoded)

if __name__ =='__main__':
    main()

