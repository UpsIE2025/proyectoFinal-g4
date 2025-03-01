import 'dart:convert';

User userFromJson(String str) => User.fromJson(json.decode(str));

String userToJson(User data) => json.encode(data.toJson());

class User {
  String? id; //NULL SAFETY
  String? name;
  String? lastname;
  String? career;
  int? semester;

  String? sessionToken;



  User({
    this.id,
    this.name,
    this.lastname,
    this.career,
    this.semester,

    this.sessionToken,
  });

  factory User.fromJson(Map<String, dynamic> json) => User(
    id: json["id"],
    name: json["name"],
    lastname: json["lastname"],
    career: json["career"],
    semester: json["semester"],

    sessionToken: json["session_token"],
  );

  Map<String, dynamic> toJson() => {
    "id": id,
    "name": name,
    "lastname": lastname,
    "career": career,
    "semester": semester,
    "session_token": sessionToken,
  };
}
