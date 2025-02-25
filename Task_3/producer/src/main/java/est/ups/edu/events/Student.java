package est.ups.edu.events;


import lombok.*;

@Data
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Student {

    private Integer id;

    private String nombre;

    private String apellido;

    private String carrera;

    private int semestre;



}
