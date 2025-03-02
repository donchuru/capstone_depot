from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FieldList, FormField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired

YEARS = sorted([2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024], reverse=True)

CATEGORIES = sorted([' ', 'Chemical Engineering', 'Civil Engineering', 'Computer Engineering', 'Software Engineering', 'Electrical Engineering', 'Engineering Physics', 'Materials Engineering', 'Mechanical Engineering', 'Mining Engineering', 'Petroleum Engineering', 'Biomedical Engineering (MSc)'])

class TeamMemberField(FlaskForm):
    name = StringField('Team Member')
    linkedin_url = StringField('LinkedIn URL')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    year = SelectField('Select the year you completed your project', choices = YEARS, validate_choice=True, validators=[DataRequired()])
    team_members = StringField('Add team members', validators=[DataRequired()])
    category = SelectField('Choose your department', choices = CATEGORIES, validate_choice=True, validators=[DataRequired()])
    content = TextAreaField('Give a description of the project', validators=[DataRequired()])
    link = StringField('Enter link to presentation (Optional)')
    poster = FileField('Upload Presentation Poster (Accepted filetypes: jpg, png)', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Upload')
