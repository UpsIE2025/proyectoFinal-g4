package com.msc_productor.msc_productor.Services;


import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class RedisMessagePublisher {
    private final StringRedisTemplate stringRedisTemplate;

    public RedisMessagePublisher(StringRedisTemplate stringRedisTemplate) {
        this.stringRedisTemplate = stringRedisTemplate;
    }

    // Guardar un string en Redis con un tiempo de expiración (opcional)
    public void guardarString(String clave, String valor, long tiempoEnMinutos) {
        stringRedisTemplate.opsForValue().set(clave, valor, tiempoEnMinutos);
    }
}
