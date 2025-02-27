import { Injectable } from '@nestjs/common';
import * as amqp from 'amqplib';

@Injectable()
export class ConsumerService {
  private async connect() {
    return amqp.connect('amqp://localhost');
  }

  async consumeMessage(queue: string) {
    const connection = await this.connect();
    const channel = await connection.createChannel();
    await channel.assertQueue(queue, { durable: false });

    console.log(`🔄 Esperando mensajes en ${queue}...`);

    channel.consume(queue, (msg) => {
      if (msg !== null) {
        const data = JSON.parse(msg.content.toString());

        // Aplicamos el filtro: Solo aceptar mensajes que tengan un campo 'valid' en true
        if (data.valid) {
          console.log(`✅ Mensaje recibido y aprobado:`, data);
        } else {
          console.log(`❌ Mensaje rechazado por el filtro:`, data);
        }

        channel.ack(msg);
      }
    });
  }
}
