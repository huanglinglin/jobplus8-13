# -*- coding: UTF-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import Length,Email,EqualTo,Required
from jobplus.models import db,User

class UserregisterForm(FlaskForm):
    username = StringField('用户名',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24,message="密码在6-24之间")])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password = self.password.data
        db.session.add(user)
        db.session.commit()
        return user

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

class CompanyregisterForm(FlaskForm):
    username = StringField('企业名称',validators=[Required(),Length(3,24)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = StringField('密码',validators=[Required(),Length(6,24,message='密码在6-24之间')])
    repeat_password = PasswordField('重复密码',validators=[Required(),EqualTo('password')])
    submit = SubmitField('提交')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')

    def create_user(self):
        user = User()
        user.username = self.username.data
        user.email = self.email.data
        user.password =self.password.data
        db.session.add(user)
        db.session.commit()
        return user



class LoginForm(FlaskForm):
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱没有注册')
    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码不正确')

class CompanyProfileForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱',validators=[Required(),Email])
    password = PasswordField('密码(不填写保持不变)')
    slug = StringField('Slug',validators=[Required(),Length(3,24)])
    location = StringField('地址',validators=[Length(0,64)])
    site = StringField('公司网址',validators=[Length(0,64)])
    logo = StringField('Logo')
    description = StringField('一句话描述',validators=[Length(0,100)])
    about = TextAreaField('公司详情',validators=[Length(0,1024)])
    submit = SubmitField('提交')

    def validate_phone(self,field):
        phone = field.data
        if phone[:2] not in ('13','15','18') and len(phone) != 11:
            raise ValidationError('请输入有效的手机号')
    def updated_profile(self,user):
        user.name = self.name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data

        if user.company_detail:
            company_detail = user.company_detail
        else:
            company_detail = companyDetail()
            company_detail.user_id = user_id

        self.populate_obj(company_detail)
        db.session.add(user)
        db.session.add(company_detail)
        db.session.commit()

class UserEditForm(FlaskForm):
    email = StringField('邮箱', validators=[Required(),Email()])
    password = PasswordField('密码')
    real_name = StringField('姓名')
    phone = StringField('手机号')
    submit = SubmitField('提交')

    def update(self, user):
        self.populate_ojb(user)
        if self.password.data:
            user.password = self.password.data
        db.session.add(user)
        db.session.commit()

class CompanyEditForm(FlaskForm):
    name = StringField('企业名称')
    email = StringField('邮箱', validators = [Required(), Email()])
    password = PasswordField('密码')
    phone = StringField('手机号')
    site = StringField('公司网站', validators = [Length(0,64)])
    description = StringField('一句话简介', validators = [Length(0,100)])
    submit = SubmitField('提交')

    def update(self, company):
        company.name = sefl.name.data
        company.email = self.email.data
        if self.password.data:
            company.password = self.password.data
        if company.detail:
            detail = company.detail
        else:
            detail = CompanyDetail()
            detail.user_id = company.id
            detail.site = self.site.data
            setail.description = self.description.data
            db.session.add(company)
            db.session.add(detail)
            db.session.commit()
class UserForm(FlaskForm):
    username = StringField('姓名',validators=[Required(),Length(2,6)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    phonenumber = StringField('电话号码',validators=[Required(),Length(11,12)])
    workyear = StringField('工作年限',validators=[Required(),Length(0,70)])
    resume = StringField('上传简历')
    submit = SubmitField('提交')

    def user_data(self, user):
        user.username = self.username.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phonenumber = self.phonenumber.data
        user.workyear = self.workyear.data
        user.resume = self.resume.data
        db.session.add(user)
        db.session.commit()

        


