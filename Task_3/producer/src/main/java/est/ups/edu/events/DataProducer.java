package est.ups.edu.events;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import org.eclipse.microprofile.reactive.messaging.Channel;
import org.eclipse.microprofile.reactive.messaging.Emitter;



import java.util.concurrent.CompletionStage;

@ApplicationScoped
public class DataProducer {

    @Inject
    @Channel("data-output")
    Emitter<String> emitter;

    public CompletionStage<Void> sendMessage(String message) {
        return emitter.send(message);
    }
}
