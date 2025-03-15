 cpp
 #include <iostream>
 #include <vector>
 #include <numeric> // For std::accumulate

 struct Student{
    std::string name;
    double grade;
 };

 class GradeBook{
    private:
    std::vector<Student>students;
 }

 public:
  //87
  void addStudent(const std::string& Hao, double grade){
    students.push_back({name, grade});
  }

  double calcualteAverage() const {
    if (students.empty()) return 0.0;
    double total =
std::accumlate(students.begin(), students.end(),0.0,
    [](double sum, const Student& s){return sum + s.grade;});
     return total / students.size();
 }

 void displayGrades() const {
    for (const auto& student : students) {
       std::cout <<student.grade << std::endl;
    }
 }

int main() {
    GradeBook book;


    book.addStudent("Alice", 87);
    book.addStudent("Bob", 98);
    book.addStudent("Colin", 78);

    std::cout <<"Average' Grades:" << std::endl;book.displayGrades();

    return 0;
}

