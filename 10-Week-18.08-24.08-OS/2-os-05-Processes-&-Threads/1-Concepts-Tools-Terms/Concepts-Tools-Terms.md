# Core Concepts

### Program vs. Process

- **Program**: A passive file on the hard drive (e.g. `chrome.exe`) – like a recipe in a cookbook
- **Process**: An actively running program in memory – like a chef actually cooking the recipe
- Every process has its own memory area, its own resources, and runs independently of other processes

### The 5 Process States

A process goes through the following states:

1. **New**: Is currently being created
2. **Ready**: Waiting for CPU time (in the queue)
3. **Running**: Currently being executed
4. **Waiting**: Waiting for an event (e.g. file download, user input)
5. **Terminated**: Finished, resources are being released

The OS **Scheduler** decides which "Ready" process runs next. By switching rapidly, the impression of **multitasking** is created.

## What are Threads?

**Threads** are the smallest unit of execution within a process:

- **One process** = One kitchen (container with resources)
- **Threads** = Multiple chefs in the same kitchen (workers operating in parallel)

### Key Characteristics of Threads

1. **Lightweight**: Faster to create than new processes
2. **Resource sharing**: Share the memory, code, and files of the process
3. **Independent execution**: Each thread has its own program counter and registers

### Why Use Threads?

1. **Responsiveness**: UI stays responsive while tasks run in the background
    
    - Example: Web browser loads a page while you can keep scrolling/clicking
2. **Efficiency**: No process overhead, since resources are shared
    
3. **Scalability**: On multi-core CPUs, threads can run truly in parallel
    

## Practical Example: Web Browser

A browser process might have the following threads:

- **Thread 1**: Renders the web page
- **Thread 2**: Downloads images
- **Thread 3**: Responds to mouse movements/clicks
- **Thread 4**: Executes JavaScript

All work in parallel within the same browser process!

## Processes vs. Threads Compared

|Aspect|Process|Thread|
|---|---|---|
|**Memory**|Own, isolated memory area|Shares memory with other threads in the process|
|**Creation**|Resource-intensive, slow|Lightweight, fast|
|**Communication**|Costly (Inter-Process Communication)|Easy (shared memory)|
|**Isolation**|Strongly isolated (crash does not affect others)|Weak (crash can affect all threads)|
|**Independence**|Completely independent|Dependent on the main process|

## Windows 11 Tools for Observation

### Task Manager (Ctrl+Shift+Esc)

- **Processes tab**: Overview of all running applications
- **Details tab**: Detailed technical information (PID, memory, CPU)
- To terminate: Right-click → "End task"

### PowerShell

```powershell
Get-Process  # Show all processes
Get-Process -Name chrome  # Only Chrome processes
Get-Process | Sort-Object CPU -Descending  # Sorted by CPU usage
```

## Potential Problems

**With threads**: When multiple threads access the same memory simultaneously, **race conditions** can occur (like two chefs both trying to use the same knife at the same time). This is why **synchronisation** is important.

**Core message**: Processes are isolated program instances, threads are lightweight workers within a process. The OS manages both through scheduling to enable efficient multitasking. Modern applications use threads extensively for parallel tasks and better performance.

## Tools Used

|Tool/Application|Meaning|
|---|---|
|**Task Manager**|Shows all running processes, their resource usage, and allows terminating processes (Ctrl+Shift+Esc)|
|**PowerShell**|Command-line interface for advanced system management and process analysis|
|**Get-Process** (PowerShell command)|Lists all currently running processes with details such as name, ID, CPU and memory usage|
|**Details Tab** (Task Manager)|Detailed view of all processes with technical information such as Process ID (PID) and memory consumption|
|**Processes Tab** (Task Manager)|Simplified overview of running applications and background processes with resource usage|

## Technical Terms

|Term|Meaning|
|---|---|
|**Program**|Passive unit – an executable file on the hard drive (e.g. notepad.exe) containing instructions and data|
|**Process**|Active execution of a program in memory with its own resources and its own memory area|
|**Thread**|Smallest unit of execution within a process; multiple threads can work in parallel within a process|
|**Scheduler**|OS component that decides which process/thread receives CPU time next|
|**Multitasking**|Ability of the OS to seemingly execute multiple processes simultaneously by switching rapidly|
|**Concurrency**|Multiple tasks make progress within the same time period, but not necessarily at the same instant|
|**Program Counter**|Register that stores the address of the next instruction to be executed|
|**Register Set**|Small, fast memory areas in the CPU for temporary data during execution|
|**Address Space**|The memory area assigned to the process in which code and data reside|
|**Multi-core Processor**|Processor with multiple computing cores that enable true parallel execution|
|**Single-threaded**|Process with only one thread of execution, processing tasks one after another|
|**Multi-threaded**|Process with multiple threads of execution that can work in parallel|
|**Context Switch**|The CPU switching from one process/thread to another by saving/loading the state|

## Key Vocabulary

|Vocabulary|Meaning|
|---|---|
|**Process States**|The various states a process passes through (New, Ready, Running, Waiting, Terminated)|
|**New**|Process is currently being created, resources are being allocated|
|**Ready**|Process has all resources and is waiting for CPU allocation|
|**Running**|Process is currently being executed by the CPU|
|**Waiting/Blocked**|Process is waiting for an external event (I/O, user input) and cannot continue|
|**Terminated**|Process has completed execution, resources are being released|
|**Responsiveness**|Ability of an application to respond quickly to user input|
|**Resource Sharing**|Threads within a process share memory and other resources|
|**Scalability**|Ability to increase performance by utilising multiple CPU cores|
|**Lightweight**|Threads are less resource-intensive to create and manage than processes|
|**Independent Execution**|Each thread can independently carry out tasks|
|**Memory Space**|The RAM area assigned to a process for code, data, and stack|
|**Overhead**|Additional resource expenditure for management tasks of the operating system|
|**Synchronisation**|Coordination between threads to avoid conflicts when accessing shared resources|
|**I/O Completion**|Completion of an input/output operation (e.g. file read, download finished)|

---