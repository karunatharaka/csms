from app import db

class User(db.Model):
    __tablename__ = "Credentials"
    email_id = db.Column(db.String(120), primary_key = True)
    password_hash = db.Column(db.String(128), nullable = False)
    type = db.Column(db.String(20), nullable = False) # 3 types - Student, Counsellor and Teacher

    def __repr__(self):
        return '<User {}>'.format(self.email_id)

class Student(db.Model):
    __tablename__ = "Student"
    s_email_id = db.Column(db.String(120), primary_key = True)
    usn = db.Column(db.String(10), unique = True, nullable = False)
    f_name = db.Column(db.String(250), nullable = False)
    l_name = db.Column(db.String(250), nullable = False)
    c_email_id = db.Column(db.String(120),db.ForeignKey('Counsellor.c_email_id'))

class Counsellor(db.Model):
    __tablename__ = "Counsellor"
    c_email_id = db.Column(db.String(120), primary_key = True)
    f_name = db.Column(db.String(250), nullable = False)
    l_name = db.Column(db.String(250), nullable = False)
    dept_id = db.Column(db.String(5),db.ForeignKey('Department.dept_id'))

    counsellees = db.relationship('Student', backref = db.backref('counsellor',lazy = 'joined'), lazy = 'subquery')

class Parent(db.Model):
    __tablename__ = "Parent"
    p_email_id = db.Column(db.String(120), primary_key = True)
    f_name = db.Column(db.String(250),nullable = False)
    l_name = db.Column(db.String(250),nullable = False)
    c_email_id = db.Column(db.String(120),db.ForeignKey('Counsellor.c_email_id'))
    s_email_id = db.Column(db.String(120),db.ForeignKey('Student.s_email_id'))

    child = db.relationship('Student', backref = db.backref('parent', lazy = 'joined'), lazy = 'joined')
    counsellor = db.relationship('Counsellor', backref = db.backref('parent', lazy = 'select'), lazy = 'joined')
    

class Department(db.Model):
    __tablename__ = "Department"
    dept_id = db.Column(db.String(5), primary_key = True)
    dept_name = db.Column(db.String(20),nullable = False)
    hod_email_id = db.Column(db.String(120),db.ForeignKey('Counsellor.c_email_id'))

    hod = db.relationship('Counsellor', backref = db.backref('managing-department', lazy = 'select'), lazy = 'joined')
    professors = db.relationship(db.String(120),backref = db.backref('department', lazy = 'joined'), lazy = 'select')
class Course(db.Model):
    __tablename__ = "Course"
    course_code = db.Column(db.String(10), primary_key = True)
    course_name = db.Column(db.String(50),nullable = False)
    dept_id = db.Column(db.String(5),db.ForeignKey('Department.dept_id'))
    department= db.relationship('Department', backref = db.backref('Course', lazy = 'select'), lazy = 'joined')

   