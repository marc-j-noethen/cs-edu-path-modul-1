## Summary Based on the 80/20 Principle

**Core statement:** CPU scheduling decides on process execution, while synchronisation prevents race conditions through controlled resource access.

**The most important 20% of the information:**

### 1. CPU Scheduling: The Basics

**Problem:** A computer has one CPU, but dozens to hundreds of active processes/threads that all need CPU time.

**Solution through scheduling:**

- **Preemptive Scheduling** (modern Windows): OS interrupts tasks after a short time slice and switches to others
- **Context Switch:** OS saves the current task state and loads the next task
- **Goals:** Maximise CPU utilisation, ensure responsiveness, fair resource distribution

**Important for Windows 11:** Task Manager shows processes, CPU usage, and thread count in real time – ideal for observing scheduling effects.

### 2. Race Conditions: The Main Problem

**Scenario:** Two threads access the same data simultaneously (e.g. bank account balance).

**Example error:**

- Thread 1: Reads $100, calculates +$50 = $150
- _Context switch occurs before saving_
- Thread 2: Reads $100 (still!), calculates -$30 = $70, saves $70
- Thread 1: Now saves $150 (overwrites Thread 2)
- **Result:** $150 instead of correct $120 – the $30 withdrawal was lost

**Critical section:** Code area where shared data is modified – must be protected.

### 3. Synchronisation with Mutexes

**Mutex = Key to the critical section:**

1. Thread attempts to acquire the lock
2. If available → Thread enters the critical section
3. If occupied → Thread waits (blocks)
4. After completion → Thread releases the lock

**Effect:** Only one thread can be in the critical section at a time → **Mutual Exclusion** is guaranteed → Race conditions are prevented.

### 4. New Problems Introduced by Synchronisation

**Deadlock:**

- Thread A: Holds Lock X, waits for Lock Y
- Thread B: Holds Lock Y, waits for Lock X
- Both wait for each other forever → System frozen

**Starvation:**

- Thread is repeatedly skipped and never gains access to the resource
- Other threads always get the lock first

### Practical Relevance for Windows 11

**Observation tools:**

- **Task Manager:** CPU usage, processes, threads
- **Resource Monitor:** Detailed thread activity
- **Process Explorer:** Advanced process/thread analysis

**Application:** These concepts are fundamental for system administration, performance tuning, and understanding system freezes or performance issues in Windows environments.

## Table: Tools, Technical Terms and Vocabulary

|Category|Term|Meaning|
|---|---|---|
|**Tools Used**|Task Manager (Windows 11)|System tool for monitoring processes, CPU usage and threads|
||Resource Monitor|Extended view for CPU, memory and thread activity in Windows|
||Performance Monitor|Windows tool for detailed performance analysis and scheduling metrics|
||Process Explorer (Sysinternals)|Advanced tool for analysing processes and threads|
||PowerShell|Scripting for process and thread management|
|**Technical Terms**|CPU Scheduling|OS mechanism for deciding which process/thread receives CPU time|
||Preemptive Scheduling|Interruptible scheduling in which the OS can interrupt tasks after a time slice|
||Non-Preemptive Scheduling|Cooperative scheduling in which tasks must release the CPU themselves|
||Context Switch|Switching between tasks by saving/loading the execution state|
||Time Slice (Quantum)|Fixed CPU time that a process/thread receives at a stretch|
||Race Condition|Error caused by uncontrolled simultaneous access to shared data|
||Critical Section|Code area with access to shared resources that requires protection|
||Mutual Exclusion|Principle that only one thread may be in the critical section at a time|
||Mutex (Lock)|Synchronisation mechanism for securing critical sections|
||Deadlock|Blocking of multiple threads that are mutually waiting for resources|
||Starvation|Permanent denial of resource access for a thread|
||Thread Synchronisation|Coordination of threads when accessing shared resources|
||Context|Complete execution state of a process/thread|
||Blocking|Waiting state of a thread when attempting to acquire a locked resource|
|**Key Vocabulary**|Responsiveness|Fast response time of the system to user input|
||Fairness|Even distribution of CPU time across all processes|
||Throughput|Number of completed tasks per unit of time|
||CPU utilisation|Percentage of time the CPU is actively working|
||Overhead|Additional resource expenditure for system operations|
||Shared Resource|Resource (memory, file) accessed by multiple threads|
||Data Consistency|Correctness and integrity of data during parallel access|
||Acquire Lock|Acquiring the locking mechanism before entering the critical section|
||Release Lock|Releasing the locking mechanism after leaving the critical section|
||Indefinite Blocking|Unlimited waiting time of a thread for a resource|
||Preemption|Interruption of a running process by the OS|
||Concurrent Access|Simultaneous access of multiple threads to the same resource|
||Thread-safe|Code that does not cause race conditions when executed in parallel|

---