# Heapish
This esolang was created from the making a language around the "put it
where it fits" model of memory management. My hope was that a
significant part of the computational power of Heapish would come from
memory fragmentation and how new data being fitted into a fragmented
memory could allow for some form of conditional logic. 

I think that this project has failed in a way because I don't feel like
I have managed to capture either a feeling of "where it fits" algorithm
nor have I made a language that seems compelling.

## How It Works
In heapish all of the commands are in and operate on an infinite array
of bits, which in the code is called the "heap". I do not have a
canonical set of instructions, in the code there are 2 listed. However,
there are some features that the instruction sets share. 
- Nop should be represented with 0
- Any instruction that adds instructions to the heap should use the heap
  push
- Jumps should be relative to the command or to the start of the heap
- The instruction set should not allow ambiguous heaps

### The 2 Instruction Sets
Command Name | Value | What it Does
:--- | ---: | :---
nop | 0 | No-op
jmp | 10 | Jumps to the start of the array.
del | 110 | Replaces the next instruction with nops
psh | 111 | Pushes the next instruction 3 times, one after the other.

Command Name | Value | What it Does
:--- | ---: | :---
nop | 0 | No-op
jmps | 100 | Jumps to the start of the array.
jmpn | 101 | Jumps over the next instruction.
del | 110 | Replaces the next instruction with nops
psh1 | 1110 | Pushes the next instruction.
psh2 | 11110 | Pushes the next instruction 2 times in a contiguous block.
psh3 | 111110 | Pushes the next instruction 3 times in a contiguous block.
psh4 | 1111110 | Pushes the next instruction 4 times in a contiguous block.
psh5 | 1111111 | Pushes the next instruction 5 times in a contiguous block.

## Other Possibilities
I had more ideas for areas to explore but I do not feel like continuing
this without an outside perspective.

### Skipping Nops
The ideas was that commands that take an argument would look for the
command that isn't a nop to use as the argument. But, for the same
reason as a lot of the ideas I had for the heap idea, I don't know how I
would handle when there are no more arguments.

### Self Deleting Commands
You can see the remains of this in the code. When a command is called it
replaces itself with nops. The commented out parts of the code delete a
push after it has completed its operation.

### String Replacements
The whole heap could probably be more compactly represented with a list
of commands than and simply replace each command with some number of
nops when it is deleted. 
