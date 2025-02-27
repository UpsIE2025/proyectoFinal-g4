import { Module } from '@nestjs/common';
import { ProducerController } from './producer.controller';
import { ProducerService } from './producer.service';
import { ConsumerService } from './consumer.service';

@Module({
  imports: [],
  controllers: [ProducerController],
  providers: [ProducerService, ConsumerService],
})
export class AppModule {
  constructor(private readonly consumerService: ConsumerService) {
    this.consumerService.consumeMessage('messages');
  }
}
