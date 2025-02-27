import { Injectable } from '@nestjs/common';
import * as amqp from 'amqplib';

@Injectable()
export class ProducerService {
    private async connect() {
        return amqp.connect('amqp://localhost');
        // return amqp.connect(process.env.RABBITMQ_URL ?? 'amqp://rabbitmq:5672');
    }
    


  async publishMessage(queue: string, message: any) {
    const connection = await this.connect();
    const channel = await connection.createChannel();
    await channel.assertQueue(queue, { durable: false });
    channel.sendToQueue(queue, Buffer.from(JSON.stringify(message)));

    await channel.close();
    await connection.close();
  }
}
