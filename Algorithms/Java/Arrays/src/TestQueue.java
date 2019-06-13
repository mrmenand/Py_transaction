import java.util.Random;

public class TestQueue {
	private static double testQueue(Queue<Integer> q, int opCount) {
		long startTime = System.nanoTime();

		Random random = new Random();
		for (int i = 0; i < opCount; i++)
			q.enqueue(random.nextInt(Integer.MAX_VALUE));
		for (int i = 0; i < opCount; i++)
			q.dequeue();

		long endTime = System.nanoTime();
		return (endTime - startTime) / 1000000000.0;
	}

	public static void main(String[] args) {
		int opCount = 100000;
		ArrayQueue<Integer> arrayQueue = new ArrayQueue<>();
		double time1 = testQueue(arrayQueue, opCount);
		System.out.println("ArrayQueue, time: " + time1 + " s");

		CircuQueue<Integer> circuQueue = new CircuQueue<>();
		double time2 = testQueue(circuQueue, opCount);
		System.out.println("CicruQueue, time: " + time2 + " s");


	}
}