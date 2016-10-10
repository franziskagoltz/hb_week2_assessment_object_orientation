"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

    Encapsulation: Data living close to it's functionality
    Abstraction: Allows the user to use concepts without needing to know how exactly they work.
    Polymorphism: Allows the user to make similar, interchangable types of an object that behaves 
                  like another object. That is achieved through inheritence from the parent class.


2. What is a class?

    Classes allow us to structure our code in a certain way, they are a sort of template to create an object. 
    Class definition is creating a new namespace for variaibles and methods that will be defined within the 
    class scope and which can be accessed through dot notation. A class definition needs to be called 
    in order for a class object to be created. This is usually done through instantiating a new class object 
    or a subclass.


3. What is an instance attribute?

    An instance attribute is an attribute that is bound to the instance of a class, not the class itself.
    This could be a value that is ever class istance has or that varies with every class instance, such as the name
    or age of an animal. (referencing the example we used in class)


4. What is a method?

    A method is a function that lives within a class definition. It can be called through dot notation.


5. What is an instance in object orientation?

    An instance is a class object (in Python). Referencing question 2, when a class definition is called, 
    the class object is being created, and that said class object is an instance of the class it references.


6. How is a class attribute different than an instance attribute? Give an example of when you might use each.

    A class attribute is an attribute that lives within a class definition. It is the same for all instances of
    that class. As attribute lookup is dynamic in Python, after we set a class attribute, change it, and call
    it again on an instance of that class, that value is now updated.

    Instance attributes live on the instance of a class. They can be changed through rebinding the attribute to
    a new value, but the value won't change for other instances of the same class. Attribute lookup is from 'the 
    bottom up', meaning instance attribute take precedent. We can Update a class attribute on an instance, and it 
    won't be updated for other instances of the class. Even though that is possible, it is not recommended to
    do so. 

    An example of a class attribute is the species of an animal. If we have a dog class, all instances of that 
    class should be dogs. If they are a different species, they should belong to a different class. Since 
    we know all our instances of the dog class are dogs, we can add other dog specific attributes to the class, 
    such as a greeting for a dog being 'woof'.

    An example of an instance attribute is the name of a dog, as this should be different for every dog. Another 
    example is the age and name of owner. Even though this could be the same for two instances of our dog class, 
    it is soecific to one instance and can change without the other instance changind at the same time to the same
    new value.


"""


# Parts 2 through 5:
# Create your classes and class methods


# Part 2

class Student(object):
    """ Creates a student class, that takes three arguments.

    """

    def __init__(self, first_name, last_name, address=None):
        """ When instantiating a class object from Student three parameters
            are required, the students first name, last name, and address.
        """

        # stores the student data in a dictionary
        self.student_data = {
            'first_name': first_name,
            'last_name': last_name,
            'address': address,
            }


class Question(object):
    """ takes a question and answer as input when creatig an instance of the
        class
    """

    def __init__(self, question, correct_answer):
        """ initializes a question object that prompts the user for a question
            and its correct answer
        """

        # storing the questions and answers in a dictionary
        self.questions_and_answers = {
            "question": question,
            "correct_answer": correct_answer,
        }

    def ask_and_evaluate(self):
        """ askinf a question and evaluating the user input as the answer """

        # ask the user to answer a question
        answer = raw_input(self.questions_and_answers["question"]+" > ")

        # if the answer matches the stores answer, return true
        if answer == self.questions_and_answers["correct_answer"]:
            return True
        return False


class Exam(object):
    """ Creates an exam class that takes a name of the exam and initializes an
        empty list of questions for each exam
    """

    def __init__(self, name):
        """ initializes instance object, takes a name as a parameter and also creates an
            attribute 'questions'
        """

        self.details = {
            "name": name,
            "questions": [],
        }

    def add_question(self, question, correct_answer):
        """ takes a question and answer as a parameter, turns them into a questions and
            stores the input as a reference in Exam.details["questions"]
        """

        self.details["questions"].append(Question(question, correct_answer))

    def administer(self):
        """ loops over the questions and increses the score for every correct answer """

        score = 0.0

        # loops over the questions stored in self.details["questions"] and asks the user to
        # answer each question. For each correct answer one point is added to the score
        for question in self.details["questions"]:
            if question.ask_and_evaluate():
                score += 1
        return score


class Quiz(Exam):
    """ A subclass of Exam, only returns true or false for pass/fail inseadt of a score """

    def administer(self):
        """ Quiz version of administer function in Exam class. Returns true or false as pass or
            fail, no scores """

        # gets the user score from the parent class function and stores the result in 'score'
        score = super(Quiz, self).administer()

        # if score is larger or equal to questions/2 (meaning they answered at least half of
        # the questions correctly), return true
        if score >= len(self.details["questions"])/2:
            return True
        return False


def take_test(exam, student):
    """ takes a student and an exam as parameter and adminsters the exam """

    # sets student score equal to the returned result of administer()
    student.score = exam.administer()


def example():
    """ example function: creates exam, adds questions to it, creates a student
        has the student take the exam and returns the score
    """

    # creating a final exam
    final = Exam("Final")

    # adding questions to the exam
    final.add_question("Color of the sky", "blue")
    final.add_question("Color of the grass", "green")
    final.add_question("Color of the sun", "yellow")

    # creating a student instance
    timothy = Student("timothy", "jones", "1010 Binary Drive")

    take_test(exam=final, student=timothy)

    return timothy.score


def exampleQuiz():
    """ example quiz function: creates quiz, adds questions to it, creates a student
        has the student take the exam and returns the score
    """

    # creating a final exam
    final = Quiz("Final")

    # adding questions to the exam
    final.add_question("Color of the sky", "blue")
    final.add_question("Color of the grass", "green")
    final.add_question("Color of the sun", "yellow")

    # creating a student instance
    timothy = Student("timothy", "jones", "1010 Binary Drive")

    take_test(exam=final, student=timothy)

    return timothy.score




















