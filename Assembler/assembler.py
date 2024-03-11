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
def I_type_binarycoverter(num):
    num1=int(num)
    count=12
    remainderx=0
    while(count>0):
        remainder=num1%2
        num1=num1//2
        remainderx+=remainder*(10**(12-count))
        count-=1
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
def I_type_instruction(instruction,s,reg,register_address):
    lst_reg=list(instruction[1].split(','))
    if instruction[0]=="addi":
        s+=str(I_type_binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"000"+register_address[lst_reg[0]]+"0010011"
        return s
    elif instruction[0]=="lw":
        s+=str(I_type_binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"010"+register_address[lst_reg[0]]+"0000011"
        return s
    elif instruction[0]=="sltiu":
        s+=str(I_type_binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"011"+register_address[lst_reg[0]]+"0010011"
        return s
    elif instruction[0]=="jalr":
        s+=str(I_type_binarycoverter(lst_reg[2]))+register_address[lst_reg[1]]+"000"+register_address[lst_reg[0]]+"1100111"
