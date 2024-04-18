import sys
import os
register_address={
    "zero":"00000","ra":"00001","sp":"00010","gp":"00011","tp":"00100","t0":"00101",
    "t1":"00110","t2":"00111","s0":"01000","s1":"01001","a0":"01010","a1":"01011",
    "a2":"01100","a3":"01101","a4":"01110","a5":"01111","a6":"10000","a7":"10001",
    "s2":"10010","s3":"10011","s4":"10100","s5":"10101","s6":"10110","s7":"10111",
    "s8":"11000","s9":"11001","s10":"11010","s11":"11011","t3":"11100","t4":"11101",
    "t5":"11110","t6":"11111"
}
register_values={
    "zero":0,"ra":0,"sp":256,"gp":0,"tp":0,"t0":0,
    "t1":0,"t2":0,"s0":0,"s1":0,"a0":0,"a1":0,
    "a2":0,"a3":0,"a4":0,"a5":0,"a6":0,"a7":0,
    "s2":0,"s3":0,"s4":0,"s5":0,"s6":0,"s7":0,
    "s8":0,"s9":0,"s10":0,"s11":0,"t3":0,"t4":0,
    "t5":0,"t6":0
}
registers={
  "00000": "zero",
  "00001": "ra",
  "00010": "sp",
  "00011": "gp",
  "00100": "tp",
  "00101": "t0",
  "00110": "t1",
  "00111": "t2",
  "01000": "s0",
  "01001": "s1",
  "01010": "a0",
  "01011": "a1",
  "01100": "a2",
  "01101": "a3",
  "01110": "a4",
  "01111": "a5",
  "10000": "a6",
  "10001": "a7",
  "10010": "s2",
  "10011": "s3",
  "10100": "s4",
  "10101": "s5",
  "10110": "s6",
  "10111": "s7",
  "11000": "s8",
  "11001": "s9",
  "11010": "s10",
  "11011": "s11",
  "11100": "t3",
  "11101": "t4",
  "11110": "t5",
  "11111": "t6"
}
dic_type_of_ins = {

    "R" : ["add","sub","sll","slt","sltu","xor","srl","or","and"],
    "I" : ['addi',"sltiu",'lw','jalr'],
    "B" : ["beq","bne","blt","bge","bltu","bgeu"],
    "J" : ["jal"],
    "U" : ["lui","auipc"],
    "S" : ["sw"]
}
program_counter=0
count=0
immediate={ }
memory=[]
labels={"start":"0","end":"1"}
R_TYPE = {
  "000": ["add","sub"],
  "001": "sll",
  "010": "slt",
  "011": "sltu",
  "100": "xor",
  "101": "srl",
  "110": "or",
  "111": "and"
}
I_TYPE={
    "0000011": "lw",
    "0010011": {"000":"addi","011":"sltiu"},
    "1100111":"jalr"
}
B_TYPE={
    '000': 'beq',
    '001': 'bne',
    '100': 'blt',
    '101': 'bge',
    '110': 'bltu', 
    '111': 'bgeu'
}

U_TYPE = {
    "0010111": "auipc",
    "0110111": "lui"
}

J_TYPE={
    "1101111":"jal"
}
S_TYPE={
    "0100011":"sw"
}
dic_type_for_opcode = {

    "R" : R_TYPE,
    "I" : I_TYPE,
    "B" : B_TYPE,
    "J" : J_TYPE,
    "U" : U_TYPE,
    "S" : S_TYPE
}
data_memory = {"0x00010000":0,
               "0x00010004":0,
               "0x00010008":0,
               "0x0001000c":0,
               "0x00010010":0,
               "0x00010014":0,
               "0x00010018":0,
               "0x0001001c":0,
               "0x00010020":0,
               "0x00010024":0,
               "0x00010028":0,
               "0x0001002c":0,
               "0x00010030":0,
               "0x00010034":0,
               "0x00010038":0,
               "0x0001003c":0,
               "0x00010040":0,
               "0x00010044":0,
               "0x00010048":0,
               "0x0001004c":0,
               "0x00010050":0,
               "0x00010054":0,
               "0x00010058":0,
               "0x0001005c":0,
               "0x00010060":0,
               "0x00010064":0,
               "0x00010068":0,
               "0x0001006c":0,
               "0x00010070":0,
               "0x00010074":0,
               "0x00010078":0,
               "0x0001007c":0,
}


