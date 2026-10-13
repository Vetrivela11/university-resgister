class StudentNOtFoundError(Exception):
    pass
class CourseNotFoundError(Exception):  #
    pass
class CourseFullError(Exception): # course has reached its maximum capacity
    pass
class AlreadyRegisteredError(Exception):
    pass