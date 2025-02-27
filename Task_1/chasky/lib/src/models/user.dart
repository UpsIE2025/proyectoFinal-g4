import 'dart:convert';

User userFromJson(String str) => User.fromJson(json.decode(str));

String userToJson(User data) => json.encode(data.toJson());

class User {
  String? id; //NULL SAFETY
  String? name;
  String? lastname;
  String? email;
  String? birthDate;
  String? career;
  int? semester;

  String? sessionToken;



  User({
    this.id,
    this.name,
    this.lastname,
    this.email,
    this.birthDate,
    this.career,
    this.semester,

    this.sessionToken,
  });

  factory User.fromJson(Map<String, dynamic> json) => User(
    id: json["id"],
    name: json["name"],
    lastname: json["lastname"],
    email: json["email"],
    birthDate: json["birth_date"],
    career: json["career"],
    semester: json["semester"],

    sessionToken: json["session_token"],
  );

  Map<String, dynamic> toJson() => {
    "id": id,
    "name": name,
    "lastname": lastname,
    "email": email,
    "birth_date": birthDate,
    "career": career,
    "semester": semester,
    "session_token": sessionToken,
  };
}