def branching(count,memory,program_counter):
    global register_values
    global data_memory
    global dic_type_for_opcode
    global registers
    q=int(count)
    if count==len(memory):
        output_file.write(print_data(data_memory))
        return 
    while(q<len(memory)):
        inst=memory[q]
        register_values,data_memory=func_Calling(inst,register_values,registers,dic_type_for_opcode,data_memory)
        output_file.write(print_register(register_values,program_counter))
        q+=1
    return 
def convert_to_binary(number):
    binary_str = bin(number)[2:]
    binary_32_bit = binary_str.zfill(32)
    return binary_32_bit

def print_register(values1,program_counter):
    reg123=""
    reg123+="0b"+convert_to_binary(program_counter)
    for val in values1.values():
        reg123+=" "+"0b"+convert_to_binary(val)
    return reg123

def print_data(data_memory):
    reg234=""
    for i,j in zip(data_memory.keys(),data_memory.values()):
        reg234=i+":"+bin(j)+"\n"
    return reg234

def todecimal(x, bits):
    assert len(x) <= bits
    n = int(x, 2)
    s = 1 << (bits - 1)
    return (n & s - 1) - (n & s)

def perform_addition(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    values[registers[dest_reg]] = values[registers[source_reg1]] + values[registers[source_reg2]]
    

def perform_subtraction(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    values[registers[dest_reg]] = values[registers[source_reg1]] - values[registers[source_reg2]]
    

def perform_signed_comparison(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    if values[registers[source_reg1]] > values[registers[source_reg2]]:
        values[registers[dest_reg]] = 1
    else:
        values[registers[dest_reg]] = 0
    return values

def perform_unsigned_comparison(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    reg1=values[registers[source_reg1]] + (1 << 13)
    reg2=values[registers[source_reg2]] + (1 << 13)
    if reg1 > reg2:
        values[registers[dest_reg]] = 1
    else:
        values[registers[dest_reg]] = 0
    

def perform_exclusive_or(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    values[registers[dest_reg]] = values[registers[source_reg1]] ^ values[registers[source_reg2]]
    

def perform_left_shift(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg = bin_code[7:12]
    length = len(bin(values[registers[source_reg]]))
    binary=str(bin(values[registers[source_reg]]))
    binarys=binary[2:]
    shift_amount = int(str(binarys)[length-5:], 2)
    values[registers[dest_reg]] = shift_amount >> values[registers[bin_code[12:17]]]
    return values

def perform_right_shift(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg = bin_code[7:12]
    length = len(bin(values[registers[source_reg]]))
    binary=str(bin(values[registers[source_reg]]))
    binarys=binary[2:]
    shift_amount = int(str(binarys)[length-5:], 2)
    values[registers[dest_reg]] = shift_amount << values[registers[bin_code[12:17]]]
    

def perform_or_operation(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    values[registers[dest_reg]] = values[registers[source_reg1]] | values[registers[source_reg2]]
    

def perform_and_operation(bin_code, values, registers):
    dest_reg = bin_code[20:25]
    source_reg1 = bin_code[7:12]
    source_reg2 = bin_code[12:17]
    values[registers[dest_reg]] = values[registers[source_reg1]] & values[registers[source_reg2]]
    


def execute_r_type_instruction(bin_code, values, registers, r_type_reg,data_memory):
    global count
    global program_counter
    func3 = bin_code[17:20]
    function = r_type_reg[func3]
    forward = bin_code[:2]

    if function is ["add", "sub"]:
        if forward == "00":
            values = perform_addition(bin_code, values, registers)
        else:
            values = perform_subtraction(bin_code, values, registers)
    elif function == "slt":
        values = perform_signed_comparison(bin_code, values, registers)
    elif function == "sltu":
        values = perform_unsigned_comparison(bin_code, values, registers)
    elif function == "xor":
        values = perform_exclusive_or(bin_code, values, registers)
    elif function == "sll":
        values = perform_left_shift(bin_code, values, registers)
    elif function == "srl":
        values = perform_right_shift(bin_code, values, registers)
    elif function == "or":
        values = perform_or_operation(bin_code, values, registers)
    elif function == "and":
        values = perform_and_operation(bin_code, values, registers)
    count+=1
    program_counter+=4
    return values,data_memory

def execute_s_type_instruction(bin_code, values, register, data_memory):
    global program_counter
    global count
    imme = bin_code[0:7] + bin_code[20:25]
    reg_dest = bin_code[7:12]
    reg_src = bin_code[12:17]
    address = "0x000" + str(hex(todecimal(imme,12) + values[register[reg_src]]))[2:]
    data_memory[address] = values[register[reg_dest]]
    count+=1
    program_counter += 4
    return values,data_memory

def perform_addition_imm(bin_code, values, register):
    source_reg = register[bin_code[20:25]]
    dest_reg = register[bin_code[12:17]]
    imme = bin_code[:12]
    values[dest_reg] = values[source_reg] + todecimal(imme, 12)
    

def perform_lessthanimme(bin_code, values, register):
    source_reg = register[bin_code[20:25]]
    dest_reg = register[bin_code[12:17]]
    reg1=values[registers[source_reg]] + (1 << 13)
    imme = bin_code[:12]
    if reg1 < int(imme, 2):
        values[dest_reg] = 1
    

def perform_workingReg(bin_code, values, register, data_memory):
    source_reg = register[bin_code[20:25]]
    dest_reg = register[bin_code[12:17]]
    imme = bin_code[:12]
    address = "0x000" + str(hex(todecimal(imme, 12) + values[source_reg]))[2:]
    data_memory[address]=values[dest_reg] 
    return values,data_memory

def jump_linkregister(bin_code, values, register):
    global count
    global program_counter
    source_reg = register[bin_code[20:25]]
    dest_reg = register[bin_code[12:17]]
    imme = bin_code[:12]
    values[dest_reg] = program_counter + 4
    program_counter = bin(values[source_reg] + todecimal(imme, 12))
    program_counter[len(program_counter)-1]=0
    program_counter=todecimal(program_counter)
    count=(program_counter/4) 
    branching(count,memory,program_counter)
    

def execute_i_type_instruction(bin_code, values, register, i_type_reg,data_memory):
    global inst
    global count
    global program_counter
    opcode = bin_code[25:]
    func = i_type_reg[opcode]
    func3 = opcode[17:20]
    if func in ["000","011"]:
        if func3 == "000":
            values = perform_addition_imm(bin_code, values, register)
        else:
            values = perform_lessthanimme(bin_code, values, register)
    elif func == "lw":
        values,data_memory = perform_workingReg(bin_code, values, register,data_memory)
    elif func == "jalr":
        values= jump_linkregister(bin_code, values, register)
    program_counter+=4
    count+=1
    return values,data_memory


def branch_if_equal(bin_code, values, register):
    global program_counter
    global count
    source_reg1 = register[bin_code[7:12]]
    source_reg2 = register[bin_code[12:17]]
    imme = bin_code[0] + bin_code[24] + bin_code[1:7] + bin_code[20:24] + "0"
    if values[source_reg1] == values[source_reg2]:
        program_counter += todecimal(imme, 13)
        count = (program_counter/4)
        branching(count,memory,program_counter)
    

def branch_if_not_equal(bin_code, values, register):
    global program_counter
    global count
    source_reg1 = register[bin_code[7:12]]
    source_reg2 = register[bin_code[12:17]]
    imme = bin_code[0] + bin_code[24] + bin_code[1:7] + bin_code[20:24] + "0"
    if values[source_reg1] != values[source_reg2]:
        program_counter += todecimal(imme, 13)
        count = (program_counter/4)
        branching(count,memory,program_counter)
    

def branch_if_greater_equal(bin_code, values, register):
    global program_counter
    global count
    source_reg1 = register[bin_code[7:12]]
    source_reg2 = register[bin_code[12:17]]
    imme = bin_code[0] + bin_code[24] + bin_code[1:7] + bin_code[20:24] + "0"
    if values[source_reg1] >= values[source_reg2]:
        program_counter += todecimal(imme, 13)
        count = (program_counter/4)
        branching(count,memory,program_counter)
    

def branch_if_greater_unsigned_equal(bin_code, values, register):
    global program_counter
    global count
    source_reg1 = register[bin_code[7:12]]
    source_reg2 = register[bin_code[12:17]]
    imme = bin_code[0] + bin_code[24] + bin_code[1:7] + bin_code[20:24] + "0"
    reg1 = values[source_reg1] + (1 << 13)
    reg2 = values[source_reg2] + (1 << 13)
    if reg1 >= reg2:
        program_counter += todecimal(imme, 13)
        count = (program_counter/4)
        branching(count,memory,program_counter)
    

def branch_if_less(bin_code, values, register):
    global program_counter
    global count
    source_reg1 = register[bin_code[7:12]]
    source_reg2 = register[bin_code[12:17]]
    imme = bin_code[0] + bin_code[24] + bin_code[1:7] + bin_code[20:24] + "0"
    if values[source_reg1] < values[source_reg2]:
        program_counter += todecimal(imme, 13)
        count = (program_counter/4)
        branching(count,memory,program_counter)
    

def branch_if_less_unsigned(bin_code, values, register):
    global program_counter
    global count
    source_reg1 = register[bin_code[7:12]]
    source_reg2 = register[bin_code[12:17]]
    imme = bin_code[0] + bin_code[24] + bin_code[1:7] + bin_code[20:24] + "0"
    reg1 = values[source_reg1] + (1 << 13)
    reg2 = values[source_reg2] + (1 << 13)
    if reg1 < reg2:
        program_counter += todecimal(imme, 13)
        count = (program_counter/4)
        branching(count,memory,program_counter)
    

def execute_b_type_instruction(bin_code, values, register, b_type_reg, data_memory):
    global program_counter
    global count 
    func3 = bin_code[17:20]
    func = b_type_reg[func3]
    if func == "beq":
        values = branch_if_equal(bin_code, values, register)
    elif func == "bne":
        values = branch_if_not_equal(bin_code, values, register)
    elif func == "bge":
        values = branch_if_greater_equal(bin_code, values, register)
    elif func == "bgeu":
        values = branch_if_greater_unsigned_equal(bin_code, values, register)
    elif func == "blt":
        values = branch_if_less(bin_code, values, register)
    elif func == "bltu":
        values = branch_if_less_unsigned(bin_code, values, register)
    else:
        pass
    program_counter+=4
    count+=1
    return values,data_memory

def add_upperimm(bin_code, values, register, program_counter):
    dest_reg = register[bin_code[20:25]]
    imme = bin_code[:20] + "000000000000"
    values[dest_reg] = program_counter + todecimal(imme, 32)
    

def load_upperimm(bin_code, values, register):
    dest_reg = register[bin_code[20:25]]
    imme = bin_code[:20] + "000000000000"
    values[dest_reg] = todecimal(imme, 32)
    

def execute_u_type_instruction(bin_code, values, register, u_type_reg,data_memory):
    global count
    global program_counter
    opcode = bin_code[25:]
    func = u_type_reg[opcode]
    if func == "auipc":
        values = add_upperimm(bin_code, values, register, program_counter)
    elif func == "lui":
        values = load_upperimm(bin_code, values, register)
    program_counter+=4
    count+=1
    return values,data_memory

def execute_j_type_instruction(bin_code, values, register, j_type_reg,data_memory):
    global program_counter
    global count
    opcode = bin_code[25:]
    imme = bin_code[0]+bin_code[12:]+bin_code[11]+bin_code[1:11]+"0"
    func = j_type_reg[opcode]
    if func == "jal":
        reg=register[bin_code[20:25]]
        values[reg]=program_counter+4
        program_counter+=todecimal(imme,21)
        count=program_counter/4
        branching(count,memory,program_counter)
    program_counter+=4
    count+=1
    return values,data_memory

def func_Calling(arg,values,register,dic_typeofopcode,data_memory):
    global program_counter
    opcode= arg[25:]
    if opcode == "0110011":
        return execute_r_type_instruction(arg,values,register,dic_typeofopcode["R"],data_memory)
    elif opcode == "0000011" or opcode == "0010011" or opcode == "1100111" :
        return execute_i_type_instruction(arg,values,register,dic_typeofopcode["I"],data_memory)
    elif opcode == "0100011" :
        return execute_s_type_instruction(arg,values,register,data_memory)
    elif opcode == "1101111":
        return execute_j_type_instruction(arg,values,register,dic_typeofopcode["J"],data_memory)
    elif opcode == "1100011":
        return execute_b_type_instruction(arg,values,register,dic_typeofopcode["B"],data_memory)
    elif opcode == "0110111" or opcode == "0010111":
        return execute_u_type_instruction(arg,values,register,dic_typeofopcode["U"],data_memory)
    return values,data_memory


input="s_test4.txt"
output="output.txt"

if not os.path.exists(input):
    sys.exit()

with open(input,"r") as input_file:
    file= input_file.readlines()
    for line in file:
        memory.append(line.strip("\n"))

with open(output,"w") as output_file:
    for bin_co in memory:
        if bin_co==memory[len(memory)-1]:
            for i in data_memory:
                line=""
                line+=str(i)+":"+str(data_memory[i])
            output_file.write(line)
        else:
            register_values,data_memory=func_Calling(bin_co,register_values,registers,dic_type_for_opcode,data_memory)
            file123=print_register(register_values,program_counter)
            output_file.write(file123+"\n")
sys.exit()
