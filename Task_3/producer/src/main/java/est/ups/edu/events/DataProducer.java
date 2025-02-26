package est.ups.edu.events;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.reactive.messaging.Channel;
import org.eclipse.microprofile.reactive.messaging.Emitter;
import io.smallrye.reactive.messaging.kafka.Record;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.jboss.logging.Logger;

import java.util.concurrent.CompletionStage;

/**
 * DataProducer is responsible for sending Kafka messages to the "data-output" channel.
 * It serializes the Student object into JSON before sending it.
 */
@ApplicationScoped
public class DataProducer {

    @Inject
    @Channel("data-output")
    Emitter<Record<Integer, String>> emitter; // ✅ Integer key

    private final ObjectMapper objectMapper = new ObjectMapper(); // JSON Serializer

    /**
     * Sends a Kafka message with student information.
     *
     * @param id Student ID (Integer)
     * @param nombre Student first name
     * @param apellido Student last name
     * @param carrera Student's career
     * @param semestre Student semester
     * @return CompletionStage representing the async operation
     */
    public CompletionStage<Void> sendMessage(int id, String nombre, String apellido, String carrera, int semestre) {
        try {
            // Convert to JSON string manually
            String studentJson = String.format("{\"id\":%d,\"nombre\":\"%s\",\"apellido\":\"%s\",\"carrera\":\"%s\",\"semestre\":%d}",
                    id, nombre, apellido, carrera, semestre);

            // ✅ Log what is being sent
            System.out.println("🔹 Sending to Kafka -> Key (Integer): " + id + ", Value (JSON): " + studentJson);

            // ✅ Send message with Integer key and JSON value
            return emitter.send(Record.of(id, studentJson));
        } catch (Exception e) {
            throw new RuntimeException("Error serializing Student data to JSON", e);
        }
    }

}
