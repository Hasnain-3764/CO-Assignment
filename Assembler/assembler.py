register={"zero":0,"ra":0,"sp":0,"gp":0,"sp":0,"t0":0,"t1":0,"t2":0,"s0":0,"s1":0,"s2":0,"s3":0,"s4":0,"s5":0,"s6":0,"s7":0,"s8":0,"s9":0,"s10":0,"s11":0,"t3":0,"t4":0,"t5":0,"t6":0,"a0":0,"a1":0,"a2":0,"a3":0,"a4":0,"a5":0,"a6":0,"a7":0}
register_address={"zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100","t0":"00101","t1":"00110","t2":"00111","s0":"01000","s1":"01001","a0":"01010","a1":"01011","a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000","a7":"10001","s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111","s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100","t4":"11101","t5":"11110","t6":"11111"}
def binary_conversion_uptofive(s):
    count=5
    remainderx=0
    while count>0:
        remainder=s%2
        s=s//2
        remainderx+=remainder*(2**(5-count))
        count-=1
    return remainderx
def binarycoverter(num):
    num1=int(num)
    count=12
    remainderx=0
    while(count>0):
        remainder=num1%2
        num1=num1//2
        remainderx+=remainder*(10**(12-count))
        count-=1
    while len(str(remainderx))<12:
        remainderx="0"+str(remainderx)
    return str(remainderx)
def binarycoverter_long(num):
    num1=int(num)
    count=32
    remainderx=0
    while(count>0):
        remainder=num1%2
        num1=num1//2
        remainderx+=remainder*(10**(32-count))
        count-=1
    while len(str(remainderx))<32:
        remainderx="0"+str(remainderx)
    return str(remainderx)
def binaryconverter_tewbits(num):
    num1=int(num)
    count=20
    remainderx=0
    while(count>0):
        remainder=num1%2
        num1=num1//2
        remainderx+=remainder*(10**(20-count))
        count-=1
    while len(str(remainderx))<20:
        remainderx="0"+str(remainderx)
    return str(remainderx)

def R_type_instruction(instruction,s,reg,register_address):
    lst_reg=list(instruction[1].split(","))
    if instruction[0]=="add":
        reg[lst_reg[0]]=reg[lst_reg[1]]+reg[lst_reg[2]]
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"000"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    elif instruction[0]=="sub":
        reg[lst_reg[0]]=reg[lst_reg[1]]-reg[lst_reg[2]]
        s+="0000010"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"000"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    elif instruction[0]=="slt":
        if reg[lst_reg[1]]<reg[lst_reg[2]]:
            reg[lst_reg[0]]=1
        else:
            reg[lst_reg[0]]=0
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"010"+register_address[lst_reg[0]]
        s+="0110011"
    elif instruction[0]=="sltu":
        if reg[lst_reg[1]]<reg[lst_reg[2]] and reg[lst_reg[1]]>=0 and reg[lst_reg[2]]>=0:
            reg[lst_reg[0]]=1
            s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"110"+register_address[lst_reg[0]]
            s+="0110011"
        elif reg[lst_reg[1]]>=reg[lst_reg[2]] and reg[lst_reg[1]]>=0 and reg[lst_reg[2]]>=0:
            reg[lst_reg[0]]=0
            s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"110"+register_address[lst_reg[0]]
            s+="0110011"
        else:
            reg[lst_reg]=0
            print("ERROR --> not a unsigned number")
    elif instruction[0]=="xor":
        reg[lst_reg[0]]=reg[lst_reg[1]]^reg[lst_reg[2]]
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"001"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    elif instruction[0]=="sll":
        reg[lst_reg[0]]=reg[lst_reg[1]]<<(binary_conversion_uptofive(reg[lst_reg[2]]))
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"100"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    elif instruction[0]=="srl":
        reg[lst_reg[0]]=reg[lst_reg[1]]>>(binary_conversion_uptofive(reg[lst_reg[2]]))
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"101"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    elif instruction[0]=="or":
        reg[lst_reg[0]]=reg[lst_reg[1]]|reg[lst_reg[2]]
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"011"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    elif instruction[0]=="and":
        reg[lst_reg[0]]=reg[lst_reg[1]]&reg[lst_reg[2]]
        s+="0000000"+register_address[lst_reg[2]]+register_address[lst_reg[1]]+"111"+register_address[lst_reg[0]]
        s+="0110011"
        return s
    return s
def I_type_instruction(instruction,s,register_address):
    lst_reg=list(instruction[1].split(','))
    if instruction[0]=="addi":
        s+=str(binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"000"+register_address[lst_reg[0]]+"0010011"
        return s
    elif instruction[0]=="lw":
        lst_reg1=list(lst_reg[1][:(len(lst_reg[1])-2)].split('('))
        s+=str(binarycoverter(lst_reg1[0]))+register_address(lst_reg1[1])+"010"+register_address(lst_reg[0])+"0000011"
        return s
    elif instruction[0]=="sltiu":
        s+=str(binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"011"+register_address[lst_reg[0]]+"0010011"
        return s
    elif instruction[0]=="jalr":
        s+=str(binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"000"+register_address[lst_reg[0]]+"1100111"
        return s
def S_type_instruction(instruction,s,register_address):
    lst_reg=list(instruction[1].split(','))
    if instruction[0]=="sw":
        lst_reg1=list(lst_reg[1][:(len(lst_reg[1])-2)].split('('))
        s+=str(lst_reg1[0])[:(len(binarycoverter(lst_reg1[0]))-5)]+register_address[lst_reg[0]]+register_address[lst_reg1[1]]+"010"+str(lst_reg1[0])[(len(binarycoverter(lst_reg1[0]))-5):]+"0100011"
        return s
    return s
def B_type_instruction(instruction,s,register_address):
    lst_reg=list(instruction[1].split(','))
    b_type_opcode={"beq":"000","bne":"001","blt":"100","bge":"101","bltu":"110","bgeu":"111"}
    s+=str(binarycoverter(lst_reg[2])[:7])+register_address[lst_reg[1]]+register_address[lst_reg[0]]+b_type_opcode[instruction[0]]+str(binarycoverter(lst_reg)[7:])+"1100011"
    return s
def U_type_instruction(instruction,s,register_address):
    lst_reg=list(instruction[1].split(','))
    U_type_opcode={"auipc":"0010111","lui":"0110111"}
    s+=binarycoverter_long(str(lst_reg[1]))[:21]+register_address[lst_reg[0]]+U_type_opcode[instruction[0]]
    return s
def J_type_instruction(instruction,s,register_address):
    lst_reg=list(instruction[1].split(','))
    j_type_opcode={"jal":"1101111"}
    num=binaryconverter_tewbits(str(lst_reg[1]))
    s+=num[0]+num[10:]+num[11]+num[1:9]
    s+=register_address[lst_reg[0]]+j_type_opcode[instruction[0]]
s=list(input('').split(' '))
s2=""
s1=R_type_instruction(s,s2,register,register_address)

input_file=sys.argv[1]
output_file=sys.argv[2]
with open(input_file,"r") as f:
    with open(output_file,"w") as q:
        for line in f:
            if line.strip():
                q.write(line)




