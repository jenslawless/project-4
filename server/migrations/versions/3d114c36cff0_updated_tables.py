"""updated tables

Revision ID: 3d114c36cff0
Revises: 
Create Date: 2023-07-17 14:29:17.831171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d114c36cff0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['users.id'], name=op.f('fk_courses_teacher_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_courses'))
    )
    op.create_table('assignments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('course_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_assignments_course_id_courses')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_assignments'))
    )
    op.create_table('enrollments',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.id'], name=op.f('fk_enrollments_course_id_courses')),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], name=op.f('fk_enrollments_student_id_users')),
    sa.PrimaryKeyConstraint('student_id', 'course_id', name=op.f('pk_enrollments'))
    )
    op.create_table('grades',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('assignment_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['assignment_id'], ['assignments.id'], name=op.f('fk_grades_assignment_id_assignments')),
    sa.ForeignKeyConstraint(['student_id'], ['users.id'], name=op.f('fk_grades_student_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_grades'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('grades')
    op.drop_table('enrollments')
    op.drop_table('assignments')
    op.drop_table('courses')
    op.drop_table('users')
    # ### end Alembic commands ###