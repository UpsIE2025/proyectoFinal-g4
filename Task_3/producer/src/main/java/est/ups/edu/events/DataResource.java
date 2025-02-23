package est.ups.edu.events;

import jakarta.enterprise.context.ApplicationScoped;
import jakarta.inject.Inject;
import jakarta.ws.rs.Consumes;
import jakarta.ws.rs.POST;
import jakarta.ws.rs.Path;
import jakarta.ws.rs.Produces;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

import java.util.concurrent.CompletionStage;

@Path("/kafka")
@ApplicationScoped
public class DataResource {

    @Inject
    DataProducer producer;


    @POST
    @Path("/send")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public CompletionStage<Response> sendMessage(String message) {
        return producer.sendMessage(message)
                .thenApply(unused -> Response.accepted().build());
    }
}
