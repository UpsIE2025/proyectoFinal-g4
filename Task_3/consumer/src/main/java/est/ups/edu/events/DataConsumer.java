package est.ups.edu.events;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import jakarta.enterprise.context.ApplicationScoped;
import lombok.extern.slf4j.Slf4j;
import org.eclipse.microprofile.reactive.messaging.Incoming;
import io.smallrye.reactive.messaging.kafka.Record;

/**
 * DataConsumer is a class that listens to incoming Kafka messages on the "data-input" channel.
 * It processes each message by manually extracting attributes from the JSON.
 */
@ApplicationScoped
@Slf4j
public class DataConsumer {

    private final ObjectMapper objectMapper = new ObjectMapper(); // JSON parser

    /**
     * Receives a Kafka record from the "data-input" channel.
     * Extracts and logs student attributes manually.
     *
     * @param record the Kafka record containing an Integer key and a JSON string value
     */
    @Incoming("data-input")
    public void receive(Record<Integer, String> record) {
        try {
            // ✅ Ensure key is an Integer
            int studentId = record.key();

            // ✅ Parse JSON value
            JsonNode jsonNode = objectMapper.readTree(record.value());

            // Extract fields
            String nombre = jsonNode.get("nombre").asText();
            String apellido = jsonNode.get("apellido").asText();
            String carrera = jsonNode.get("carrera").asText();
            int semestre = jsonNode.get("semestre").asInt();

            // ✅ Log extracted values
            log.info("📩 Received Student Data:");
            log.info("🆔 ID: " + studentId);
            log.info("👤 Nombre: " + nombre + " " + apellido);
            log.info("🎓 Carrera: " + carrera);
            log.info("📅 Semestre: " + semestre);

        } catch (Exception e) {
            log.error("❌ Error parsing Kafka message: " + record.value(), e);
        }
    }


}
