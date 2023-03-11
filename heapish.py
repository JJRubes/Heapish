# commands be changed as long as the following hold true
# 1. nop is [0]
# 2. all commands have different bitstrings
# 3. commands are parsed top-to-bottom
#    changinge the order of commands doesn't change
#    how a string is parsed
simpleCommands = {
        "nop": [0],
        "jmp": [1, 0],
        "del": [1, 1, 0],
        "psh": [1, 1, 1]
        }

complexCommands = {
        "nop": [0],
        "jmps": [1, 0, 0],
        "jmpn": [1, 0, 1],
        "dell": [1, 1, 0],
        "psh1": [1, 1, 1, 0],
        "psh2": [1, 1, 1, 1, 0],
        "psh3": [1, 1, 1, 1, 1, 0],
        "psh4": [1, 1, 1, 1, 1, 1, 0],
        "psh5": [1, 1, 1, 1, 1, 1, 1]
        }

# finds the type of the next command
def parse(heap, ip):
    if ip >= len(heap):
        heap.append(0)
    for k, v in commands.items():
        if heap[ip:ip + len(v)] == v:
            return (k, len(v))

# zeros out the next command
def delete(heap, ip, length):
    for i in range(ip, ip + length):
        heap[i] = 0

# writes a command at a location
# doesn't care about what is there
def overwrite(heap, ip, command):
    for i in commands[command]:
        if ip >= len(heap):
            heap.append(i)
        else:
            heap[ip] = i
        ip += 1

# does a heap write
# it finds the first location containing all nops
# that is large enough to fit the commands
# and writes the commands there
def write(heap, command, n):
    length = len(commands[command])
    ip = 0
    space = 0
    while ip < len(heap):
        c, l = parse(heap, ip)
        if c == "nop":
            space += l
        else:
            space = 0

        ip += l
        if space >= length * n:
            for i in range(n):
                overwrite(heap, ip - space, command)
                ip += length
            return
    for i in range(n):
        overwrite(heap, ip - space, command)
        ip += length

def push(heap, command, n, contiguous):
    if contiguous:
        write(heap, command, n)
    else:
        for _ in range(n):
            write(heap, command, 1)

def run(heap, p, steps = 20):
    ip = 0
    for _ in range(steps):
        command, length = parse(heap, ip)
        print(f"Running {command}")
        if command == "nop":
            ip += length
            if ip == len(heap):
                print("And off into infinity...")
                break;
        # start of simple command set
        elif command == "jmp":
            # delete(heap, ip, length)
            ip = 0
        elif command == "del":
            # delete(heap, ip, length)
            ip += length
            _, nextLength = parse(heap, ip)
            delete(heap, ip, nextLength)
            ip += nextLength
        elif command == "psh":
            writeCommand, nextLength = parse(heap, ip + length)
            push(heap, writeCommand, 3, False)
            # delete(heap, ip, length)
            ip += length
            # delete(heap, ip, nextLength)
            ip += nextLength
        # start of complex command set
        elif command == "jmps":
            # delete(heap, ip, length)
            ip = 0
        elif command == "jmpn":
            # delete(heap, ip, length)
            ip += length
        elif command == "dell":
            # delete(heap, ip, length)
            ip += length
            _, nextLength = parse(heap, ip)
            delete(heap, ip, nextLength)
            ip += nextLength
        elif command == "psh1":
            writeCommand, nextLength = parse(heap, ip + length)
            push(heap, writeCommand, 1, True)
            # delete(heap, ip, length)
            ip += length
            # delete(heap, ip, nextLength)
            ip += nextLength
        elif command == "psh2":
            writeCommand, nextLength = parse(heap, ip + length)
            push(heap, writeCommand, 2, True)
            # delete(heap, ip, length)
            ip += length
            # delete(heap, ip, nextLength)
            ip += nextLength
        elif command == "psh3":
            writeCommand, nextLength = parse(heap, ip + length)
            push(heap, writeCommand, 3, True)
            # delete(heap, ip, length)
            ip += length
            # delete(heap, ip, nextLength)
            ip += nextLength
        elif command == "psh4":
            writeCommand, nextLength = parse(heap, ip + length)
            push(heap, writeCommand, 4, True)
            # delete(heap, ip, length)
            ip += length
            # delete(heap, ip, nextLength)
            ip += nextLength
        elif command == "psh5":
            writeCommand, nextLength = parse(heap, ip + length)
            push(heap, writeCommand, 5, True)
            # delete(heap, ip, length)
            ip += length
            # delete(heap, ip, nextLength)
            ip += nextLength
        else:
            print("invalid")
            break
        if p:
            print(heap)

if __name__ == "__main__":
    global commands
    heap = []
    while True:
        value = input("Command set ([s]imple/[c]omplex): ")
        if value == "s" or value == "simple":
            commands = simpleCommands
            break
        if value == "c" or value == "complex":
            commands = complexCommands
            break
    while True:
        value = input(">>> ")
        if value == "q":
            break
        if value == "run":
            run(heap, True)
            break

        if value in commands:
            for i in commands[value]:
                heap.append(i)
            print(heap)
            continue

        # check if it is a binary number
        try:
            int(value, 2)
        except ValueError:
            print("did you mean 'run' or 'q'?")
            continue

        for digit in value:
            if digit == "0":
                heap.append(0)
            else:
                heap.append(1)
        print(heap)
