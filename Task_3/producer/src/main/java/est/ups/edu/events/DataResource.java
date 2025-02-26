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

/**
 * DataResource is a RESTful resource class that provides an endpoint for sending Kafka messages.
 * It consumes JSON data and produces JSON responses.
 */
@Path("/kafka")
@ApplicationScoped
public class DataResource {

    @Inject
    DataProducer producer;

    /**
     * Endpoint to send a Kafka message with student information.
     * Consumes a JSON representation of a Student object and produces a JSON response.
     *
     * @param student the student object containing ID, name, surname, semester, and career information
     * @return a CompletionStage representing the asynchronous response
     */
    @POST
    @Path("/send")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public CompletionStage<Response> sendMessage(Student student) {
        return producer.sendMessage(
                        student.getId(),
                        student.getNombre(),
                        student.getApellido(),
                        student.getCarrera(),
                        student.getSemestre()
                ).thenApply(unused -> Response.accepted().build())
                .exceptionally(e -> Response.serverError().entity("Error sending message: " + e.getMessage()).build());
    }

}
