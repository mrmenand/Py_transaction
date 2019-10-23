总结Python用多种方式实现多进程 
- Queue 
- Condition 
- Barrier   
- Event
- Lock 
- Samaphore 

需要进行并发编程，通常是使用多线程/多进程模型实现的。由于GIL的存在，多线程对于计算密集型的任务并不十分友好，而对于IO密集型任务，可以在等待IO的时候进行线程调度，让出GIL，实现『假并发』。
当然对于IO密集型的任务另外一种选择就是协程，协程其实是运行在单个线程中的，避免了多线程模型中的线程上下文切换，减少了很大的开销。
从某些角度来理解协程其实就是一个可以暂停执行的函数，并且可以恢复继续执行

### Barrier  
栅栏，也叫屏障。可以想象成路障、道闸。 
每进一个就等待，不够就阻塞，知道够parties就开闸 
方法：
wait（）wait(timeout=None) 等待通过栅栏，返回0到线程数-1的整数(barrier_id)，每个线程返回不同。如果wait方法设置了超时，并超时发送，栅栏将处于broken状态。
broken() 检测栅栏是否处于打破的状态，返回True或False
abort()  将栅栏置于broken状态，等待中的线程或者调用等待方法的线程都会抛出threading.BrokenBarrieError异常，直到reset方法来恢复栅栏
reset()   恢复栅栏，重新开始拦截  

* 1114 按序打印  
   -  通过阻塞，等待任务 
   -  [循环/阻塞*5/队列*2/字典的九种解法](https://leetcode-cn.com/problems/print-in-order/solution/1114-an-xu-da-yin-python3de-5chong-jie-fa-by-tuotu/) 

* 1115 交替打印FooBar
   - 与1114题目类似，都是通过阻塞，实现异步
