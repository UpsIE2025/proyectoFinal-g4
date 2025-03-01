import 'dart:convert';
import 'dart:io';
import 'package:path/path.dart';
import 'package:get/get.dart';
import 'package:chasky/src/environment/environment.dart';
import 'package:chasky/src/models/response_api.dart';
import 'package:chasky/src/models/user.dart';
import 'package:http/http.dart' as http;

class UsersProvider extends GetConnect {
  String url = Environment.API_URL + 'api/users';

  Future<Response> create(User user) async {
    Response response = await post(
      '$url/create',
      user.toJson(),
      headers: {'Content-Type': 'application/json'},
    ); // ESPERAR HASTA QUE EL SERVIDOR NOS RETORNE LA RESPUESTA

    return response;
  }

  Future<Stream<String>> createWithImage(User user, File image) async {
    final url = Environment.API_GATEWAY;
    final headers = {
      'apikey': '0f59mIgD5HKu9XSut5Q6cSTt84qjVcls',
      'Content-Type': 'application/json',
    };
    final body = json.encode({
      'query': '''
        query {
          saveStudent(input: {
            id: 1,
            nombre: "${user.name}",
            apellido: "${user.lastname}",
            carrera: "${user.career}",
            semestre: ${user.semester}
          }) {
            message
            status
          }
        }
      ''',
    });

    final response = await http.post(
      Uri.parse(url),
      headers: headers,
      body: body,
    );

    // Use logging framework instead of print
    Get.log('Response status: ${response.statusCode}');
    Get.log('Response body: ${response.body}');

    if (response.statusCode == 200) {
      final responseBody = json.decode(response.body);
      if (responseBody['errors'] != null) {
        return Stream.value('Error: ${responseBody['errors'][0]['message']}');
      }
      return Stream.value(response.body);
    } else {
      return Stream.value('Error: ${response.reasonPhrase}');
    }
  }

  /*
  * GET X
   */
  Future<ResponseApi> createUserWithImageGetX(User user, File image) async {
    FormData form = FormData({
      'image': MultipartFile(image, filename: basename(image.path)),
      'user': json.encode(user),
    });
    Response response = await post('$url/createWithImage', form);

    if (response.body == null) {
      Get.snackbar('Error en la peticion', 'No se pudo crear el usuario');
      return ResponseApi();
    }
    ResponseApi responseApi = ResponseApi.fromJson(response.body);
    return responseApi;
  }

  Future<ResponseApi> login(String email, String password) async {
    Response response = await post(
      '$url/login',
      {'email': email, 'password': password},
      headers: {'Content-Type': 'application/json'},
    ); // ESPERAR HASTA QUE EL SERVIDOR NOS RETORNE LA RESPUESTA

    if (response.body == null) {
      Get.snackbar('Error', 'No se pudo ejecutar la peticion');
      return ResponseApi();
    }

    ResponseApi responseApi = ResponseApi.fromJson(response.body);
    return responseApi;
  }
}
