package com.msc_productor.msc_productor.Controller;

import com.msc_productor.msc_productor.Services.RedisMessagePublisher;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/redis")
public class ProductorController {
    private final RedisMessagePublisher redisService;

    public ProductorController(RedisMessagePublisher redisService) {
        this.redisService = redisService;
    }

    @PostMapping("/guardar")
    public String guardar(@RequestParam String clave, @RequestParam String valor) {
        redisService.guardarString(clave, valor, 10); // Guarda con 10 minutos de expiración
        return "Valor guardado en Redis!" + valor;
    }

}
