import 'dart:convert';

ResponseApi responseApiFromJson(String str) =>
    ResponseApi.fromJson(json.decode(str));

String responseApiToJson(ResponseApi data) => json.encode(data.toJson());

class ResponseApi {
  bool? success;
  String? message;
  dynamic data;

  ResponseApi({this.success, this.message, this.data});

  factory ResponseApi.fromJson(Map<String, dynamic> json) {
    // Ajustar para manejar la estructura de la respuesta GraphQL
    final data = json['data']?['saveStudent'];
    return ResponseApi(
      success: data != null,
      message: data?['message'],
      data: data,
    );
  }

  Map<String, dynamic> toJson() => {
    "success": success,
    "message": message,
    "data": data,
  };
}
