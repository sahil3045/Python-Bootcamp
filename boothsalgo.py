
def decbin(num:int):
    rems = []
    while num:
        rems.append(str(num%2))
        num//=2
    return ''.join(reversed(rems))

def set_zeros(num:str):
    return '0'*(6-len(num)) + num

def to_str(num: int):
    return set_zeros(decbin(num)[-6:])
    
def add_binary(n1:str, n2:str):
    carry = 0
    s = list('000000')
    for i in range(5, -1, -1):
        temp = int(n1[i]) + int(n2[i]) + carry
        if temp == 3:
            s[i] = '1'
            carry = 1
        elif temp == 2:
            s[i] = '0'
            carry = 1
        else:
            s[i] = str(temp)
            carry = 0
    
    return ''.join(s)
q_1 = '0'

M = set_zeros(to_str(int(input("Enter Multiplicand: ")))) # remove the 0b from start
Q = set_zeros(to_str(int(input("Enter Multiplier: "))))

m_comp = to_str(int(''.join(('0' if x=='1' else '1' for x in M)), 2)+1)
if len(m_comp)>=6:
    m_comp=m_comp[:6]
else:
    m_comp = set_zeros(m_comp)

A = '000000'

print('A', 'Q', 'Q-1', 'M', 'STEP', sep="\t")
print(A, Q, q_1, M, 'Initial Values', sep="\t")

for step in range(6):
    print('\nCycle', step+1)
    if Q[-1]+q_1 == '10': #A = A-M
        A = add_binary(A, m_comp)
        print(A, Q, q_1, M, 'A <- A-M', sep="\t")
    elif Q[-1]+q_1 == '01': #A = A+M
        A = add_binary(A, M)
        print(A, Q, q_1, M, 'A <- A+M', sep="\t")
        
    # right shift
    q_1 = Q[-1]
    temp = A[0]+A+Q[:-1]
    A, Q = temp[:6], temp[6:]
    print(A, Q, q_1, M, 'Right Shift', sep="\t")
    
print("\nAnswer:", int(A+Q, 2))