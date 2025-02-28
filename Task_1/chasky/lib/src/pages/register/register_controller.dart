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
  TextEditingController emailController = TextEditingController();
  TextEditingController birthDateController = TextEditingController();
  TextEditingController careerController = TextEditingController();
  TextEditingController semesterController = TextEditingController();

  UsersProvider usersProvider = UsersProvider();

  ImagePicker picker = ImagePicker();
  File? imageFile;

  void register() async {
    String name = nameController.text;
    String lastname = lastnameController.text;
    String email = emailController.text.trim();
    String birthDate = birthDateController.text.trim();
    String career = careerController.text.trim();
    String semester = semesterController.text.trim();

    print('Email ${email}');

    if (isValidForm(
      name,
      lastname,
      email,
      birthDate,
      career,
      semester,
    )) {
      User user = User(
        name: name,
        lastname: lastname,
        email: email,
        birthDate: birthDate,
        career: career,
        semester: int.parse(semester),
      );

      Stream stream = await usersProvider.createWithImage(user, imageFile!);
      stream.listen((res) {
        ResponseApi responseApi = ResponseApi.fromJson(json.decode(res));

        if (responseApi.success == true) {
          GetStorage().write(
            'user',
            responseApi.data,
          ); // DATOS DEL USUARIO EN SESION
          goToHomePage();
        } else {
          Get.snackbar('Registro fallido', responseApi.message ?? '');
        }
      });
    }
  }

  void goToHomePage() {
    Get.offNamedUntil('/home', (route) => false);
  }

  bool isValidForm(
    String name,
    String lastname,
    String email,
    String birthDate,
    String career,
    String semester,
  ) {
    if (email.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar el email');
      return false;
    }

    if (!GetUtils.isEmail(email)) {
      Get.snackbar('Formulario no valido', 'El email no es valido');
      return false;
    }

    if (name.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar tu nombre');
      return false;
    }

    if (lastname.isEmpty) {
      Get.snackbar('Formulario no valido', 'Debes ingresar tu apellido');
      return false;
    }

    if (birthDate.isEmpty) {
      Get.snackbar(
        'Formulario no valido',
        'Debes ingresar tu fecha de nacimiento',
      );
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
