import { PipeTransform, Injectable, ArgumentMetadata, BadRequestException } from '@nestjs/common';
import { plainToInstance } from 'class-transformer';
import { IsBoolean, IsString, validateSync } from 'class-validator';

class MessageDto {
  @IsString()
  message: string;

  @IsBoolean()
  valid: boolean;
}

@Injectable()
export class MessageValidationPipe implements PipeTransform {
  transform(value: any, metadata: ArgumentMetadata) {
    const object = plainToInstance(MessageDto, value);
    const errors = validateSync(object);
    if (errors.length > 0) {
      throw new BadRequestException('El mensaje no es válido');
    }
    return object;
  }
}
