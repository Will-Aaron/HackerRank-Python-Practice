def merge_the_tools(string, k):
    no_doubles = []
    div = len(string) // k
    for i in range(div):
        subsegment = string[i*k:(i+1)*k]
        used_char = []
        segment_no_d = ''
        for char in subsegment:
            if char not in used_char:
                used_char.append(char)
                segment_no_d += char
        no_doubles.append(segment_no_d)
    for j in range(len(no_doubles)):
        print(no_doubles[j])
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
