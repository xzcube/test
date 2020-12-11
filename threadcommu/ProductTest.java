package threadcommu;

public class ProductTest {
    public static void main(String[] args) {
        Clerk clerk = new Clerk();
        Producer p1 = new Producer(clerk);
        Consume c1 = new Consume(clerk);
        Consume c2 = new Consume(clerk);

        p1.setName("生产者1");
        c1.setName("消费者1");
        c2.setName("消费者2");

        p1.start();
        c1.start();
        c2.start();
    }
}


class Clerk{
    private int product;

    //生产产品
    public synchronized void produceProduct(){
        if(product < 20) {
            product++;
            System.out.println(Thread.currentThread().getName() + "开始生产第" + product + "个产品");
            notify();
        }else {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    //消费产品
    public synchronized void consumeProduct(){
        if(product > 0){
            System.out.println(Thread.currentThread().getName() + "消费第" + product + "个产品");
            product--;
            notify();
        }else {
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}


class Producer extends Thread{
    Clerk clerk = new Clerk();

    public Producer(Clerk clerk) {
        this.clerk = clerk;
    }

    @Override
    public void run() {
        System.out.println(Thread.currentThread().getName() + "：生产产品");
        while(true){
            try {
                Thread.sleep(20);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            clerk.produceProduct();
        }
    }
}


class Consume extends Thread{
    Clerk clerk = new Clerk();

    public Consume(Clerk clerk){
        this.clerk = clerk;
    }

    @Override
    public void run() {
        System.out.println(getName() + ":消费产品");
        while (true){
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            clerk.consumeProduct();
        }
    }
}
