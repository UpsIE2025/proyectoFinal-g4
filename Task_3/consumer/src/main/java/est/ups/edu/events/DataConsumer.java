package est.ups.edu.events;

import jakarta.enterprise.context.ApplicationScoped;
import lombok.extern.slf4j.Slf4j;
import org.eclipse.microprofile.reactive.messaging.Incoming;
import io.smallrye.reactive.messaging.kafka.Record;

@ApplicationScoped
@Slf4j
public class DataConsumer {

    @Incoming("data-input")
    public void receive(Record<Integer, String> record){

        log.info("Semestre: "+ record.key()+" ,Carrera: "+ record.value());
        
    }

}
