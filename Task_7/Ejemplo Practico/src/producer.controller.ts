import { Controller, Post, Body, UsePipes } from '@nestjs/common';
import { ProducerService } from './producer.service';
import { MessageValidationPipe } from './message.pipe';

@Controller('publish')
export class ProducerController {
  constructor(private readonly producerService: ProducerService) {}

  @Post()
  @UsePipes(new MessageValidationPipe())
  async publishMessage(@Body() message: any) {
    await this.producerService.publishMessage('messages', message);
    return { status: 'Mensaje enviado correctamente' };
  }
}
