import 'dart:io';
import 'dart:math';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:get_storage/get_storage.dart';
import 'package:image_picker/image_picker.dart';
import 'package:chasky/src/models/response_api.dart';
import 'package:chasky/src/models/user.dart';
import 'package:chasky/src/providers/users_provider.dart';

class RegisterController extends GetxController {
  TextEditingController nameController = TextEditingController();
  TextEditingController lastnameController = TextEditingController();
  TextEditingController careerController = TextEditingController();
  TextEditingController semesterController = TextEditingController();

  UsersProvider usersProvider = UsersProvider();

  ImagePicker picker = ImagePicker();
  File? imageFile;

  void register() async {
    String name = nameController.text;
    String lastname = lastnameController.text;
    String career = careerController.text.trim();
    String semester = semesterController.text.trim();

    print('name ${name}');

    if (isValidForm(name, lastname, career, semester)) {
      User user = User(
        name: name,
        lastname: lastname,
        career: career,
        semester: int.parse(semester),
      );

      Stream stream = await usersProvider.createWithImage(user, imageFile!);
      stream.listen((res) {
        print('name ${res}');
        ResponseApi responseApi = ResponseApi.fromJson(json.decode(res));

        if (responseApi.success == true) {
          goToHomePage();
          Get.snackbar('Registro OK', responseApi.message ?? '');
        } else {
          Get.snackbar('Registro fallido', responseApi.message ?? '');
        }
      });
    }
  }

  void goToHomePage() {
    Get.offNamedUntil('/', (route) => false);
  }

  bool isValidForm(
    String name,
    String lastname,
    String career,
    String semester,
  ) {
    if (name.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar tu nombre');
      return false;
    }

    if (lastname.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar tu apellido');
      return false;
    }

    if (career.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar tu carrera');
      return false;
    }

    if (semester.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar tu semestre');
      return false;
    }

    if (int.tryParse(semester) == null) {
      Get.snackbar('Formulario no valido', 'El semestre debe ser un número');
      return false;
    }

    if (imageFile == null) {
      Get.snackbar(
        'Formulario no valido',
        'Debes seleccionar una imagen de perfil',
      );
      return false;
    }

    return true;
  }

  Future selectImage(ImageSource imageSource) async {
    XFile? image = await picker.pickImage(source: imageSource);
    if (image != null) {
      imageFile = File(image.path);
      update();
    }
  }

  void showAlertDialog(BuildContext context) {
    Widget galleryButton = ElevatedButton(
      onPressed: () {
        Get.back();
        selectImage(ImageSource.gallery);
      },
      child: Text('GALERIA', style: TextStyle(color: Colors.black)),
    );
    Widget cameraButton = ElevatedButton(
      onPressed: () {
        Get.back();
        selectImage(ImageSource.camera);
      },
      child: Text('CAMARA', style: TextStyle(color: Colors.black)),
    );

    AlertDialog alertDialog = AlertDialog(
      title: Text('Selecciona una opcion'),
      actions: [galleryButton, cameraButton],
    );

    showDialog(
      context: context,
      builder: (BuildContext context) {
        return alertDialog;
      },
    );
  }
}
