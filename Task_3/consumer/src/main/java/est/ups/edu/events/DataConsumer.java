package est.ups.edu.events;

import jakarta.enterprise.context.ApplicationScoped;
import lombok.extern.slf4j.Slf4j;
import org.eclipse.microprofile.reactive.messaging.Incoming;

@ApplicationScoped
@Slf4j
public class DataConsumer {

    @Incoming("data-input")
    public void receive(String message) {

        log.info(message);

    }

}
