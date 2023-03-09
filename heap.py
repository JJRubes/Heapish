# commands be changed as long as the following hold true
# 1. nop is [0]
# 2. all commands have different bitstrings
# 3. commands are parsed top-to-bottom
#    changinge the order of commands doesn't change
#    how a string is parsed
commands = {
        "nop": [0],
        "jmp": [1, 0],
        "del": [1, 1, 0],
        "psh": [1, 1, 1]
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
# that is large enough to fit the command
# and writes the command there
def write(heap, command):
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
        if space >= length:
            overwrite(heap, ip - space, command)
            return
    overwrite(heap, ip - space, command)

def push(heap, command):
    # copy the command 3 times
    for _ in range(3):
        write(heap, command)

def run(heap, p, steps = 20):
    ip = 0
    for _ in range(20):
        command, length = parse(heap, ip)
        print(f"Running {command}")
        if command == "nop":
            ip += length
            if ip == len(heap):
                print("And off into infinity...")
                break;
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
            push(heap, writeCommand)
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
    heap = []
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
