# Q.6. Explain deadlocks and race conditions.
# Deadlocks and race conditions are two common concurrency issues that can occur in multithreaded programs.

# Deadlocks:
# A deadlock occurs when two or more threads are blocked waiting for each other to release a resource that they are holding. In other words, each thread is waiting for a resource that is being held by another thread, resulting in a situation where no progress can be made. This can cause the program to hang indefinitely or even crash.

# A common example of a deadlock is the "dining philosophers" problem, where a group of philosophers each require two forks to eat, but only have access to one fork each. If each philosopher grabs the fork to their right and waits for the fork to their left to be released, they can end up in a deadlock where no one can eat.

# To avoid deadlocks, it is important to use proper synchronization mechanisms, such as locks and semaphores, to ensure that resources are acquired and released in a consistent and predictable manner.

# Race Conditions:
# A race condition occurs when the behavior of a program depends on the timing or order of events, such as the interleaving of threads. In other words, two or more threads are competing for access to a shared resource and the outcome depends on which thread wins the race.

# A common example of a race condition is the "lost update" problem, where two threads are trying to update the same variable or data structure simultaneously. Depending on the timing of the updates, one thread's update may be lost or overwritten by the other thread's update, resulting in incorrect behavior.

# To avoid race conditions, it is important to use proper synchronization mechanisms to ensure that only one thread can access a shared resource at a time. This can include using locks or atomic operations to ensure that updates to shared data are performed atomically and cannot be interrupted by other threads.

# In summary, deadlocks and race conditions are two common concurrency issues that can occur in multithreaded programs. To avoid these issues, it is important to use proper synchronization mechanisms and design the program in a way that avoids resource contention and timing dependencies