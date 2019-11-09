from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, URL, Optional, EqualTo
from flask_login import current_user

from ..models import User


class ChangePasswordForm(FlaskForm):
    """定义修改密码表单"""
    current_password = PasswordField('当前密码', validators=[DataRequired(), Length(6, 128)])
    password = PasswordField('新的密码', validators=[DataRequired(), Length(6, 128), EqualTo('password2')])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('提交')


class ProfileForm(FlaskForm):
    """定义修改个人资料表单"""
    name = StringField('姓名', validators=[Length(1, 128)])
    bio = StringField('Bio', validators=[Optional(), Length(0, 200)])
    homepage = StringField('主页', validators=[Optional(), URL()])
    weibo = StringField('微博', validators=[Optional(), URL()])
    weixin = StringField('微信', validators=[Optional(), URL()])
    github = StringField('GitHub', validators=[Optional(), URL()])
    submit = SubmitField('提交')


class ChangeEmailForm(FlaskForm):
    email = StringField('新的邮箱', validators=[DataRequired(), Length(1, 254), Email()])
    submit = SubmitField('提交')

    def validate_email(self, field):
        """验证email是否已注册"""
        if User.objects.filter(email=field.data.lower()).first():
            raise ValidationError('该邮箱已被使用')


class DeleteAccountForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)],
                           render_kw={'placeholder':'请输入用户名确认账户'})
    submit = SubmitField('提交')

    def validate_username(self, field):
        if field.data != current_user.username:
            raise ValidationError('用户名错误')
