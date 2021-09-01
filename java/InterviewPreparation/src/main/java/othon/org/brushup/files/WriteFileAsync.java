package othon.org.brushup.files;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.Instant;
import org.jetbrains.annotations.NotNull;

public class WriteFileAsync {
    static final String filename = "test.txt";
    static final int ITERATIONS = 10;


    public static void main(String[] args) throws InterruptedException {
        Thread t = createWriterThread();
        t.start();

        Thread t2 = createReaderThread();
        t2.start();
        t.join();
        t2.join();
    }

    @NotNull
    private static Thread createWriterThread() {
        return new Thread(() -> {
            FileWriter fileWriter = null;
            try {
                fileWriter = new FileWriter(filename);
            } catch (IOException e) {
                e.printStackTrace();
            }
            PrintWriter printWriter = new PrintWriter(fileWriter);


            for (int i = 0; i < ITERATIONS ; i++) {
                final String log = String.format("[%s][%s][%d] %s\n", Instant.now().toString(), Thread.currentThread().getName(), i, "Some string" );
                System.out.println(log);
                printWriter.print(log);
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            printWriter.close();
        });
    }

    private static Thread createReaderThread() {
        return new Thread(() -> {
            FileReader fileReader = null;
            try {
                fileReader = new FileReader(filename);
            } catch (IOException e) {
                e.printStackTrace();
            }
            BufferedReader reader = new BufferedReader(fileReader);

            for (int i = 0; i < ITERATIONS ; i++) {
                try {
                    final String line = reader.readLine();
                    System.out.println("Reading " + line);
                    Thread.sleep(1000);
                } catch (InterruptedException | IOException e) {
                    e.printStackTrace();
                }
            }
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        });
    }
}
