from app import db

class User(db.Model):
    __tablename__ = "Credentials"
    email_id = db.Column(db.String(120), primary_key = True)
    password_hash = db.Column(db.String(128))
    type = db.Column(db.String(20)) # 3 types - Student, Counsellor and Teacher

    def __repr__(self):
        return '<User {}>'.format(self.email_id)

# class Student(db.Model):
    # __tablename__ = "Student"
    # s_email_id = db.Column(db.String(120), primary_key = True)
    # usn = db.Column(db.String(10), unique = True, nullable = False)
    # f_name = db.Column(db.String(250), nullable = False)
    # l_name = db.Column(db.String(250), nullable = False)
    # c_email_id = db.relationship('Counsellor',db.ForeignKey('counsellor.c_email_id'))
# 
# class Counsellor(db.Model):
    # __tablename__ = "Counsellor"
    # c_email_id = db.Column(db.String(120), primary_key = True)
    # f_name = db.Column(db.String(250), nullable = False)
    # l_name = db.Column(db.String(250), nullable = False)
    # counsellees = db.relationship('Student', backref = 'counsellor', lazy = 'dynamic')
    # dept_id = db.relationship('Department')
# 
# class Parent(db.Model):
    # __tablename__ = "Parent"
    # p_email_id = db.Column(db.String(120), primary_key = True)
    # f_name = db.Column(db.String(250))
    # l_name = db.Column(db.String(250))
    # c_email_id = db.relationship('Counsellor')
    # s_email_id = db.relationship('Student')
# 
# class Department(db.Model):
    # __tablename__ = "Department"
    # dept_id = db.Column(db.String(5), primary_key = True)
    # dept_name = db.Column(db.String(20))
    # hod_email_id = db.relationship('Counsellor')