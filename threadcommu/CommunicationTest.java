package threadcommu;

public class CommunicationTest {
    public static void main(String[] args) {
        Number number = new Number();
        Thread t1 = new Thread(number);
        Thread t2 = new Thread(number);
        t1.setName("线程1");
        t2.setName("线程2");

        t1.start();
        t2.start();
    }
}


class Number implements Runnable{
    private int number = 1;
    Object obj = new Object();

    @Override
    public void run() {
        while(true){
            synchronized(obj) {
                obj.notify();
                if (number <= 100) {
                    try {
                        Thread.sleep(10);  //线程进入阻塞状态，但不会释放线程锁
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    System.out.println(Thread.currentThread().getName() + ":" + number);
                    number++;
                    try {
                        // 使得调用如下wait()方法的线程进入阻塞状态并释放线程锁
                        obj.wait();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                } else {
                    break;
                }
            }
        }
    }
}