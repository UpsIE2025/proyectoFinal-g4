package est.ups.edu.events;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.reactive.messaging.Channel;
import org.eclipse.microprofile.reactive.messaging.Emitter;
import io.smallrye.reactive.messaging.kafka.Record;


import java.util.concurrent.CompletionStage;

@ApplicationScoped
public class DataProducer {

    @Inject
    @Channel("data-output")
    Emitter<Record<Integer, String>> emitter;

    public CompletionStage<Void> sendMessage(Student student) {
        return emitter.send(Record.of(student.semestre, student.carrera));
    }
}
